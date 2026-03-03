## Auto-Update Checker ########################################################
##
## Fetches version.json from GitHub in a background thread at startup.
## Results stored in persistent so the screen can read them at any time.

init python:
    import json
    import os
    import ssl
    import datetime
    import urllib.request

    _UPDATE_VERSION_URL = (
        "https://raw.githubusercontent.com/"
        "Red-Semele/Groundhog-date-with-Lilith-Remastered/"
        "main/version.json"
    )
    _UPDATE_URL = (
        "https://red-semele.github.io/"
        "Groundhog-date-with-Lilith-Remastered/updates/"
    )

    ## Unverified SSL context — needed because Ren'Py's bundled Python
    ## doesn't ship with system CA certificates.
    _ssl_ctx = ssl._create_unverified_context()

    _update_log_path = os.path.join(config.basedir, "update_debug.txt")

    def _update_log(msg):
        """Append a timestamped line to update_debug.txt."""
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(_update_log_path, "a", encoding="utf-8") as f:
                f.write(u"[{}] {}\n".format(timestamp, msg))
        except Exception:
            pass

    def _run_update_check():
        _update_log(u"--- Update check started (local version: {}) ---".format(config.version))
        _update_log(u"Fetching: {}".format(_UPDATE_VERSION_URL))
        try:
            req = urllib.request.urlopen(_UPDATE_VERSION_URL, timeout=8, context=_ssl_ctx)
            data = req.read().decode("utf-8")
            _update_log(u"Raw response: {}".format(data.strip()))
            info = json.loads(data)
            latest = info.get("version", "").strip()
            persistent._update_latest_version = latest
            _update_log(u"Latest version: {}  Local version: {}".format(latest, config.version))
            if latest and latest != config.version:
                persistent._update_available = True
                _update_log(u"Update available -> showing notification bar")
            else:
                persistent._update_available = False
                _update_log(u"Already up to date -> no notification")
        except Exception as e:
            persistent._update_error = str(e)
            persistent._update_available = False
            _update_log(u"ERROR during update check: {}".format(e))
        finally:
            persistent._update_checked = True
            _update_log(u"--- Update check complete ---")

    def _start_update_check():
        ## Reset each session so the check always runs fresh.
        persistent._update_available = False
        persistent._update_checked   = False
        persistent._update_latest_version = None
        persistent._update_error = None
        renpy.invoke_in_thread(_run_update_check)

    ## Register the check to run automatically when Ren'Py finishes loading.
    config.start_callbacks.append(_start_update_check)


## Notification bar shown at the top of the main menu when an update is ready.

screen update_notification():

    ## Poll persistent every second so the bar appears as soon as thread finishes.
    timer 1.0 repeat True action NullAction()

    if persistent._update_checked and persistent._update_available:
        frame:
            background "#1a1a2ecc"
            xfill True
            ysize 46
            xalign 0.5
            yalign 0.0
            padding (20, 0)

            hbox:
                xfill True
                yalign 0.5
                spacing 16

                text "Update available — v[persistent._update_latest_version]":
                    color "#e0e0ff"
                    yalign 0.5
                    xmaximum 9999

                textbutton "Update Now":
                    yalign 0.5
                    action updater.Update(_UPDATE_URL, restart=True)

                textbutton "✕":
                    yalign 0.5
                    action [SetField(persistent, "_update_available", False), NullAction()]
