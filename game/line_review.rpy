
init -1 python:

    import json
    import os
    import datetime
    import threading
    import urllib.request
    import urllib.error
    import ssl

    ## Credentials are loaded from game/review_credentials.rpy (gitignored).
    ## Fallback to empty strings if that file is missing (send/pull will error
    ## gracefully with a message instead of crashing).
    if not hasattr(store, "_REVIEW_WEBHOOK_URL"):
        _REVIEW_WEBHOOK_URL = u""
    if not hasattr(store, "_REVIEW_BOT_TOKEN"):
        _REVIEW_BOT_TOKEN = u""
    if not hasattr(store, "_REVIEW_CHANNEL_ID"):
        _REVIEW_CHANNEL_ID = u""  ## blank = auto-detect from webhook URL

    ## Where reviews are written.
    _review_save_path = os.path.join(config.basedir, "line_reviews.json")


    _review_rating  = None   # "up" | "down" | None
    _review_tag     = None   # "rewrite" | "keep" | "feedback" | "question"
    _review_reason  = u""
    _review_reviewer = u""
    _review_submit_msg = u""   # brief flash message after saving

    ## -------------------------------------------------------------------------
    ## File I/O helpers
    ## -------------------------------------------------------------------------

    def _review_load_all():
        """Return the full list of saved review entries (list of dicts)."""
        if os.path.exists(_review_save_path):
            try:
                with open(_review_save_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def _review_write_all(entries):
        try:
            with open(_review_save_path, "w", encoding="utf-8") as f:
                json.dump(entries, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False

    def _review_save_entry(who, what, rating, tag, reason, reviewer, priority=None):
        """
        Append a new review entry to line_reviews.json.
        Returns True on success, False on failure.
        """
        entries = _review_load_all()

        try:
            fname, lineno = renpy.get_filename_line()
        except Exception:
            fname, lineno = "unknown", 0

        entry = {
            "timestamp"   : datetime.datetime.now().isoformat(sep=" ", timespec="seconds"),
            "game_version": config.version,
            "reviewer"    : reviewer.strip() if reviewer.strip() else "anonymous",
            "file"        : fname,
            "line"        : lineno,
            "who"         : who  if who  else "narration",
            "dialogue"    : what if what else "",
            "rating"      : rating if rating else "none",
            "tag"         : tag      if tag      else "none",
            "priority"    : priority  if priority  else "none",
            "reason"      : reason.strip(),
            "resolved"    : False,
        }

        entries.append(entry)

        try:
            with open(_review_save_path, "w", encoding="utf-8") as f:
                json.dump(entries, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False

    def _review_do_submit(rating, tag, reason, reviewer, priority=None):
        """Save a review; called from the panel screen with screen-local values."""
        who  = u""
        what = u""
        try:
            if _history_list:
                entry = _history_list[-1]
                who  = entry.who  if entry.who  else u""
                what = entry.what if entry.what else u""
        except Exception:
            pass
        return _review_save_entry(
            who      = who,
            what     = what,
            rating   = rating,
            tag      = tag,
            reason   = reason,
            reviewer = reviewer,
            priority = priority,
        )

    ## -------------------------------------------------------------------------
    ## Discord webhook sender – background thread so the game doesn't freeze.
    ## Status is written to store._review_email_status so screens react:
    ##   "" | "sending" | "sent" | "error:<msg>"
    ## -------------------------------------------------------------------------

    def _review_set_status(val):
        """Write status into Ren'Py store from any thread so screens redraw."""
        ## Escape { and } so Ren'Py doesn't try to parse JSON as text tags.
        store._review_email_status = val.replace(u"{", u"{{").replace(u"}", u"}}")

    def _review_send_email_thread():
        try:
            ## Guard against placeholder URL
            if "YOUR_ID" in _REVIEW_WEBHOOK_URL or "YOUR_TOKEN" in _REVIEW_WEBHOOK_URL:
                renpy.invoke_in_main_thread(
                    _review_set_status,
                    u"error:Webhook URL is still a placeholder – paste your real Discord webhook URL into line_review.rpy"
                )
                return

            entries = _review_load_all()
            count   = len(entries)
            version = config.version
            now     = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")

            ## ---- Build message chunks (Discord max 2000 chars each) --------
            header = (
                "**Groundhog Date with Lilith \u2013 Review Report**\n"
                "Game version : `{}`\n"
                "Sent at      : {}\n"
                "Total reviews: **{}**\n"
            ).format(version, now, count)

            chunks   = []
            current  = header
            for i, e in enumerate(entries, 1):
                rat    = e.get("rating", "none")
                tag    = e.get("tag", "none")
                pri    = e.get("priority", "none")
                rat_ic = "\ud83d\udc4d" if rat == "up" else ("\ud83d\udc4e" if rat == "down" else "\u2013")
                pri_ic = {"low":"\ud83d\udfe2","medium":"\ud83d\udfe1","high":"\ud83d\udd34"}.get(pri, "")
                pri_str = " {} {}".format(pri_ic, pri) if pri != "none" else ""
                block  = "**[{}]** {} `{}` | v{} | {} | by {}{}\n".format(
                    i, rat_ic, tag,
                    e.get("game_version", "?"),
                    e.get("timestamp", "?"),
                    e.get("reviewer", "anon"),
                    pri_str,
                )
                if e.get("who"):
                    block += "> *{}*: {}\n".format(e.get("who", ""), e.get("dialogue", ""))
                if e.get("reason"):
                    block += "> \ud83d\udcac {}\n".format(e.get("reason", ""))
                block += "\n"

                if len(current) + len(block) > 1900:
                    chunks.append(current)
                    current = block
                else:
                    current += block

            if current.strip():
                chunks.append(current)

            ## ---- POST each chunk as a plain JSON message -------------------
            ssl_ctx = ssl._create_unverified_context()
            for chunk in chunks:
                payload = json.dumps({
                    "content"  : chunk,
                    "username" : "GDWL Review Bot",
                }).encode("utf-8")
                req = urllib.request.Request(
                    _REVIEW_WEBHOOK_URL,
                    data    = payload,
                    headers = {
                        "Content-Type" : "application/json",
                        "User-Agent"   : "GDWLReviewBot/1.0",
                    },
                    method  = "POST",
                )
                try:
                    urllib.request.urlopen(req, timeout=15, context=ssl_ctx)
                except urllib.error.HTTPError as http_err:
                    body = http_err.read().decode("utf-8", errors="replace")
                    raise Exception("HTTP {} – {}".format(http_err.code, body))

            ## ---- POST one machine-readable tagged message per entry --------
            ## These are used by the Pull function to import reviews from Discord.
            ## Format: GDWL_ENTRY:<json>
            ## The bot-token pull fetches these and merges them into line_reviews.json.
            for entry in entries:
                tagged = "GDWL_ENTRY:" + json.dumps(entry, ensure_ascii=False)
                ## Truncate if somehow over 2000 chars (extremely unlikely for one entry)
                if len(tagged) > 1990:
                    tagged = tagged[:1990]
                ep = json.dumps({
                    "content"  : tagged,
                    "username" : "GDWL Review Bot",
                }).encode("utf-8")
                req2 = urllib.request.Request(
                    _REVIEW_WEBHOOK_URL,
                    data    = ep,
                    headers = {
                        "Content-Type" : "application/json",
                        "User-Agent"   : "GDWLReviewBot/1.0",
                    },
                    method  = "POST",
                )
                try:
                    urllib.request.urlopen(req2, timeout=15, context=ssl_ctx)
                except urllib.error.HTTPError as http_err:
                    body = http_err.read().decode("utf-8", errors="replace")
                    raise Exception("HTTP {} – {}".format(http_err.code, body))

            renpy.invoke_in_main_thread(_review_set_status, u"sent")

        except Exception as ex:
            renpy.invoke_in_main_thread(_review_set_status, u"error:" + str(ex))

    def _review_send_email():
        renpy.invoke_in_main_thread(_review_set_status, u"sending")
        t = threading.Thread(target=_review_send_email_thread)
        t.daemon = True
        t.start()

    ## -------------------------------------------------------------------------
    ## Discord Bot pull – fetch GDWL_ENTRY messages from the channel and merge
    ## them into the local line_reviews.json.
    ## Requires _REVIEW_BOT_TOKEN and _REVIEW_CHANNEL_ID to be set above.
    ## Status is written to store._review_pull_status:
    ##   "" | "pulling" | "pulled:N" | "error:<msg>"
    ## -------------------------------------------------------------------------

    def _review_set_pull_status(val):
        ## Escape { and } so Ren'Py doesn't try to parse JSON as text tags.
        store._review_pull_status = val.replace(u"{", u"{{").replace(u"}", u"}}")

    def _review_pull_thread():
        try:
            ## Dump the live token prefix to a file so we can verify it
            _dbg = os.path.join(config.basedir, "token_debug.txt")
            with open(_dbg, "w", encoding="utf-8") as _f:
                _f.write(u"token_prefix={}\nwebhook_prefix={}\n".format(
                    repr(_REVIEW_BOT_TOKEN[:30]),
                    repr(_REVIEW_WEBHOOK_URL[:50]),
                ))

            ## Guard against placeholder bot token
            if "YOUR_BOT_TOKEN" in _REVIEW_BOT_TOKEN:
                renpy.invoke_in_main_thread(
                    _review_set_pull_status,
                    u"error:Bot token not configured – see line_review.rpy"
                )
                return

            ssl_ctx = ssl._create_unverified_context()

            ## ---- Auto-resolve channel ID from the webhook URL --------------
            ## A GET request to the webhook URL (no auth needed) returns JSON
            ## that includes the channel_id the webhook posts to.
            channel_id = _REVIEW_CHANNEL_ID
            if not channel_id or "YOUR_CHANNEL" in channel_id:
                try:
                    wh_req = urllib.request.Request(
                        _REVIEW_WEBHOOK_URL,
                        headers = {"User-Agent": "GDWLReviewBot/1.0"},
                        method  = "GET",
                    )
                    with urllib.request.urlopen(wh_req, timeout=15, context=ssl_ctx) as wh_resp:
                        wh_info    = json.loads(wh_resp.read().decode("utf-8"))
                        channel_id = str(wh_info.get("channel_id", ""))
                except Exception as wh_ex:
                    renpy.invoke_in_main_thread(
                        _review_set_pull_status,
                        u"error:Could not resolve channel from webhook – " + str(wh_ex)
                    )
                    return

            if not channel_id:
                renpy.invoke_in_main_thread(
                    _review_set_pull_status,
                    u"error:Channel ID could not be determined. Set _REVIEW_CHANNEL_ID manually."
                )
                return

            all_parsed    = []
            total_fetched = 0
            before_id     = None   ## used for pagination

            ## Fetch up to 500 messages (5 pages × 100), newest first
            for _page in range(5):
                url = "https://discord.com/api/v10/channels/{}/messages?limit=100".format(
                    channel_id
                )
                if before_id:
                    url += "&before={}".format(before_id)

                req = urllib.request.Request(
                    url,
                    headers = {
                        "Authorization" : "Bot " + _REVIEW_BOT_TOKEN,
                        "User-Agent"    : "GDWLReviewBot/1.0",
                    },
                    method = "GET",
                )
                try:
                    with urllib.request.urlopen(req, timeout=15, context=ssl_ctx) as resp:
                        messages = json.loads(resp.read().decode("utf-8"))
                except urllib.error.HTTPError as http_err:
                    body = http_err.read().decode("utf-8", errors="replace")
                    raise Exception("HTTP {} – {}".format(http_err.code, body))

                if not messages:
                    break

                total_fetched += len(messages)

                for msg in messages:
                    content = msg.get("content", "")
                    brace = content.find("{")
                    if brace != -1:
                        raw = content[brace:]
                        try:
                            entry = json.loads(raw)
                            if ("timestamp" in entry
                                    and "dialogue" in entry
                                    and "rating" in entry):
                                all_parsed.append(entry)
                        except Exception:
                            pass

                ## If we got fewer than 100, we've reached the start of the channel
                if len(messages) < 100:
                    break
                before_id = messages[-1]["id"]

            if not all_parsed:
                renpy.invoke_in_main_thread(
                    _review_set_pull_status,
                    u"error:No review messages found in channel ({} msgs scanned). Run Send Reviews first.".format(total_fetched)
                )
                return

            ## ---- Merge: deduplicate against local entries ------------------
            ## Dedup key: timestamp + reviewer + dialogue (should be unique per review)
            local = _review_load_all()
            existing_keys = set()
            for e in local:
                key = (
                    e.get("timestamp", ""),
                    e.get("reviewer", ""),
                    e.get("dialogue", ""),
                )
                existing_keys.add(key)

            added = 0
            for e in all_parsed:
                key = (
                    e.get("timestamp", ""),
                    e.get("reviewer", ""),
                    e.get("dialogue", ""),
                )
                if key not in existing_keys:
                    local.append(e)
                    existing_keys.add(key)
                    added += 1

            _review_write_all(local)
            renpy.invoke_in_main_thread(
                _review_set_pull_status,
                u"pulled:{} new (found {} total in channel)".format(added, len(all_parsed))
            )

        except Exception as ex:
            renpy.invoke_in_main_thread(_review_set_pull_status, u"error:" + str(ex))

    def _review_pull():
        renpy.invoke_in_main_thread(_review_set_pull_status, u"pulling")
        t = threading.Thread(target=_review_pull_thread)
        t.daemon = True
        t.start()

    def _review_toggle_resolved(idx):
        """Flip the resolved flag for entry at index idx and rewrite the file."""
        entries = _review_load_all()
        if 0 <= idx < len(entries):
            entries[idx]["resolved"] = not entries[idx].get("resolved", False)
            _review_write_all(entries)

    ## -------------------------------------------------------------------------
    ## Multi-select helpers
    ## -------------------------------------------------------------------------

    def _review_toggle_select(sel_set, idx):
        """Toggle idx in the mutable selection set and force a screen redraw."""
        if idx in sel_set:
            sel_set.discard(idx)
        else:
            sel_set.add(idx)
        renpy.restart_interaction()

    def _review_select_all(sel_set, indices):
        """Add all supplied indices to the selection set."""
        for i in indices:
            sel_set.add(i)
        renpy.restart_interaction()

    def _review_deselect_all(sel_set):
        """Clear the selection set."""
        sel_set.clear()
        renpy.restart_interaction()

    def _review_bulk_resolve(indices, resolved, sel_set):
        """Set resolved flag for all selected entries."""
        entries = _review_load_all()
        for i in indices:
            if 0 <= i < len(entries):
                entries[i]["resolved"] = resolved
        _review_write_all(entries)
        sel_set.clear()
        renpy.restart_interaction()

    def _review_bulk_delete(indices, sel_set):
        """Delete all selected entries by original index."""
        entries = _review_load_all()
        keep = [e for i, e in enumerate(entries) if i not in indices]
        _review_write_all(keep)
        sel_set.clear()
        renpy.restart_interaction()

    def _review_filter_sort(entries, f_rating, f_tag, f_reviewer, f_resolved, sort_col, sort_desc, f_priority="all", f_search=""):
        """Return a filtered + sorted list of (original_index, entry) pairs."""
        result = []
        _fq = f_search.strip().lower()
        for i, e in enumerate(entries):
            if f_rating != "all" and e.get("rating", "none") != f_rating:
                continue
            if f_tag != "all" and e.get("tag", "none") != f_tag:
                continue
            if f_priority != "all" and e.get("priority", "none") != f_priority:
                continue
            if f_resolved != "all":
                is_res = bool(e.get("resolved", False))
                if f_resolved == "open" and is_res:
                    continue
                if f_resolved == "resolved" and not is_res:
                    continue
            if f_reviewer.strip():
                if f_reviewer.strip().lower() not in e.get("reviewer", "").lower():
                    continue
            if _fq:
                haystack = u" ".join([
                    e.get("dialogue", ""),
                    e.get("who", ""),
                    e.get("reason", ""),
                    e.get("reviewer", ""),
                ]).lower()
                if _fq not in haystack:
                    continue
            result.append((i, e))
        key_map = {
            "date"     : lambda x: x[1].get("timestamp", ""),
            "rating"   : lambda x: x[1].get("rating", ""),
            "tag"      : lambda x: x[1].get("tag", ""),
            "reviewer" : lambda x: x[1].get("reviewer", ""),
            "file"     : lambda x: x[1].get("file", ""),
            "who"      : lambda x: x[1].get("who", ""),
        }
        keyfn = key_map.get(sort_col, key_map["date"])
        result.sort(key=keyfn, reverse=sort_desc)
        return result

    ## -------------------------------------------------------------------------
    ## Register the overlay screen so it appears on top of all other screens.
    ## -------------------------------------------------------------------------
    config.overlay_screens.append("line_review_overlay")

    ## -------------------------------------------------------------------------
    ## Keyboard shortcut: Ctrl+R toggles the overlay visibility.
    ## -------------------------------------------------------------------------
    config.keymap["line_review_toggle"] = ["ctrl_r"]


## Enable the overlay by default. Set to False to disable for shipped builds.
default persistent.review_mode_enabled = True
## Reviewer name is remembered across sessions so you don't retype it each time.
default persistent.review_default_reviewer = u""
## Send status lives in the store so screens redraw when the thread updates it.
default _review_email_status = u""
## Pull status lives in the store so screens redraw when the pull thread updates it.
default _review_pull_status = u""


################################################################################
## Overlay – the small floating button shown during dialogue
################################################################################

screen line_review_overlay():

    if persistent.testmode and persistent.review_mode_enabled and _history_list:
        frame:
            style "line_review_float_frame"
            xalign 0.99
            yalign 0.97
            padding (8, 6)
            hbox:
                spacing 8
                textbutton "📋 Log":
                    style "line_review_float_btn"
                    action Show("line_review_log")
                textbutton "📝 Review Line":
                    style "line_review_float_btn"
                    action Show("line_review_panel")

    if config.developer or persistent.testmode:
        key "line_review_toggle" action ToggleVariable("persistent.review_mode_enabled")


################################################################################
## Review Panel – write a new review
################################################################################

screen line_review_panel():

    modal True
    zorder 200

    ## Screen-local variables so each input field works independently.
    default rv_rating        = None
    default rv_tag            = None
    default rv_priority       = None
    default rv_reason         = u""
    default rv_reviewer       = persistent.review_default_reviewer
    default rv_active_field   = "reason"  ## which input currently has focus

    python:
        _rv_who  = u""
        _rv_what = u"(No dialogue captured yet)"
        try:
            if _history_list:
                h = _history_list[-1]
                _rv_who  = h.who  if h.who  else u""
                _rv_what = h.what if h.what else u"(empty)"
        except Exception:
            pass

    add "#000c"

    frame:
        style "line_review_panel_frame"
        xalign 0.5
        yalign 0.45
        xmaximum 800
        padding (28, 24)

        vbox:
            spacing 14

            ## Header
            hbox:
                xfill True
                text "📝 Line Review" style "line_review_heading"
                textbutton "✕":
                    style "line_review_close_btn"
                    xalign 1.0
                    action Hide("line_review_panel")

            ## Dialogue being reviewed
            frame:
                style "line_review_quote_frame"
                xfill True
                padding (12, 10)
                vbox:
                    spacing 4
                    if _rv_who:
                        text "[_rv_who]" style "line_review_who"
                    text "[_rv_what]" style "line_review_what"

            ## Rating
            hbox:
                spacing 10
                yalign 0.5
                text "Rating:" style "line_review_label"
                textbutton "👍 Thumbs Up":
                    style "line_review_tag_btn"
                    background ("#2a7" if rv_rating == "up" else "#383838")
                    action SetScreenVariable("rv_rating", "up")
                textbutton "👎 Thumbs Down":
                    style "line_review_tag_btn"
                    background ("#a33" if rv_rating == "down" else "#383838")
                    action SetScreenVariable("rv_rating", "down")
                if rv_rating is not None:
                    textbutton "✕ Clear":
                        style "line_review_tag_btn"
                        background "#383838"
                        action SetScreenVariable("rv_rating", None)

            ## Tag
            hbox:
                spacing 10
                yalign 0.5
                text "Tag:" style "line_review_label"
                textbutton "✏ Rewrite":
                    style "line_review_tag_btn"
                    background ("#447" if rv_tag == "rewrite" else "#383838")
                    action SetScreenVariable("rv_tag", "rewrite")
                textbutton "✔ Keep":
                    style "line_review_tag_btn"
                    background ("#447" if rv_tag == "keep" else "#383838")
                    action SetScreenVariable("rv_tag", "keep")
                textbutton "💬 Feedback":
                    style "line_review_tag_btn"
                    background ("#447" if rv_tag == "feedback" else "#383838")
                    action SetScreenVariable("rv_tag", "feedback")
                textbutton "❓ Question":
                    style "line_review_tag_btn"
                    background ("#447" if rv_tag == "question" else "#383838")
                    action SetScreenVariable("rv_tag", "question")

            ## Priority
            hbox:
                spacing 10
                yalign 0.5
                text "Priority:" style "line_review_label"
                textbutton "🟢 Low":
                    style "line_review_tag_btn"
                    background ("#1a4a1a" if rv_priority == "low" else "#383838")
                    action SetScreenVariable("rv_priority", "low")
                textbutton "🟡 Medium":
                    style "line_review_tag_btn"
                    background ("#4a4a1a" if rv_priority == "medium" else "#383838")
                    action SetScreenVariable("rv_priority", "medium")
                textbutton "🔴 High":
                    style "line_review_tag_btn"
                    background ("#4a1a1a" if rv_priority == "high" else "#383838")
                    action SetScreenVariable("rv_priority", "high")
                if rv_priority is not None:
                    textbutton "✕ Clear":
                        style "line_review_tag_btn"
                        background "#383838"
                        action SetScreenVariable("rv_priority", None)

            ## Notes
            vbox:
                spacing 4
                text "Notes / Reason:" style "line_review_label"
                frame:
                    style "line_review_input_frame"
                    xfill True
                    ## Only render the active input; inactive shows a click-to-edit button.
                    if rv_active_field == "reason":
                        input:
                            style "line_review_input"
                            value ScreenVariableInputValue("rv_reason")
                            length 400
                    else:
                        textbutton (rv_reason if rv_reason else "(click to edit)"):
                            style "line_review_input_btn"
                            action SetScreenVariable("rv_active_field", "reason")

            ## Reviewer name
            hbox:
                spacing 10
                yalign 0.5
                text "Your name (optional):" style "line_review_label"
                frame:
                    style "line_review_input_frame"
                    xsize 260
                    if rv_active_field == "reviewer":
                        input:
                            style "line_review_input"
                            value ScreenVariableInputValue("rv_reviewer")
                            length 60
                    else:
                        textbutton (rv_reviewer if rv_reviewer else "(click to set name)"):
                            style "line_review_input_btn"
                            action SetScreenVariable("rv_active_field", "reviewer")

            ## Submit / Cancel
            hbox:
                spacing 14
                xalign 1.0

                textbutton "Submit":
                    style "line_review_submit_btn"
                    sensitive (rv_rating is not None or rv_tag is not None or bool(rv_reason.strip()))
                    action [
                        SetVariable("persistent.review_default_reviewer", rv_reviewer),
                        Function(_review_do_submit, rv_rating, rv_tag, rv_reason, rv_reviewer, rv_priority),
                        Hide("line_review_panel"),
                    ]

                textbutton "Cancel":
                    style "line_review_cancel_btn"
                    action Hide("line_review_panel")


################################################################################
## Review Log – browse, filter and sort all saved reviews
################################################################################

screen line_review_log():

    modal True
    zorder 200

    default log_f_rating   = "all"
    default log_f_tag      = "all"
    default log_f_priority = "all"
    default log_f_resolved = "all"
    default log_f_reviewer = u""
    default log_f_search   = u""
    default log_sort       = "date"
    default log_sort_desc  = True
    default log_selected        = set()
    default log_confirm_delete  = False

    add "#000e"

    frame:
        style "line_review_panel_frame"
        xalign 0.5
        yalign 0.5
        xsize 1060
        ysize 840
        padding (24, 20)

        vbox:
            spacing 10

            ## Header
            hbox:
                xfill True
                yalign 0.5
                text "📋 Review Log" style "line_review_heading"

                ## Send & Pull buttons + statuses (right-aligned before close)
                hbox:
                    xalign 1.0
                    yalign 0.5
                    spacing 12

                    python:
                        _log_err  = _review_email_status
                        _pull_err = _review_pull_status

                    ## ---- Send status ----------------------------------------
                    if _review_email_status == "sending":
                        text "⏳ Sending…" style "line_review_filter_label"
                    elif _review_email_status == "sent":
                        text "✅ Sent!" style "line_review_success_msg"
                    elif _review_email_status.startswith("error:"):
                        text "❌ [_log_err]" style "line_review_error_msg"

                    textbutton "📧 Send Reviews":
                        style "line_review_send_btn"
                        sensitive (_review_email_status != "sending")
                        action Function(_review_send_email)

                    ## ---- Pull status ----------------------------------------
                    if _review_pull_status == "pulling":
                        text "⏳ Pulling…" style "line_review_filter_label"
                    elif _review_pull_status.startswith("pulled:"):
                        python:
                            _pulled_n = _review_pull_status.split(":", 1)[1]
                        text "✅ [_pulled_n]" style "line_review_success_msg"
                    elif _review_pull_status.startswith("error:"):
                        text "❌ [_pull_err]" style "line_review_error_msg"

                    textbutton "📥 Pull Reviews":
                        style "line_review_send_btn"
                        sensitive (_review_pull_status != "pulling")
                        action Function(_review_pull)

                    textbutton "✕":
                        style "line_review_close_btn"
                        xalign 1.0
                        action Hide("line_review_log")

            ## Filter panel
            frame:
                style "line_review_quote_frame"
                xfill True
                padding (10, 10)
                vbox:
                    spacing 8

                    ## Rating
                    hbox:
                        spacing 6
                        yalign 0.5
                        text "Rating:" style "line_review_filter_label"
                        textbutton "All":
                            style "line_review_filter_btn"
                            background ("#556" if log_f_rating == "all" else "#303030")
                            action SetScreenVariable("log_f_rating", "all")
                        textbutton "👍":
                            style "line_review_filter_btn"
                            background ("#2a7" if log_f_rating == "up" else "#303030")
                            action SetScreenVariable("log_f_rating", "up")
                        textbutton "👎":
                            style "line_review_filter_btn"
                            background ("#a33" if log_f_rating == "down" else "#303030")
                            action SetScreenVariable("log_f_rating", "down")
                        textbutton "Unrated":
                            style "line_review_filter_btn"
                            background ("#556" if log_f_rating == "none" else "#303030")
                            action SetScreenVariable("log_f_rating", "none")

                    ## Tag
                    hbox:
                        spacing 6
                        yalign 0.5
                        text "Tag:" style "line_review_filter_label"
                        textbutton "All":
                            style "line_review_filter_btn"
                            background ("#556" if log_f_tag == "all" else "#303030")
                            action SetScreenVariable("log_f_tag", "all")
                        textbutton "✏ Rewrite":
                            style "line_review_filter_btn"
                            background ("#447" if log_f_tag == "rewrite" else "#303030")
                            action SetScreenVariable("log_f_tag", "rewrite")
                        textbutton "✔ Keep":
                            style "line_review_filter_btn"
                            background ("#447" if log_f_tag == "keep" else "#303030")
                            action SetScreenVariable("log_f_tag", "keep")
                        textbutton "💬 Feedback":
                            style "line_review_filter_btn"
                            background ("#447" if log_f_tag == "feedback" else "#303030")
                            action SetScreenVariable("log_f_tag", "feedback")
                        textbutton "❓ Question":
                            style "line_review_filter_btn"
                            background ("#447" if log_f_tag == "question" else "#303030")
                            action SetScreenVariable("log_f_tag", "question")
                        textbutton "Untagged":
                            style "line_review_filter_btn"
                            background ("#556" if log_f_tag == "none" else "#303030")
                            action SetScreenVariable("log_f_tag", "none")

                    ## Priority
                    hbox:
                        spacing 6
                        yalign 0.5
                        text "Priority:" style "line_review_filter_label"
                        textbutton "All":
                            style "line_review_filter_btn"
                            background ("#556" if log_f_priority == "all" else "#303030")
                            action SetScreenVariable("log_f_priority", "all")
                        textbutton "🟢 Low":
                            style "line_review_filter_btn"
                            background ("#1a4a1a" if log_f_priority == "low" else "#303030")
                            action SetScreenVariable("log_f_priority", "low")
                        textbutton "🟡 Medium":
                            style "line_review_filter_btn"
                            background ("#4a4a1a" if log_f_priority == "medium" else "#303030")
                            action SetScreenVariable("log_f_priority", "medium")
                        textbutton "🔴 High":
                            style "line_review_filter_btn"
                            background ("#4a1a1a" if log_f_priority == "high" else "#303030")
                            action SetScreenVariable("log_f_priority", "high")
                        textbutton "None set":
                            style "line_review_filter_btn"
                            background ("#556" if log_f_priority == "none" else "#303030")
                            action SetScreenVariable("log_f_priority", "none")

                    ## Status + Reviewer
                    hbox:
                        spacing 16
                        yalign 0.5
                        hbox:
                            spacing 6
                            yalign 0.5
                            text "Status:" style "line_review_filter_label"
                            textbutton "All":
                                style "line_review_filter_btn"
                                background ("#556" if log_f_resolved == "all" else "#303030")
                                action SetScreenVariable("log_f_resolved", "all")
                            textbutton "⬜ Open":
                                style "line_review_filter_btn"
                                background ("#556" if log_f_resolved == "open" else "#303030")
                                action SetScreenVariable("log_f_resolved", "open")
                            textbutton "✅ Resolved":
                                style "line_review_filter_btn"
                                background ("#556" if log_f_resolved == "resolved" else "#303030")
                                action SetScreenVariable("log_f_resolved", "resolved")
                        hbox:
                            spacing 6
                            yalign 0.5
                            text "Search:" style "line_review_filter_label"
                            frame:
                                style "line_review_input_frame"
                                xsize 300
                                input:
                                    style "line_review_input"
                                    value ScreenVariableInputValue("log_f_search")
                                    length 200
                            if log_f_search:
                                textbutton "✕":
                                    style "line_review_filter_btn"
                                    background "#444"
                                    action SetScreenVariable("log_f_search", u"")

                    ## Sort
                    hbox:
                        spacing 6
                        yalign 0.5
                        text "Sort:" style "line_review_filter_label"
                        textbutton "Date":
                            style "line_review_filter_btn"
                            background ("#668" if log_sort == "date" else "#303030")
                            action SetScreenVariable("log_sort", "date")
                        textbutton "Rating":
                            style "line_review_filter_btn"
                            background ("#668" if log_sort == "rating" else "#303030")
                            action SetScreenVariable("log_sort", "rating")
                        textbutton "Tag":
                            style "line_review_filter_btn"
                            background ("#668" if log_sort == "tag" else "#303030")
                            action SetScreenVariable("log_sort", "tag")
                        textbutton "Reviewer":
                            style "line_review_filter_btn"
                            background ("#668" if log_sort == "reviewer" else "#303030")
                            action SetScreenVariable("log_sort", "reviewer")
                        textbutton "File":
                            style "line_review_filter_btn"
                            background ("#668" if log_sort == "file" else "#303030")
                            action SetScreenVariable("log_sort", "file")
                        textbutton "Speaker":
                            style "line_review_filter_btn"
                            background ("#668" if log_sort == "who" else "#303030")
                            action SetScreenVariable("log_sort", "who")
                        textbutton ("↓ Desc" if log_sort_desc else "↑ Asc"):
                            style "line_review_filter_btn"
                            background "#445"
                            action ToggleScreenVariable("log_sort_desc")

            ## Entry count + selection controls
            python:
                _log_all   = _review_load_all()
                _log_shown = _review_filter_sort(
                    _log_all,
                    log_f_rating, log_f_tag, log_f_reviewer,
                    log_f_resolved, log_sort, log_sort_desc, log_f_priority,
                    log_f_search
                )
                _shown_indices = [i for i, _ in _log_shown]

            hbox:
                xfill True
                yalign 0.5
                spacing 10

                text "Showing [len(_log_shown)] of [len(_log_all)] reviews" style "line_review_filter_label"

                if log_selected:
                    text "· [len(log_selected)] selected" style "line_review_filter_label"

                textbutton "Select all shown":
                    style "line_review_filter_btn"
                    background "#333"
                    action [
                        Function(_review_select_all, log_selected, _shown_indices),
                        SetScreenVariable("log_confirm_delete", False),
                    ]

                if log_selected:
                    textbutton "Deselect all":
                        style "line_review_filter_btn"
                        background "#333"
                        action [
                            Function(_review_deselect_all, log_selected),
                            SetScreenVariable("log_confirm_delete", False),
                        ]

            ## Bulk action bar – only visible when something is selected
            if log_selected:
                frame:
                    background "#1e2840"
                    xfill True
                    padding (12, 8)
                    hbox:
                        spacing 10
                        yalign 0.5

                        text "Actions for [len(log_selected)] selected:" style "line_review_filter_label"

                        textbutton "✅ Resolve":
                            style "line_review_tag_btn"
                            background "#1a4a1a"
                            action [
                                Function(_review_bulk_resolve, list(log_selected), True, log_selected),
                                SetScreenVariable("log_confirm_delete", False),
                            ]

                        textbutton "⬜ Unresolve":
                            style "line_review_tag_btn"
                            background "#3a3a3a"
                            action [
                                Function(_review_bulk_resolve, list(log_selected), False, log_selected),
                                SetScreenVariable("log_confirm_delete", False),
                            ]

                        if not log_confirm_delete:
                            textbutton "🗑 Delete":
                                style "line_review_tag_btn"
                                background "#5a1a1a"
                                action SetScreenVariable("log_confirm_delete", True)
                        else:
                            text "Delete [len(log_selected)] entries?" style "line_review_filter_label"

                            textbutton "Yes, delete":
                                style "line_review_tag_btn"
                                background "#8a1a1a"
                                action [
                                    Function(_review_bulk_delete, list(log_selected), log_selected),
                                    SetScreenVariable("log_confirm_delete", False),
                                ]

                            textbutton "Cancel":
                                style "line_review_tag_btn"
                                background "#3a3a3a"
                                action SetScreenVariable("log_confirm_delete", False)

            ## Scrollable entries
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xfill True
                ysize 420

                vbox:
                    spacing 8
                    xfill True

                    if not _log_shown:
                        text "No reviews match the current filters." style "line_review_label"

                    for _log_idx, _log_e in _log_shown:
                        python:
                            _log_res    = bool(_log_e.get("resolved", False))
                            _log_rat    = _log_e.get("rating", "none")
                            _log_tag_v  = _log_e.get("tag", "none")
                            _log_pri_v  = _log_e.get("priority", "none")
                            _log_rat_ic = "👍" if _log_rat == "up" else ("👎" if _log_rat == "down" else "–")
                            _log_tag_ic = {"rewrite":"✏","keep":"✔","feedback":"💬","question":"❓"}.get(_log_tag_v, "–")
                            _log_pri_ic = {"low":"🟢","medium":"🟡","high":"🔴"}.get(_log_pri_v, "–")
                            _log_res_ic = "✅" if _log_res else "⬜"
                            _log_sel    = (_log_idx in log_selected)
                            _log_bg     = "#1a2a4a" if _log_sel else ("#1e2a1e" if _log_res else "#252525")

                        frame:
                            background _log_bg
                            xfill True
                            padding (12, 10)

                            hbox:
                                xfill True
                                spacing 10

                                ## Selection checkbox
                                textbutton ("☑" if _log_sel else "☐"):
                                    style "line_review_tag_btn"
                                    yalign 0.5
                                    background ("#27a" if _log_sel else "#2e2e2e")
                                    action [
                                        Function(_review_toggle_select, log_selected, _log_idx),
                                        SetScreenVariable("log_confirm_delete", False),
                                    ]

                                vbox:
                                    xfill True
                                    spacing 4

                                    hbox:
                                        spacing 8
                                        if _log_e.get("who", ""):
                                            text ("[_log_e['who']]") style "line_review_who"
                                        text ("[_log_e.get('dialogue','')]") style "line_review_log_dialogue"

                                    hbox:
                                        spacing 16
                                        text ("[_log_rat_ic] [_log_tag_ic] [_log_pri_ic]") style "line_review_log_meta"
                                        text ("v[_log_e.get('game_version','?')]") style "line_review_log_meta"
                                        text ("[_log_e.get('timestamp','')]") style "line_review_log_meta"
                                        text ("by [_log_e.get('reviewer','?')]") style "line_review_log_meta"
                                        text ("[_log_e.get('file','')]:[_log_e.get('line','')]") style "line_review_log_meta"

                                    if _log_e.get("reason", ""):
                                        text ("\"[_log_e.get('reason','')]\"") style "line_review_log_reason"

                                vbox:
                                    yalign 0.5
                                    textbutton "[_log_res_ic]":
                                        style "line_review_tag_btn"
                                        background ("#1a4a1a" if _log_res else "#3a3a3a")
                                        action Function(_review_toggle_resolved, _log_idx)


################################################################################
## Styles
################################################################################

style line_review_float_frame:
    background "#111b"
    xpadding 8
    ypadding 6

style line_review_float_btn is button:
    xpadding 10
    ypadding 5

style line_review_float_btn_text is button_text:
    size 18
    color "#ddd"
    hover_color "#fff"

style line_review_panel_frame:
    background "#1a1a1aee"
    xpadding 28
    ypadding 24

style line_review_heading is gui_text:
    size 26
    bold True
    color "#eee"

style line_review_close_btn is button:
    color "#aaa"
    hover_color "#fff"
    size 22

style line_review_quote_frame:
    background "#2a2a2a"
    xpadding 12
    ypadding 10

style line_review_who is gui_text:
    size 18
    color "#adf"
    bold True

style line_review_what is gui_text:
    size 20
    color "#ddd"

style line_review_label is gui_text:
    size 19
    color "#bbb"
    yalign 0.5

style line_review_tag_btn is button:
    xpadding 12
    ypadding 6

style line_review_tag_btn_text is button_text:
    size 18
    color "#ccc"
    hover_color "#fff"

style line_review_input_frame:
    background "#2e2e2e"
    xpadding 10
    ypadding 6

style line_review_input is input:
    size 19
    color "#eee"

style line_review_input_btn is button:
    xpadding 0
    ypadding 0

style line_review_input_btn_text is button_text:
    size 19
    color "#888"
    hover_color "#ccc"

style line_review_success_msg is gui_text:
    size 18
    color "#6d6"
    yalign 0.5

style line_review_submit_btn is button:
    background "#2a6"
    xpadding 18
    ypadding 8

style line_review_submit_btn_text is button_text:
    size 19
    color "#fff"
    hover_color "#dfd"

style line_review_cancel_btn is button:
    background "#555"
    xpadding 18
    ypadding 8

style line_review_cancel_btn_text is button_text:
    size 19
    color "#ccc"
    hover_color "#fff"

style line_review_filter_label is gui_text:
    size 17
    color "#aaa"
    yalign 0.5

style line_review_filter_btn is button:
    xpadding 10
    ypadding 5

style line_review_filter_btn_text is button_text:
    size 16
    color "#ccc"
    hover_color "#fff"

style line_review_log_dialogue is gui_text:
    size 18
    color "#ddd"

style line_review_log_meta is gui_text:
    size 15
    color "#777"
    yalign 0.5

style line_review_log_reason is gui_text:
    size 17
    color "#999"
    italic True

style line_review_send_btn is button:
    background "#27a"
    xpadding 14
    ypadding 6

style line_review_send_btn_text is button_text:
    size 18
    color "#fff"
    hover_color "#aef"

style line_review_error_msg is gui_text:
    size 17
    color "#d55"
    yalign 0.5
