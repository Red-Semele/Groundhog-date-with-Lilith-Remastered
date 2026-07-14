################################################################################
## Font Settings
## Handles persistent font choice and runtime font switching.
################################################################################

## Default font choice. "DejaVuSans.ttf" is the built-in Ren'Py default.
## "Pacifico-Regular.ttf" is the custom Pacifico font.
default persistent.font_choice = "DejaVuSans.ttf"

## Text size offset from the default sizes. 0 = no change.
default persistent.text_size_offset = 0

## Extra space (px) between each character in dialogue. 0 = default Ren'Py spacing.
default persistent.letter_spacing = 0

## Textbox background opacity as a percentage (20-100). 100 = fully opaque.
default persistent.textbox_opacity = 100

## Text outline style: "none", "outline", or "shadow".
default persistent.text_outline = "none"

## Whether to use the compact grid layout for 3–4 choices.
## When off, the classic stacked layout is used. 5+ choices always scroll.
default persistent.grid_choices = True

init python:
    FONT_DEJAVU           = "DejaVuSans.ttf"
    FONT_PACIFICO         = "defaultFonts/Pacifico-Regular.ttf"
    FONT_INDIEFLOWER      = "defaultFonts/IndieFlower-Regular.ttf"
    FONT_SHADOWSINTOLIGHT = "defaultFonts/ShadowsIntoLight-Regular.ttf"
    ## Scan game/custom_fonts/ for any .ttf/.otf files the player dropped in.
    ## Populates a list of (display_name, gamedir-relative path) tuples.
    ## This runs once at startup; players must restart for new fonts to appear.
    import os as _os
    _custom_dir = _os.path.join(config.gamedir, "custom_fonts")
    CUSTOM_FONTS = []
    if _os.path.isdir(_custom_dir):
        for _fname in sorted(_os.listdir(_custom_dir)):
            if _fname.lower().endswith((".ttf", ".otf")):
                _display = _os.path.splitext(_fname)[0].replace("-", " ").replace("_", " ")
                CUSTOM_FONTS.append((_display, "custom_fonts/" + _fname))

    ## Base text sizes matching gui.rpy defaults.
    ## The slider shifts all of them by the same offset so proportions stay intact.
    _TEXT_BASE           = 33
    _NAME_BASE           = 45
    _INTERFACE_BASE      = 33
    _LABEL_BASE          = 36
    _NOTIFY_BASE         = 24
    TEXT_SIZE_MIN_OFFSET = -10   # how much smaller the player can go
    TEXT_SIZE_MAX_OFFSET =  20   # how much larger the player can go

    LETTER_SPACING_MIN = 0
    LETTER_SPACING_MAX = 20

    ## Maximum words shown on a grid choice button before truncating.
    ## Full text appears in the tooltip notecard on hover.
    CHOICE_MAX_WORDS = 8

    def truncate_choice(text, max_words=None):
        if max_words is None:
            max_words = CHOICE_MAX_WORDS
        words = text.split()
        if len(words) <= max_words:
            return text
        return u" ".join(words[:max_words]) + u"\u2026"

    def _measure_text_px(s, style_name):
        """Return the rendered pixel width of string s using the named style."""
        import renpy.text.text as _rtt
        t = _rtt.Text(s, style=style_name)
        surf = renpy.display.render.render(t, 99999, 999, 0, 0)
        return surf.get_size()[0]

    def truncate_to_width(text, max_px, style_name="inline_choice_button_text"):
        """
        Truncate text so it fits within max_px pixels when rendered with the
        given style.  Uses Ren'Py's own font rendering, so it's accurate for
        any font or size.  Binary-searches for the cutoff to keep it fast.
        """
        if _measure_text_px(u"\u00b7 " + text, style_name) <= max_px:
            return text
        # Binary-search the character cutoff.
        lo, hi = 1, len(text) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if _measure_text_px(u"\u00b7 " + text[:mid] + u"\u2026", style_name) <= max_px:
                lo = mid
            else:
                hi = mid - 1
        # Snap back to the last word boundary.
        cut = text[:lo].rsplit(None, 1)[0] if u" " in text[:lo] else text[:lo]
        return cut + u"\u2026"

    def apply_text_size(offset):
        offset = max(TEXT_SIZE_MIN_OFFSET, min(TEXT_SIZE_MAX_OFFSET, int(offset)))
        persistent.text_size_offset = offset
        # gui.rpy defines now read persistent.text_size_offset directly,
        # so gui.rebuild() re-evaluates them with the correct value
        # instead of resetting back to the hardcoded base numbers.
        gui.rebuild()

    class TextSizeValue(BarValue):
        """Slider bar for text size offset.

        Caches exactly one ui.adjustment so Ren'Py never recreates it mid-drag.
        gui.rebuild() is intentionally NOT called here; it fires once via the
        'on hide / on replaced' hooks on the preferences screen.
        """
        def __init__(self):
            self._adj = None

        def _changed(self, value):
            offset = int(round(value)) + TEXT_SIZE_MIN_OFFSET
            persistent.text_size_offset = offset
            # No gui.rebuild() here — that would tear down the screen and
            # kill the active drag gesture every single step.
            renpy.restart_interaction()

        def get_adjustment(self):
            if self._adj is None:
                offset    = getattr(persistent, "text_size_offset", 0)
                bar_range = float(TEXT_SIZE_MAX_OFFSET - TEXT_SIZE_MIN_OFFSET)
                current   = float(offset - TEXT_SIZE_MIN_OFFSET)
                self._adj = ui.adjustment(
                    value=current,
                    range=bar_range,
                    adjustable=True,
                    changed=self._changed,
                    step=1.0,
                )
            return self._adj

        def get_style(self):
            return "slider", "vslider"

    ## Convenience wrapper called once when the preferences screen closes.
    ## This is where gui.rebuild() runs — NOT during the drag.
    def apply_text_size_current():
        apply_text_size(getattr(persistent, "text_size_offset", 0))

    class LetterSpacingValue(BarValue):
        """Slider bar for letter spacing. Same caching pattern as TextSizeValue."""
        def __init__(self):
            self._adj = None

        def _changed(self, value):
            spacing = int(round(value))
            persistent.letter_spacing = spacing
            renpy.restart_interaction()

        def get_adjustment(self):
            if self._adj is None:
                spacing   = getattr(persistent, "letter_spacing", 0)
                bar_range = float(LETTER_SPACING_MAX - LETTER_SPACING_MIN)
                current   = float(spacing - LETTER_SPACING_MIN)
                self._adj = ui.adjustment(
                    value=current,
                    range=bar_range,
                    adjustable=True,
                    changed=self._changed,
                    step=1.0,
                )
            return self._adj

        def get_style(self):
            return "slider", "vslider"

    class TextboxOpacityValue(BarValue):
        """Slider for textbox background opacity (20-100%)."""
        def __init__(self):
            self._adj = None

        def _changed(self, value):
            persistent.textbox_opacity = int(round(value)) + 20
            renpy.restart_interaction()

        def get_adjustment(self):
            if self._adj is None:
                opacity   = getattr(persistent, "textbox_opacity", 100)
                self._adj = ui.adjustment(
                    value=float(opacity - 20),
                    range=80.0,
                    adjustable=True,
                    changed=self._changed,
                    step=1.0,
                )
            return self._adj

        def get_style(self):
            return "slider", "vslider"

    class SetTextOutline(Action):
        """Action for the text outline radio buttons."""
        def __init__(self, mode):
            self.mode = mode

        def __call__(self):
            persistent.text_outline = self.mode
            gui.rebuild()
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(persistent, "text_outline", "none") == self.mode

    ## Returns the currently selected font, falling back to DejaVu if unset.
    ## Also falls back if a previously chosen custom font file was removed.
    def current_font():
        f = getattr(persistent, "font_choice", None)
        if not f:
            return FONT_DEJAVU
        ## If it was a custom font, verify the file still exists
        if f.startswith("custom_fonts/"):
            _path = _os.path.join(config.gamedir, f.replace("/", _os.sep))
            if not _os.path.isfile(_path):
                return FONT_DEJAVU
        return f

    ## Applies the given font by updating gui.* variables then rebuilding all styles.
    ## gui.rebuild() is the proper Ren'Py API for runtime style changes.
    def apply_font_to_styles(font):
        gui.text_font            = font
        gui.name_text_font       = font
        gui.interface_text_font  = font
        gui.button_text_font     = font
        gui.choice_button_text_font = font
        gui.rebuild()

    ## Re-apply the saved font choice and text size after loading a save or starting fresh.
    ## Both font and size are now read from persistent inside gui.rpy defines,
    ## so a single gui.rebuild() picks up both.
    def _on_load_apply_font():
        gui.rebuild()

    config.after_load_callbacks.append(_on_load_apply_font)

    ## SetFont: action used by the preferences screen buttons.
    class SetFont(Action):
        def __init__(self, font_name):
            self.font_name = font_name

        def __call__(self):
            persistent.font_choice = self.font_name
            apply_font_to_styles(self.font_name)
            renpy.restart_interaction()

        def get_selected(self):
            return current_font() == self.font_name

## Apply persistent letter spacing via a style block so gui.rebuild() picks it up.
## gui.text_letter_spacing is defined in gui.rpy to read persistent.letter_spacing.
style say_dialogue:
    kerning gui.text_letter_spacing
    outlines gui.text_outlines
