init python:

    import re
    import random

    # ----------------------------
    # Helpers
    # ----------------------------

    def normalize_secret(text):
        # Keep everything, only normalize case
        # Now punctuation is preserved and meaningful
        return text.upper()

    def clean_dialogue_text(text):
        if text is None:
            return ""
        rendered = renpy.substitute(str(text))
        rendered = re.sub(r"\{[^}]*\}", "", rendered)
        rendered = re.sub(r"\[[^\]]+\]", "", rendered)
        rendered = re.sub(r"\s+", " ", rendered)
        return rendered.strip()

    def line_score(text):
        cleaned = clean_dialogue_text(text)
        chars = [ch.lower() for ch in cleaned if not ch.isspace()]
        if not chars:
            return 0
        unique = len(set(chars))
        return (len(chars) * 2) + (unique * 6)

    def get_active_secret():
        messages = getattr(store, "hidden_messages", [])
        index = int(getattr(persistent, "message_index", 0))
        if not messages or index < 0 or index >= len(messages):
            return ""
        return normalize_secret(str(messages[index]))

    def progressive_match_score(line, secret):
        if not line or not secret:
            return 0

        text_chars = [ch.lower() for ch in clean_dialogue_text(line) if not ch.isspace()]
        secret_chars = [ch.lower() for ch in secret if not ch.isspace()]

        if not text_chars or not secret_chars:
            return 0

        best_run = 0

        for start in range(len(text_chars)):
            run = 0
            while start + run < len(text_chars) and run < len(secret_chars):
                if text_chars[start + run] == secret_chars[run]:
                    run += 1
                else:
                    break
            if run > best_run:
                best_run = run

        return best_run

    def get_am_allowed_speakers():
        speakers = getattr(persistent, "am_allowed_speakers", ["Abigail"])
        if not isinstance(speakers, (list, tuple, set)):
            return ["Abigail"]
        return [str(s) for s in speakers if str(s).strip()]

    def split_secret_into_segments(secret_text, max_chars=20):
        text = clean_dialogue_text(secret_text)
        if not text:
            return []

        segments = []
        index = 0

        while index < len(text):
            end = min(index + max_chars, len(text))
            segment = text[index:end].strip()
            if not segment:
                index = end
                continue

            if end < len(text):
                split_at = max(segment.rfind(" "), segment.rfind("-"), segment.rfind("."), segment.rfind("!"), segment.rfind("?"), segment.rfind(","), segment.rfind(":"), segment.rfind(";"))
                if split_at > max_chars // 2:
                    end = index + split_at + 1
                    segment = text[index:end].strip()

            segments.append(segment)
            index = end

        return [segment for segment in segments if segment]

    def choose_am_voice_line(secret_text=None):
        pool = getattr(persistent, "am_voice_pool", {})
        if not isinstance(pool, dict):
            pool = {}

        secret = normalize_secret(clean_dialogue_text(secret_text)) if secret_text else get_active_secret()
        if not secret:
            secret = "GREETINGS"

        best_line = None
        best_rank = (-1, -1, "")

        for speaker in get_am_allowed_speakers():
            lines = pool.get(speaker, [])
            if not isinstance(lines, list):
                continue

            for line in lines:
                if not isinstance(line, str):
                    continue

                cleaned = clean_dialogue_text(line)
                if not cleaned:
                    continue

                match_count = progressive_match_score(cleaned, secret)
                if match_count <= 0:
                    continue

                rank = (match_count, len(cleaned), cleaned.lower())
                if rank > best_rank:
                    best_line = cleaned
                    best_rank = rank

        if best_line is not None:
            return best_line

        filler = [
            "I keep hearing it in the quiet.",
            "The room keeps repeating it softly.",
            "It slips through the walls like a warning.",
            "The silence keeps whispering the same thing.",
        ]
        frame = random.choice(filler)
        return frame + " greetings " + random.choice(filler)

    def is_lilith_speaker(who, who_name=None):
        lilith_char = getattr(store, "l", None)
        if who is lilith_char:
            return True

        if who_name is None:
            who_name = getattr(who, "who", None)
            if who_name is None:
                who_name = str(who)

        speaker_name = str(who_name).strip().upper()
        date_name = str(getattr(persistent, "date", "")).strip().upper()

        if date_name and speaker_name == date_name:
            return True

        return speaker_name == "LILITH"

    def get_am_possession_target():
        targets = getattr(store, "am_possession_targets", [])
        if not isinstance(targets, (list, tuple)) or not targets:
            return ""

        index = int(getattr(store, "am_possession_index", 0))
        if index < 0:
            index = 0
        if index >= len(targets):
            index = len(targets) - 1

        target = clean_dialogue_text(targets[index])
        return target

    def advance_am_possession_target():
        targets = getattr(store, "am_possession_targets", [])
        if not isinstance(targets, (list, tuple)) or not targets:
            return

        index = int(getattr(store, "am_possession_index", 0))
        if index < len(targets) - 1:
            setattr(store, "am_possession_index", index + 1)

    def non_space_char_count(text):
        return len([ch for ch in clean_dialogue_text(text) if not ch.isspace()])

    def choose_possession_source_line(current_line, secret_text):
        source_line = clean_dialogue_text(current_line)
        needed = non_space_char_count(secret_text)

        if non_space_char_count(source_line) >= needed:
            return source_line

        recent_lilith = getattr(store, "am_recent_lilith_lines", [])
        if not isinstance(recent_lilith, (list, tuple)):
            recent_lilith = []

        recent_viable = []
        for line in recent_lilith:
            cleaned = clean_dialogue_text(line)
            if cleaned and non_space_char_count(cleaned) >= needed:
                recent_viable.append(cleaned)

        if recent_viable:
            return random.choice(recent_viable)

        fallback_pool = getattr(store, "am_possession_lilith_pool", [])
        if not isinstance(fallback_pool, (list, tuple)):
            fallback_pool = []

        viable = []
        for line in fallback_pool:
            cleaned = clean_dialogue_text(line)
            if cleaned and non_space_char_count(cleaned) >= needed:
                viable.append(cleaned)

        if viable:
            return random.choice(viable)

        if fallback_pool:
            cleaned_pool = [clean_dialogue_text(line) for line in fallback_pool if clean_dialogue_text(line)]
            if cleaned_pool:
                return random.choice(cleaned_pool)

        return source_line

    def remember_lilith_line(line):
        cleaned = clean_dialogue_text(line)
        if not cleaned:
            return

        history = getattr(store, "am_recent_lilith_lines", None)
        if not isinstance(history, list):
            history = []

        history.append(cleaned)
        if len(history) > 80:
            history = history[-80:]

        setattr(store, "am_recent_lilith_lines", history)

    def force_censor_to_secret(source_text, secret_text):
        source = clean_dialogue_text(source_text)
        secret = clean_dialogue_text(secret_text)
        if not secret:
            return source

        secret_chars = [ch for ch in secret if not ch.isspace()]
        if not source:
            source = " ".join(secret_chars)

        result = []
        secret_index = 0

        for ch in source:
            if ch.isspace():
                result.append(" ")
                continue

            if secret_index < len(secret_chars):
                result.append(secret_chars[secret_index])
                secret_index += 1
            else:
                result.append(censor_block())

        while secret_index < len(secret_chars):
            result.append(secret_chars[secret_index])
            secret_index += 1

        return "".join(result)

    def am_possess_lilith_line(current_line):
        target = get_am_possession_target()
        if not target:
            return clean_dialogue_text(current_line)

        source = choose_possession_source_line(current_line, target)
        return force_censor_to_secret(source, target)

    def censor_block():
        return "{font=DejaVuSans.ttf}{color=#000}█{/color}{/font}"

    def censor_to_secret(text, secret_text):
        if text is None:
            return ""

        secret = normalize_secret(clean_dialogue_text(secret_text))
        if not secret:
            return text

        reveal_chars = [ch for ch in secret if not ch.isspace()]
        if not reveal_chars:
            return text

        source = clean_dialogue_text(text)
        if not source:
            return "".join(reveal_chars)

        result = []
        secret_index = 0

        for ch in source:
            if ch.isspace():
                result.append(" ")
                continue

            if secret_index < len(reveal_chars) and ch.upper() == reveal_chars[secret_index].upper():
                result.append(ch)
                secret_index += 1
            else:
                result.append(censor_block())

        while secret_index < len(reveal_chars):
            result.append(censor_block())
            secret_index += 1

        return "".join(result)

    def am_censored_voice_line(secret_text=None):
        secret = secret_text if secret_text else get_active_secret()
        line = choose_am_voice_line(secret)
        if not secret:
            return line
        return censor_to_secret(line, secret)

    # ----------------------------
    # Censor logic (PURE FUNCTION)
    # ----------------------------

    def censor_filter(text):

        if not persistent.censor_mode:
            return text

        hidden_messages = getattr(store, "hidden_messages", [])

        if persistent.message_index >= len(hidden_messages):
            return text

        secret = normalize_secret(hidden_messages[persistent.message_index])

        result = []

        i = 0

        # local copies (avoid mid-render mutation issues)
        letter_index = int(getattr(persistent, "letter_index", 0))
        message_index = int(getattr(persistent, "message_index", 0))

        while i < len(text):

            # Preserve Ren'Py text tags like {color=#fff}
            if text[i] == "{":
                end = text.find("}", i)
                if end != -1:
                    result.append(text[i:end + 1])
                    i = end + 1
                    continue

            ch = text[i]

            # --------------------------------
            # MATCHING LOGIC (NOW INCLUDES PUNCTUATION)
            # --------------------------------
            if letter_index < len(secret) and ch.upper() == secret[letter_index]:

                result.append(ch)
                letter_index += 1

                # advance secret when fully matched
                if letter_index >= len(secret):
                    letter_index = 0
                    message_index += 1

                    if message_index < len(hidden_messages):
                        secret = normalize_secret(
                            hidden_messages[message_index]
                        )
                    else:
                        message_index = len(hidden_messages)

            else:
                # Everything else is censored (including punctuation)
                if ch.isspace():
                    result.append(ch)   # keep spacing readable
                else:
                    result.append(censor_block())

            i += 1

        # commit persistent state AFTER rendering pass
        setattr(persistent, "letter_index", letter_index)
        setattr(persistent, "message_index", message_index)

        return "".join(result)


    # ----------------------------
    # Override renpy.say
    # ----------------------------

    _original_say = renpy.say


    def censored_say(who, what, *args, **kwargs):

        if isinstance(what, str):

            try:
                rendered = renpy.substitute(what)
            except Exception:
                rendered = what

            who_name = getattr(who, "who", None)
            if who_name is None:
                who_name = str(who)

            if "A.M" in str(who_name).upper():
                secret = clean_dialogue_text(rendered)
                if secret:
                    segments = split_secret_into_segments(secret)
                    if len(segments) > 1:
                        first_segment = segments[0]
                        first_source = choose_am_voice_line(first_segment)
                        first_what = censor_to_secret(first_source, first_segment)
                        result = _original_say(who, first_what, *args, **kwargs)
                        for segment in segments[1:]:
                            renpy.call_in_new_context("am_followup_say", who, segment)
                        return result

                    source = choose_am_voice_line(secret)
                    what = censor_to_secret(source, secret)
                else:
                    what = censor_filter(rendered)
            elif getattr(store, "am_possession_active", False) and is_lilith_speaker(who, who_name):
                what = am_possess_lilith_line(rendered)
                advance_am_possession_target()
            else:
                if is_lilith_speaker(who, who_name):
                    remember_lilith_line(rendered)
                what = censor_filter(rendered)

        return _original_say(who, what, *args, **kwargs)


    renpy.say = censored_say