init python:

    import re

    # ----------------------------
    # Helpers
    # ----------------------------

    def normalize_secret(text):
        # Keep everything, only normalize case
        # Now punctuation is preserved and meaningful
        return text.upper()


    # ----------------------------
    # Censor logic (PURE FUNCTION)
    # ----------------------------

    def censor_filter(text):

        if not persistent.censor_mode:
            return text

        if persistent.message_index >= len(store.hidden_messages):
            return text

        secret = normalize_secret(store.hidden_messages[persistent.message_index])

        result = []

        i = 0

        # local copies (avoid mid-render mutation issues)
        letter_index = persistent.letter_index
        message_index = persistent.message_index

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

                    if message_index < len(store.hidden_messages):
                        secret = normalize_secret(
                            store.hidden_messages[message_index]
                        )
                    else:
                        message_index = len(store.hidden_messages)

            else:
                # Everything else is censored (including punctuation)
                if ch.isspace():
                    result.append(ch)   # keep spacing readable
                else:
                    result.append("█")

            i += 1

        # commit persistent state AFTER rendering pass
        persistent.letter_index = letter_index
        persistent.message_index = message_index

        return "".join(result)


    # ----------------------------
    # Override renpy.say
    # ----------------------------

    _original_say = renpy.say


    def censored_say(who, what, *args, **kwargs):

        if isinstance(what, str):

            # 1. FIRST: resolve interpolation ([var], [name], etc.)
            try:
                rendered = renpy.substitute(what)
            except Exception:
                rendered = what

            # 2. THEN: apply censoring
            what = censor_filter(rendered)

        return _original_say(who, what, *args, **kwargs)


    renpy.say = censored_say