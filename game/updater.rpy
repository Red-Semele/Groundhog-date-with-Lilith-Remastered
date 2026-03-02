## Auto-Update Checker ########################################################
##
## Fetches version.json from GitHub in a background thread and shows a
## notification bar on the main menu when a newer version is available.

init python:
    import json
    import urllib.request

    _UPDATE_VERSION_URL = (
        "https://raw.githubusercontent.com/"
        "Red-Semele/Groundhog-date-with-Lilith-Remastered/"
        "main/version.json"
    )
    ## Base URL for Ren'Py update packages hosted on GitHub Pages.
    ## The workflow publishes updates.json and *.update.bz2 here.
    _UPDATE_URL = (
        "https://red-semele.github.io/"
        "Groundhog-date-with-Lilith-Remastered/updates/"
    )

    _update_available      = False
    _update_latest_version = None
    _update_checked        = False
    _update_check_started  = False

    def _run_update_check():
        global _update_available, _update_latest_version, _update_checked
        try:
            req = urllib.request.urlopen(_UPDATE_VERSION_URL, timeout=8)
            data = req.read().decode("utf-8")
            info = json.loads(data)
            latest = info.get("version", "").strip()
            if latest and latest != config.version:
                _update_latest_version = latest
                _update_available = True
        except Exception:
            pass
        finally:
            _update_checked = True

    def _trigger_update_check():
        """Called once when the main menu is first shown."""
        global _update_check_started
        if not _update_check_started:
            _update_check_started = True
            renpy.invoke_in_thread(_run_update_check)


## Notification bar shown at the top of the main menu when an update is ready.

screen update_notification():

    ## Kick off the background check the first time this screen appears.
    on "show" action Function(_trigger_update_check)

    if _update_checked and _update_available:
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

                text "Update available — v[_update_latest_version]":
                    color "#e0e0ff"
                    yalign 0.5
                    xmaximum 9999

                textbutton "Update Now":
                    yalign 0.5
                    ## Uses Ren'Py's built-in updater: downloads only changed
                    ## files, applies the patch, then restarts the game.
                    action updater.Update(_UPDATE_URL, restart=True)

                textbutton "✕":
                    yalign 0.5
                    action SetVariable("_update_available", False)
