# --- Cinematic Textbox Shift Toggle ---
default cinematic_textbox_shift = True
default cinematic_textbox_shift_last_size = 0
default cinematic_textbox_shift_prev_shift = 0
default cinematic_bars_state = {"sides": [], "size": 0, "target_size": 0, "animate": False, "duration": 0.3, "hide_duration": 0.3, "retracting": False, "retract_from": 0, "retract_pending": False, "curve": None, "block_dismiss_until": 0.0}
default persistent.menu_choice_history = {}
default persistent.menu_choice_history_display = {}
default persistent.menu_choice_history_current = {}
default persistent.menu_choice_history_loop = {}
default persistent.inline_choices = False
default persistent.inline_choice_grow = True
default persistent.number_keys = False
default persistent.auto_pick_underlined_choice = False
screen cinematic_bars():
    zorder 200
    $ size = cinematic_bars_state["target_size"]
    $ duration = cinematic_bars_state["duration"] if cinematic_bars_state["animate"] else 0.0
    if "top" in cinematic_bars_state["sides"] and size > 0:
        fixed:
            xysize (config.screen_width, size)
            align (0, 0)
            at bar_grow_ysize(duration, size)
            add Solid("#000") xysize (config.screen_width, size)
    if "bottom" in cinematic_bars_state["sides"]:
        fixed:
            xysize (config.screen_width, max(size, 1))
            at bar_grow_ysize_bottom(duration, size)
            add Solid("#000") xysize (config.screen_width, max(size, 1))
            # Always add a 1px black line at the very bottom to cover any gap
            add Solid("#000") xysize (config.screen_width, 1) ypos config.screen_height - 1
    if "left" in cinematic_bars_state["sides"] and size > 0:
        fixed:
            xysize (size, config.screen_height)
            align (0, 0)
            at bar_grow_xsize(duration, size)
            add Solid("#000") xysize (size, config.screen_height)
    if "right" in cinematic_bars_state["sides"]:
        fixed:
            xysize (max(size, 1), config.screen_height)
            at bar_grow_xsize_right(duration, size)
            add Solid("#000") xysize (max(size, 1), config.screen_height)
            # Always add a 1px black line at the very right to cover any gap
            add Solid("#000") xysize (1, config.screen_height) xpos config.screen_width - 1

# Animate ysize for vertical bars

# Top bar grows down from the top
transform bar_grow_ysize(duration, target):
    on show:
        ysize 0
        cinematic_ease duration ysize target
    on hide:
        cinematic_ease cinematic_bars_state.get("hide_duration", duration) ysize 0
    ysize target

# Bottom bar grows up from the bottom (by animating ysize and ypos)
transform bar_grow_ysize_bottom(duration, target):
    on show:
        ysize 0
        ypos config.screen_height
        cinematic_ease duration ysize target+1 ypos config.screen_height - target
    on hide:
        cinematic_ease cinematic_bars_state.get("hide_duration", duration) ysize 0 ypos config.screen_height
    ysize target+1
    ypos config.screen_height - target


# Animate xsize for left bar (grows from left)
transform bar_grow_xsize(duration, target):
    on show:
        xsize 0
        cinematic_ease duration xsize target
    on hide:
        cinematic_ease cinematic_bars_state.get("hide_duration", duration) xsize 0
    xsize target

# Animate xsize and xpos for right bar (grows from right, +1px to prevent gap)
transform bar_grow_xsize_right(duration, target):
    on show:
        xsize 1
        xpos config.screen_width
        cinematic_ease duration xsize target+1 xpos config.screen_width - target
    on hide:
        cinematic_ease cinematic_bars_state.get("hide_duration", duration) xsize 1 xpos config.screen_width
    xsize target+1
    xpos config.screen_width - target


init python:
    import time as _cinematic_time

    def show_cinematic_bars(sides, size, animate=True, duration=0.3, curve=None):
        """
        Shows the cinematic bars, optionally animating them in.
        """
        global cinematic_bars_state, cinematic_textbox_shift_prev_shift, cinematic_textbox_shift_last_size
        cinematic_bars_state["sides"] = sides
        cinematic_bars_state["size"] = size
        cinematic_bars_state["target_size"] = size
        cinematic_bars_state["animate"] = animate
        cinematic_bars_state["duration"] = duration if animate else 0.0
        cinematic_bars_state["curve"] = curve
        cinematic_bars_state["retracting"] = False
        cinematic_bars_state["retract_pending"] = False
        cinematic_bars_state["retract_from"] = 0
        if animate and duration > 0:
            cinematic_bars_state["block_dismiss_until"] = _cinematic_time.time() + duration
        if cinematic_textbox_shift and "bottom" in sides and size > 0:
            cinematic_textbox_shift_prev_shift = cinematic_textbox_shift_last_size
        else:
            cinematic_textbox_shift_prev_shift = 0
        cinematic_textbox_shift_last_size = size
        renpy.show_screen("cinematic_bars")

    def hide_cinematic_bars(animate=True, duration=0.3, curve=None):
        """
        Hides the cinematic bars (animates out if animate equals True).
        curve: same options as show_cinematic_bars (None/"linear", "ease", etc.)
        """
        global cinematic_bars_state, cinematic_textbox_shift_prev_shift, cinematic_textbox_shift_last_size
        hide_dur = duration if animate else 0.0
        cinematic_bars_state["target_size"] = 0
        cinematic_bars_state["animate"] = animate
        cinematic_bars_state["duration"] = hide_dur
        cinematic_bars_state["hide_duration"] = hide_dur
        cinematic_bars_state["curve"] = curve
        if animate and hide_dur > 0:
            cinematic_bars_state["block_dismiss_until"] = _cinematic_time.time() + hide_dur
        if cinematic_textbox_shift and "bottom" in cinematic_bars_state["sides"]:
            cinematic_bars_state["retracting"] = True
            cinematic_bars_state["retract_pending"] = True
            cinematic_bars_state["retract_from"] = cinematic_textbox_shift_last_size
        cinematic_textbox_shift_last_size = 0
        renpy.hide_screen("cinematic_bars")

    def reset_to_default_family_terms():
        for npc_var, name_d, nick_d in _NPC_DEFAULTS:
            setattr(persistent, npc_var, name_d)
            setattr(persistent, npc_var + "_nickname", nick_d)
            setattr(persistent, npc_var + "_family_terms", dict(_FAMILY_DEFAULTS.get(npc_var, {})))
            setattr(persistent, npc_var + "_pronouns", dict(_PRONOUN_DEFAULTS.get(npc_var, {})))
        updateFamilyTerms()
        updatePronouns()

    def updateFamilyTerms():
        _prefix_map = [
            ("date",       "date"),
            ("date_sis",   "sis"),
            ("date_dad",   "dad"),
            ("date_mom",   "mom"),
            ("date_ghost", "ghost"),
        ]
        for npc_var, prefix in _prefix_map:
            defaults = _FAMILY_DEFAULTS.get(npc_var, {})
            f = _get_family_dict(npc_var)
            for form in defaults.keys():
                setattr(store, prefix + "_" + form, f.get(form, defaults.get(form, "")))
            # Also update names and nicknames in store for UI
            name = getattr(persistent, npc_var, "")
            nickname = getattr(persistent, npc_var + "_nickname", "")
            setattr(store, prefix + "_name", name)
            setattr(store, prefix + "_nickname", nickname)
        sync_family_term_shorthands()

    def sync_family_term_shorthands():
        # Safely assign all family term shorthands with fallback defaults
        # Date
        store.date_sibShort = persistent.date_family_terms.get("sibShort", "sis")
        store.date_sib = persistent.date_family_terms.get("sib", "sister")
        store.date_child = persistent.date_family_terms.get("child", "daughter")
        # Sis
        store.sis_sibShort = persistent.date_sis_family_terms.get("sibShort", "sis")
        store.sis_sib = persistent.date_sis_family_terms.get("sib", "sister")
        store.sis_child = persistent.date_sis_family_terms.get("child", "daughter")
        # Dad
        store.dad_parShort = persistent.date_dad_family_terms.get("parShort", "dad")
        store.dad_par = persistent.date_dad_family_terms.get("par", "father")
        # Mom
        store.mom_parShort = persistent.date_mom_family_terms.get("parShort", "mom")
        store.mom_par = persistent.date_mom_family_terms.get("par", "mother")
        # Ghost
        store.ghost_sibShort = persistent.date_ghost_family_terms.get("sibShort", "bro")
        store.ghost_sib = persistent.date_ghost_family_terms.get("sib", "brother")
        store.ghost_child = persistent.date_ghost_family_terms.get("child", "son")

    def sync_pronoun_shorthands():
        # Assign all pronoun shorthands (excluding verbs except vs)
        _prefix_map = [
            ("date",       "date"),
            ("date_sis",   "sis"),
            ("date_dad",   "dad"),
            ("date_mom",   "mom"),
            ("date_ghost", "ghost"),
        ]
        for npc_var, prefix in _prefix_map:
            p = _get_pronoun_dict(npc_var)
            for form in ("sub", "obj", "pos", "ref", "pred", "vs"):
                setattr(store, f"{prefix}_{form}", p.get(form, ""))

screen show_family_input_screen(npc_var, term_key, term_label, term_default):
    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            text f"Enter {term_label}:" size 28
            input:
                default _get_family_dict(npc_var).get(term_key, term_default)
                changed (lambda v, nv=npc_var, tk=term_key: set_family_term(nv, tk, v))
            hbox:
                spacing 10
                textbutton "Save" action [Function(updateFamilyTerms), Hide('show_family_input_screen')]
                textbutton "Cancel" action Hide('show_family_input_screen')

screen change_family_terms_menu():
    tag menu
    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        xsize 1150
        ysize 720
        vbox:
            spacing 8
            text "Change Family Terms" size 26 xalign 0.5
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xsize 1110
                ysize 620
                vbox:
                    spacing 10
                    xsize 1090
                    for npc_var, npc_default, _ in _NPC_DEFAULTS:
                        $ _f = _get_family_dict(npc_var)
                        $ _defs = _FAMILY_DEFAULTS.get(npc_var, {})
                        frame:
                            background "#CCCCCC"
                            padding (12, 10)
                            margin (4, 4)
                            xfill True
                            vbox:
                                spacing 6
                                text npc_default size 20
                                for term_key, term_label in _defs.items():
                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text f"{term_key}: {_f.get(term_key, term_label)}" yalign 0.5 size 18
                                        textbutton "Edit" yalign 0.5 action Show("show_family_input_screen", npc_var=npc_var, term_key=term_key, term_label=term_key, term_default=term_label)
            hbox:
                spacing 16
                xalign 0.5
                textbutton "Reset to Defaults" action [Function(reset_all_character_defaults), Function(renpy.restart_interaction)] style "menu_button"
                textbutton "Return" action Return() style "menu_button"
################################################################################
## Initialization
################################################################################

init offset = -1

define _game_menu_screen = "notebook_closed_menu"
define config.auto_load = None


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Solid(gui.hover_color)
    right_bar Solid(gui.hover_muted_color)

style vbar:
    xsize gui.bar_size
    top_bar Solid(gui.hover_color)
    bottom_bar Solid(gui.hover_muted_color)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize 72
    ypadding 0
    unscrollable "hide"
    base_bar Transform(Frame("gui/scrollbar/vertical_idle_bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile), matrixcolor=ColorizeMatrix("#000000", gui.hover_muted_color))
    thumb Transform("gui/scrollbar/vertical_idle_thumb.png", matrixcolor=ColorizeMatrix("#000000", gui.hover_color))
    thumb_offset 36

style slider:
    ysize gui.slider_size
    base_bar Solid(gui.hover_muted_color)
    thumb Solid(gui.hover_color)

style slider_bar is bar:
    left_bar "gui/horizontal bar filling.png"
    right_bar "gui/horizontal bar empty.png"

style vslider:
    xsize gui.slider_size
    base_bar Solid(gui.hover_muted_color)
    thumb Solid(gui.hover_color)


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################






## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what, nametag=None, **kwargs):
    style_prefix "say"

    # Text fills the free space below first; then it climbs into the free space above (never into the torn edge, which ends ~34px below the box top) before the box grows.
    $ _say_text_top_min = 50
    $ _say_text_top_default = gui.dialogue_ypos + 18
    $ _say_cap_box_height = int(config.screen_height * 0.92)
    $ _say_content_height = measure_dialogue_height(what, gui.dialogue_width, gui.text_size)
    $ _say_box_height = min(_say_cap_box_height, max(gui.textbox_height, _say_text_top_min + _say_content_height + 10))
    $ _say_text_top = max(_say_text_top_min, min(_say_text_top_default, _say_box_height - 10 - _say_content_height))



    $ shift = 0
    $ prev_shift = 0
    $ duration = 0.0
    $ animate_shift = False
    if cinematic_textbox_shift and "bottom" in cinematic_bars_state["sides"]:
        if cinematic_bars_state["target_size"] > 0:
            $ shift = cinematic_bars_state["target_size"]
            $ prev_shift = cinematic_textbox_shift_prev_shift
            $ duration = cinematic_bars_state["duration"] if cinematic_bars_state["animate"] else 0.0
            $ animate_shift = (prev_shift != shift and duration > 0.0)
        elif cinematic_bars_state.get("retracting", False):
            $ prev_shift = cinematic_bars_state.get("retract_from", 0)
            $ duration = cinematic_bars_state["duration"]
            $ animate_shift = (prev_shift > 0 and duration > 0.0)

    if what is not None and what != "" and persistent.cheddar and cheddar_state["open"]:
        fixed:
            at (textbox_shift_smooth(prev_shift, shift, duration) if animate_shift else textbox_shift_static(shift))
            use cheddar_tab_piece

    $ _nt = nametag_track(who, what)
    if what is not None and what != "" and who is not None:
        $ _tag_render_w = int(round(202 * menu_notebook_zoom))
        $ _tag_render_h = int(round(63 * menu_notebook_zoom))
        fixed:
            at (textbox_shift_smooth(prev_shift, shift, duration) if animate_shift else textbox_shift_static(shift))
            if _nt["swap"] and _nt["prev"] is not None:
                use nametag_piece(_nt["prev"], nametag_color(_nt["prev"]), _tag_render_w, _tag_render_h, nametag_retract(nametag_shown(_nt["prev"]), nametag_hidden()), False)
                use nametag_piece(who, nametag_color(who, nametag), _tag_render_w, _tag_render_h, nametag_extend(nametag_hidden(), nametag_shown(who), 0.8), True)
            elif _nt["swap"]:
                use nametag_piece(who, nametag_color(who, nametag), _tag_render_w, _tag_render_h, nametag_extend(nametag_hidden(), nametag_shown(who), 0.0), True)
            else:
                use nametag_piece(who, nametag_color(who, nametag), _tag_render_w, _tag_render_h, nametag_static(nametag_shown(who)), True)

    if what is not None and what != "":
        window:
            id "window"
            at (textbox_shift_smooth(prev_shift, shift, duration) if animate_shift else textbox_shift_static(shift))
            ysize _say_box_height
            background At(Frame(Transform(Crop((0, 330, 912, 187), "gui/textbox paper unripped.png"), zoom=menu_notebook_zoom), 240, 170, 240, 40, tile=False, xsize=int(912 * menu_notebook_zoom), xalign=0.5, ysize=_say_box_height + 96, yalign=1.0), Transform(alpha=gui.textbox_alpha))

            fixed:
                xalign 1.0
                xoffset -300
                yalign 0.0
                yoffset 60 + (_say_box_height - gui.textbox_height)
                xsize 80
                vbox:
                    xalign 1.0
                    spacing 18
                    imagebutton:
                        idle Transform("gui/side.png", crop=(764, 380, 26, 29), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#000000"), xalign=0.5)
                        hover Transform("gui/side.png", crop=(764, 380, 26, 29), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        selected_idle Transform("gui/side.png", crop=(764, 380, 26, 29), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        selected_hover Transform("gui/side.png", crop=(764, 380, 26, 29), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        selected skip_is_armed()
                        action Function(toggle_skip_armed) alternate Skip(fast=True, confirm=True)
                    imagebutton:
                        idle Transform("gui/side.png", crop=(764, 413, 31, 40), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#000000"), xalign=0.5)
                        hover Transform("gui/side.png", crop=(764, 413, 31, 40), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        selected Transform("gui/side.png", crop=(764, 413, 31, 40), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        action ShowMenu('history')
                    imagebutton:
                        idle Transform("gui/side.png", crop=(764, 461, 30, 30), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#000000"), xalign=0.5)
                        hover Transform("gui/side.png", crop=(764, 461, 30, 30), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        selected Transform("gui/side.png", crop=(764, 461, 30, 30), zoom=1.4, matrixcolor=ColorizeMatrix("#000000", "#2E9F53"), xalign=0.5)
                        action ShowMenu('notebook_closed_menu')

            text what id "what" ypos _say_text_top

init python:
    _nametag_state = {"line": None, "who": None, "prev": None, "swap": False}

    def skip_is_armed():
        return bool(renpy.session.get("skip_armed", False))

    def toggle_skip_armed():
        # Armed skip stays on until toggled off; it only advances over seen text.
        # Kept in renpy.session so rollback doesn't revert the player's choice.
        renpy.session["skip_armed"] = not skip_is_armed()
        if skip_is_armed():
            renpy.config.skipping = "slow"
        else:
            renpy.config.skipping = None
        renpy.restart_interaction()

    # Tab now toggles the armed skip instead of Ren'Py's built-in toggle.
    config.keymap["toggle_skip"] = []
    config.overlay_screens.append("skip_toggle_key")

    def skip_delay_seconds():
        afm = float(getattr(preferences, "afm_time", 15.0) or 0.0)
        return 1.0 - 0.8 * max(0.0, min(1.0, afm / 30.0))

    def skip_apply_speed():
        # Skip delay follows the auto-forward slider: left = 1.0s (slowest), right = 0.2s (fastest).
        afm = float(getattr(preferences, "afm_time", 15.0) or 0.0)
        config.skip_delay = int(round(skip_delay_seconds() * 1000))

    config.start_interact_callbacks.append(lambda: skip_apply_speed())

    def skip_rearm_callback():
        if not skip_is_armed() or renpy.config.skipping:
            return
        try:
            node = renpy.game.script.lookup(renpy.game.context().current)
            if isinstance(node, renpy.ast.Say) and renpy.game.context().seen_current(True):
                renpy.config.skipping = "slow"
        except Exception:
            pass

    config.start_interact_callbacks.append(skip_rearm_callback)

    def nametag_plain(who):
        if who is None:
            return None
        return renpy.filter_text_tags(who, allow=[])

    def nametag_paper_left():
        # Left edge of the opaque textbox paper on screen (paper art: x=114 of 912, centred).
        return int((config.screen_width - 912 * menu_notebook_zoom) / 2 + 114 * menu_notebook_zoom)

    def nametag_hidden(who=None):
        # Whole tag tucked behind the paper.
        return nametag_paper_left() - 18 + 6

    def nametag_shown(who):
        # Stops once the last letter has cleared the paper edge.
        tw = Text(who, style="say_label").size()[0]
        return max(-18, nametag_paper_left() - 18 - 24 - int(tw) - 24)

    _nametag_explicit = {}

    def nametag_color(who, explicit=None):
        # Colour comes from the Character's show_nametag="#hex"; remembered so the outgoing tag keeps it.
        name = nametag_plain(who)
        if explicit:
            _nametag_explicit[name] = explicit
            return explicit
        if name in _nametag_explicit:
            return _nametag_explicit[name]
        return gui.hover_color

    def nametag_track(who, what):
        # Recomputed only when the line changes, so redraws don't restart the animation.
        st = _nametag_state
        name = nametag_plain(who)
        if renpy.predicting():
            return {"swap": name != st["who"], "prev": st["who"]}
        if st["line"] != what:
            st["swap"] = (name != st["who"])
            st["prev"] = st["who"]
            st["line"] = what
            st["who"] = name
        return st

transform nametag_static(x):
    xoffset x

transform nametag_retract(x_from, x_to):
    xoffset x_from
    easein 0.8 xoffset x_to

transform nametag_extend(x_from, x_to, wait):
    xoffset x_from
    pause wait
    easeout 0.8 xoffset x_to

screen skip_toggle_key():
    key "K_TAB" action Function(toggle_skip_armed)

screen nametag_piece(name, color, w, h, anim, main):
    window:
        if main:
            id "namebox"
        style "namebox"
        at anim
        xpos 18
        yalign 1.0
        yoffset -100
        xsize w
        ysize h
        background At(Transform("gui/nametag tab.png", crop=(117, 352, 202, 63), xalign=0.0, yalign=1.0, zoom=menu_notebook_zoom, matrixcolor=ColorizeMatrix("#000000", color)), Transform(alpha=gui.textbox_alpha))
        fixed:
            xsize w
            ysize h
            if main:
                text name id "who":
                    style "say_label"
                    xanchor 0.0
                    yanchor 0.5
                    xpos 24
                    ypos int(round(h / 2.0))
                    text_align 0.0
            else:
                text name:
                    style "say_label"
                    xanchor 0.0
                    yanchor 0.5
                    xpos 24
                    ypos int(round(h / 2.0))
                    text_align 0.0

screen multiple_say(who, what, multiple):
    if multiple and multiple[1] == 2:
        $ _block = int(multiple[0])
        $ _say_base_viewport_height = max(120, gui.textbox_height - gui.dialogue_ypos - 10)
        $ _say_cap_box_height = int(config.screen_height * 0.92)
        $ _say_cap_viewport_height = max(120, _say_cap_box_height - gui.dialogue_ypos - 10)
        $ _say_content_height = estimate_dialogue_content_height(what, gui.dialogue_width, gui.text_size)
        $ _say_viewport_height = min(_say_cap_viewport_height, max(_say_base_viewport_height, _say_content_height))
        $ _say_box_height = gui.dialogue_ypos + _say_viewport_height + 10

        # Match split placement to the textbox's rendered width at current y-size.
        $ _src_w, _src_h = _multiple_textbox_source_size_safe()
        $ _src_left_w = max(1, int(_src_w / 2))
        $ _src_right_w = max(1, int(_src_w - _src_left_w))
        $ _scale = (float(_say_box_height) / float(max(1, _src_h)))
        $ _render_w = max(2, int(round(float(_src_w) * _scale)))
        $ _left_w = max(1, int(round(float(_src_left_w) * _scale)))
        $ _right_w = max(1, int(_render_w - _left_w))

        $ _split_gap = 18
        $ _split_shift_x = 220
        $ _box_base_x = int((config.screen_width - _render_w) / 2) + _split_shift_x
        $ _left_gap_push = int(_split_gap / 2)
        $ _right_gap_push = int(_split_gap - _left_gap_push)
        $ _panel_x = ((_box_base_x - _left_gap_push) if _block == 1 else (_box_base_x + _left_w + _right_gap_push))
        $ _panel_w = (_left_w if _block == 1 else _right_w)

        $ _text_pad_x = int(max(24, round(44.0 * _scale)))
        $ _namebox_x = _panel_x + int(max(12, round(24.0 * _scale)))
        $ _bg_crop = _multiple_textbox_half_crop(_block)
        $ _content_w = max(120, _panel_w - (_text_pad_x * 2))

        $ shift = 0
        $ prev_shift = 0
        $ duration = 0.0
        $ animate_shift = False
        if cinematic_textbox_shift and "bottom" in cinematic_bars_state["sides"]:
            if cinematic_bars_state["target_size"] > 0:
                $ shift = cinematic_bars_state["target_size"]
                $ prev_shift = cinematic_textbox_shift_prev_shift
                $ duration = cinematic_bars_state["duration"] if cinematic_bars_state["animate"] else 0.0
                $ animate_shift = (prev_shift != shift and duration > 0.0)
            elif cinematic_bars_state.get("retracting", False):
                $ prev_shift = cinematic_bars_state.get("retract_from", 0)
                $ duration = cinematic_bars_state["duration"]
                $ animate_shift = (prev_shift > 0 and duration > 0.0)

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                at (textbox_shift_smooth(prev_shift, shift, duration) if animate_shift else textbox_shift_static(shift))
                xpos _namebox_x
                yoffset -(_say_box_height) - 20
                xminimum max(180, int(_panel_w * 0.40))
                text who id "who"

        if what is not None and what != "":
            window:
                id "window"
                style "empty"
                at (textbox_shift_smooth(prev_shift, shift, duration) if animate_shift else textbox_shift_static(shift))
                xfill False
                xpos _panel_x
                xsize _panel_w
                yalign gui.textbox_yalign
                yoffset -40
                ysize _say_box_height
                background At(Transform("gui/textbox paper unripped.png", crop=_bg_crop, xalign=0.0, yalign=1.0, xsize=_panel_w * 1.5, ysize=_say_box_height + 120, zoom=menu_notebook_zoom), Transform(alpha=gui.textbox_alpha))

                text what id "what":
                    style "say_dialogue"
                    xpos _text_pad_x
                    xsize _content_w
    else:
        use say(who, what)

transform textbox_shift_smooth(prev, new, duration):
    yoffset -prev
    cinematic_ease duration yoffset -new

## Two transforms: one animated, one static
transform textbox_shift_animated(shift, duration):
    on show:
        yoffset 0
        linear duration yoffset -shift
    yoffset -shift

transform textbox_shift_static(shift):
    yoffset -shift

init python:
    _multiple_textbox_source_size = None

    def _multiple_textbox_source_size_safe():
        global _multiple_textbox_source_size

        if _multiple_textbox_source_size is None:
            try:
                _multiple_textbox_source_size = renpy.image_size("gui/textbox.png")
            except Exception:
                _multiple_textbox_source_size = (config.screen_width, gui.textbox_height)

        src_w, src_h = _multiple_textbox_source_size
        return (int(src_w), int(src_h))

    def _multiple_textbox_half_crop(block):
        """Return a crop rect for left/right half of the textbox source image."""
        src_w, src_h = _multiple_textbox_source_size_safe()
        left_w = max(1, int(src_w / 2))
        right_w = max(1, int(src_w - left_w))
        if int(block) == 1:
            return (0, 0, left_w, src_h)
        return (left_w, 0, right_w, src_h)

init python:
    def enable_cinematic_textbox_shift(enable=True):
        """
        Enables or disables shifting the textbox and namebox up with the bottom bar.
        """
        global cinematic_textbox_shift
        cinematic_textbox_shift = enable

    def _cinematic_after_say(event, interact=True, **kwargs):
        if event == "end" and interact:
            setattr(store, "cinematic_textbox_shift_prev_shift", getattr(store, "cinematic_textbox_shift_last_size", 0))
            _cinematic_bars_state = getattr(store, "cinematic_bars_state", {})
            if _cinematic_bars_state.get("retract_pending", False):
                # First click after retract — the animation played, now clear everything
                _cinematic_bars_state["retracting"] = False
                _cinematic_bars_state["retract_from"] = 0
                _cinematic_bars_state["retract_pending"] = False
    config.all_character_callbacks.append(_cinematic_after_say)

    def _cinematic_say_allow_dismiss():
        _cinematic_bars_state = getattr(store, "cinematic_bars_state", {})
        until = _cinematic_bars_state.get("block_dismiss_until", 0.0)
        if until > 0.0:
            if _cinematic_time.time() < until:
                return False
            _cinematic_bars_state["block_dismiss_until"] = 0.0
        return True
    config.say_allow_dismiss = _cinematic_say_allow_dismiss

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # Side image support is currently disabled due to syntax issues.
    # if not renpy.variant("small"):
    #     fixed:
    #         add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    yoffset -40

    background At(Transform("gui/textbox paper unripped.png", xalign=0.5, yalign=1.0, zoom=menu_notebook_zoom), Transform(alpha=gui.textbox_alpha))

style namebox:
    xanchor 0.0
    xminimum 202
    xsize 202
    yanchor 1.0
    yalign 1.0
    yoffset 0
    ysize 63
    background At(Transform("gui/nametag tab.png", crop=(117, 352, 202, 63), xalign=0.0, yalign=1.0, zoom=menu_notebook_zoom, matrixcolor=ColorizeMatrix("#000000", gui.hover_color)), Transform(alpha=gui.textbox_alpha))
    padding (0, 0, 0, 0)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    text_align 0.0
    yalign 0.5
    color "#ffffff"

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos + 18

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos + 18

            text prompt style "input_prompt"
            input id "input" default_focus True


style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


init python:
    def speak_player_reply(text, literal=False):
        if not text or not getattr(store, "_profile_context_active", True):
            return

        if literal:
            text = text.replace("[", "[[").replace("{", "{{")

        renpy.say(p, text)

    # Screen actions can't start an interaction, so the picked caption is
    # stored here and spoken once the menu interaction has returned.
    _pending_player_reply = [None]

    def set_pending_player_reply(caption):
        _pending_player_reply[0] = caption

    _display_menu = renpy.display_menu

    def menu(items, *args, **kwargs):
        _pending_player_reply[0] = None
        rv = _display_menu(items, *args, **kwargs)
        caption = _pending_player_reply[0]
        _pending_player_reply[0] = None
        if caption and not kwargs.get("predict_only", False):
            speak_player_reply(caption)
        return rv

    _renpy_input = renpy.input

    def player_input(*args, **kwargs):
        result = _renpy_input(*args, **kwargs)
        speak_player_reply(result, literal=True)
        return result


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init python:
    import math
    import re

    _renpy_text_tag_re = re.compile(r"\{[^\}]*\}")

    def _choice_menu_id():
        filename, line = renpy.get_filename_line()
        return "%s:%s" % (filename, line)

    def _choice_caption_key(caption):
        return renpy.substitute(caption)

    def _ensure_menu_choice_history():
        legacy = getattr(persistent, "menu_choice_history", None)

        if getattr(persistent, "menu_choice_history_display", None) is None or not isinstance(persistent.menu_choice_history_display, dict):
            # Migrate legacy storage so existing data remains visible.
            persistent.menu_choice_history_display = legacy if isinstance(legacy, dict) else {}

        if getattr(persistent, "menu_choice_history_current", None) is None or not isinstance(persistent.menu_choice_history_current, dict):
            persistent.menu_choice_history_current = {}

        if not isinstance(getattr(persistent, "menu_choice_history_loop", None), dict):
            persistent.menu_choice_history_loop = {}

        if not isinstance(legacy, dict):
            persistent.menu_choice_history = {}

    def start_menu_choice_session(menu_id):
        _ensure_menu_choice_history()

        loop_id = getattr(persistent, "retry_counter", 0) or 0
        loops = persistent.menu_choice_history_loop
        previous = persistent.menu_choice_history_current.get(menu_id, [])

        # Revisiting a menu inside the same loop keeps showing the previous loop's path.
        if loops.get(menu_id) == loop_id and isinstance(previous, list):
            return

        if isinstance(previous, list) and previous:
            persistent.menu_choice_history_display[menu_id] = list(previous)

        persistent.menu_choice_history_current[menu_id] = []
        loops[menu_id] = loop_id

    def remember_menu_choice(menu_id, caption):
        _ensure_menu_choice_history()
        caption_key = _choice_caption_key(caption)

        choices = persistent.menu_choice_history_current.get(menu_id, [])
        if not isinstance(choices, list):
            choices = []

        choices.append(caption_key)
        persistent.menu_choice_history_current[menu_id] = choices

    def get_menu_choice_order_marks(menu_id):
        _ensure_menu_choice_history()

        marks = {}
        choices = persistent.menu_choice_history_display.get(menu_id, [])
        if not isinstance(choices, list):
            return marks

        for idx, cap in enumerate(choices, 1):
            marks.setdefault(cap, []).append(idx)

        return marks

    def get_auto_pick_item(items, marks):
        """Return the marked item that was chosen latest in the previous encounter."""
        if not marks:
            return None

        # The profile select menu must never auto-pick: a quit-save taken there would reload itself forever.
        if any(_choice_caption_key(i.caption).startswith("Profile ") for i in items if i.action):
            return None

        best_item = None
        best_order = -1

        for i in items:
            if not i.action:
                continue

            key = _choice_caption_key(i.caption)
            order_marks = marks.get(key, [])
            if not order_marks:
                continue

            last_order = order_marks[-1]
            if last_order > best_order:
                best_order = last_order
                best_item = i

        return best_item

    def underline_if_marked(text, is_marked):
        if not is_marked:
            return text
        return "{u}%s{/u}" % text

    def estimate_inline_choice_content_height(items, text_pixel_width, number_keys=False, text_size=34):
        """Estimate inline-choice content height so the textbox can grow before scrolling."""
        width = max(120.0, float(text_pixel_width))
        size = max(16.0, float(text_size))
        avg_char_px = max(7.0, size * 0.56)
        chars_per_line = max(10, int(width / avg_char_px))
        line_height = int(size + 10)
        row_padding = 4
        spacing = 2

        total = 0
        for i in items:
            caption = renpy.substitute(i.caption)
            prefix_chars = 3 if (number_keys and i.action is not None) else 0
            raw_lines = max(1, int(math.ceil(float(len(caption) + prefix_chars) / chars_per_line)))

            # Action rows are truncated in the resting state, so fully wrapped
            # estimates push the list too high. Cap at 2 lines to preserve
            # baseline alignment while still allowing tall menus to grow.
            if i.action is not None:
                lines = min(2, raw_lines)
            else:
                lines = raw_lines

            if i.action is None:
                total += (lines * line_height)
            else:
                total += (lines * line_height) + row_padding

            total += spacing

        return max(0, total)

    _dialogue_measure_cache = {}

    def measure_dialogue_height(text, text_pixel_width, text_size=34):
        # Real rendered height of the wrapped dialogue; falls back to the estimate.
        key = (text, text_pixel_width, text_size)
        if key in _dialogue_measure_cache:
            return _dialogue_measure_cache[key]
        try:
            d = Text(text or "", style="say_dialogue", xpos=0, ypos=0, xsize=text_pixel_width)
            h = int(renpy.render(d, text_pixel_width, 4000, 0, 0).get_size()[1])
            if h <= 0:
                raise ValueError("empty")
        except Exception:
            return estimate_dialogue_content_height(text, text_pixel_width, text_size)
        if len(_dialogue_measure_cache) > 300:
            _dialogue_measure_cache.clear()
        _dialogue_measure_cache[key] = h
        return h

    def estimate_dialogue_content_height(text, text_pixel_width, text_size=34):
        """Estimate dialogue content height for adaptive say-window growth."""
        width = max(140.0, float(text_pixel_width))
        size = max(16.0, float(text_size))
        avg_char_px = max(7.0, size * 0.6)
        chars_per_line = max(12, int((width - 16.0) / avg_char_px))
        line_height = int(size * 1.55)

        raw = renpy.substitute(text or "")
        cleaned = _renpy_text_tag_re.sub("", raw)
        line_count = max(1, int(math.ceil(float(len(cleaned)) / chars_per_line)))

        # Keep a little extra breathing room so larger fonts don't clip.
        return max(line_height + 12, (line_count * line_height) + int(line_height * 0.35) + 12)

screen choice(items):
    style_prefix "choice"
    zorder 100

    default max_visible = 5
    default _inline_hovered = ""
    default _menu_session_initialized = False
    default _auto_pick_scheduled = False

    if persistent.cheddar and cheddar_state["open"] and not renpy.get_screen("say"):
        use cheddar_tab_piece

    ## Shift choices up when cinematic bottom bar is active.
    $ _choice_shift = cinematic_bars_state["target_size"] if cinematic_textbox_shift and "bottom" in cinematic_bars_state["sides"] and cinematic_bars_state["target_size"] > 0 else 0

    ## Tooltip captured reactively every interaction so the notecard updates live.
    $ tt = GetTooltip()

    ## Count only items with a live action — insensitive/disabled items
    ## (passed when config.menu_include_disabled is True) are excluded so
    ## a menu that looks like 2 choices isn't mis-classified as 3+.
    $ _active = [i for i in items if i.action]

    ## Scroll threshold: grid mode caps at 4 items (5+ scroll); default uses max_visible.
    $ _scroll_at = 4 if persistent.grid_choices else max_visible

    ## Number-key map: maps each active item's id to its 1-based choice number.
    $ _num_map = {id(i): idx+1 for idx, i in enumerate(_active)}
    $ _menu_id = _choice_menu_id()

    if not _menu_session_initialized:
        $ start_menu_choice_session(_menu_id)
        $ _menu_session_initialized = True

    $ _menu_choice_marks = get_menu_choice_order_marks(_menu_id)
    $ _auto_pick_item = get_auto_pick_item(_active, _menu_choice_marks)
    $ _auto_pick_delay = max(0.25, min(2.0, float(getattr(preferences, "afm_time", 15.0) or 15.0) / 15.0))

    if persistent.auto_pick_underlined_choice and preferences.afm_enable and _auto_pick_item is not None and not _auto_pick_scheduled:
        $ _auto_pick_scheduled = True
        timer _auto_pick_delay action [Function(remember_menu_choice, _menu_id, _auto_pick_item.caption), Function(set_pending_player_reply, _auto_pick_item.caption), _auto_pick_item.action] repeat False

    ## Bind number keys 1–9 (main and numpad) to the corresponding active choice when enabled.
    if persistent.number_keys:
        for _kidx, _kitem in enumerate(_active):
            if _kidx < 9:
                key "K_%d" % (_kidx + 1) action [Function(remember_menu_choice, _menu_id, _kitem.caption), Function(set_pending_player_reply, _kitem.caption), _kitem.action]
                key "K_KP%d" % (_kidx + 1) action [Function(remember_menu_choice, _menu_id, _kitem.caption), Function(set_pending_player_reply, _kitem.caption), _kitem.action]

    if persistent.inline_choices:
        # -- Inline mode: choices appear inside the dialogue box ----------
        $ _inline_text_max = max(120, gui.dialogue_width - gui.scrollbar_size - 120)
        $ _inline_top_padding = gui.dialogue_ypos + 15
        $ _inline_base_viewport_height = max(120, gui.textbox_height - _inline_top_padding - 10)
        $ _inline_min_viewport_height = _inline_base_viewport_height
        $ _inline_cap_box_height = min(int(config.screen_height * 0.72), gui.textbox_height + 420)
        $ _inline_cap_viewport_height = max(120, _inline_cap_box_height - _inline_top_padding - 10)
        $ _inline_content_height = estimate_inline_choice_content_height(items, _inline_text_max, persistent.number_keys, gui.text_size)
        $ _inline_target_viewport_height = max(_inline_min_viewport_height, _inline_content_height)
        $ _inline_viewport_height = (min(_inline_cap_viewport_height, _inline_target_viewport_height) if persistent.inline_choice_grow else _inline_base_viewport_height)
        $ _inline_box_height = _inline_top_padding + _inline_viewport_height + 10
        $ _inline_needs_scroll = (_inline_content_height > (_inline_viewport_height + 2))
        $ _inline_top_spacer = 0

        window:
            style "window"
            at textbox_shift_static(_choice_shift)
            ysize _inline_box_height
            background At(Frame(Transform(Crop((0, 330, 912, 187), "gui/textbox paper unripped.png"), zoom=menu_notebook_zoom), 240, 170, 240, 40, tile=False, xsize=int(912 * menu_notebook_zoom), xalign=0.5, ysize=_inline_box_height + 96, yalign=1.0), Transform(alpha=gui.textbox_alpha))

            viewport:
                mousewheel True
                draggable "touch"
                scrollbars ("vertical" if _inline_needs_scroll else None)
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos _inline_top_padding
                ymaximum _inline_viewport_height

                vbox:
                    style "inline_choice_vbox"
                    xoffset 10
                    yoffset _inline_top_spacer
                    for i in items:
                        if i.action is None:
                            text i.caption style "inline_choice_caption"
                        else:
                            $ safe_caption = renpy.substitute(i.caption)
                            $ _short = truncate_to_width(safe_caption, _inline_text_max)
                            $ _choice_key = _choice_caption_key(i.caption)
                            $ _was_marked = bool(_menu_choice_marks.get(_choice_key, []))
                            #TODO: Make the truncuation revealing work better. have it always show the full text the same way.
                            $ _hovering = (_inline_hovered == i.caption)
                            $ _nprefix = ("%d. " % _num_map[id(i)]) if persistent.number_keys and id(i) in _num_map else ""
                            $ _base_caption = (safe_caption if _hovering else _short)
                            $ _caption_display = _nprefix + underline_if_marked(_base_caption, _was_marked)
                            button:
                                alt i.caption
                                style "inline_choice_button"
                                hovered SetScreenVariable("_inline_hovered", i.caption)
                                unhovered SetScreenVariable("_inline_hovered", "")
                                action [Function(remember_menu_choice, _menu_id, i.caption), Function(set_pending_player_reply, i.caption), i.action]
                                hbox:
                                    spacing 20
                                    $ _bullet_deaths = profile_choice_bullet_deaths(i.caption, persistent.lildeaths)
                                    $ _bullet_num = min(7, max(0, _bullet_deaths))
                                    $ _bullet_img = "gui/bullet_loop.png" if _bullet_num == 0 else "gui/bullet_loop%s.png" % _bullet_num
                                    yalign 0.5

                                    add Transform(
                                        _bullet_img,
                                        zoom=0.09,
                                        matrixcolor=(
                                            ColorizeMatrix(gui.hover_color, "#ffffff")
                                            if _inline_hovered == i.caption
                                            else ColorizeMatrix("#000000", "#ffffff") ##707070 is also pretty for the dark color
                                        )
                                    ):
                                        yalign 0.5
                                    


                                    text _caption_display:
                                        style "inline_choice_button_text"
                                        xmaximum _inline_text_max
                                        xfill True
                                        layout "subtitle"
                                        yalign 0.5

    else:
        # Fallback menu renderer for non-inline mode (important on fresh persistent data).
        vbox:
            style "choice_vbox"
            at textbox_shift_static(_choice_shift)

            for i in items:
                if i.action is None:
                    text i.caption style "choice_button_text"
                else:
                    $ _choice_key = _choice_caption_key(i.caption)
                    $ _was_marked = bool(_menu_choice_marks.get(_choice_key, []))
                    $ _nprefix = ("%d. " % _num_map[id(i)]) if persistent.number_keys and id(i) in _num_map else ""
                    $ _caption_display = _nprefix + underline_if_marked(i.caption, _was_marked)
                    button:
                        style "choice_button"
                        action [Function(remember_menu_choice, _menu_id, i.caption), Function(set_pending_player_reply, i.caption), i.action]

                        text _caption_display style "choice_button_text"

   



style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 650 # Lowered even further for more space above notecard
    yanchor 0.0 # Anchor to the top
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

## Grid choice button — narrower for side-by-side layout
style grid_choice_button is choice_button:
    xsize 560
    yminimum 90

style grid_choice_button_text is choice_button_text:
    text_align 0.0
    xalign 0.5

## Tooltip notecard — yellow card showing full choice text on hover
style notecard_frame is frame:
    background Frame(Solid("#f5e179"), Borders(12, 10, 12, 10))
    padding (20, 14, 20, 14)
    xalign 0.5

style notecard_text:
    color "#1a1000"
    text_align 0.0
    size gui.text_size

## Inline choices — choices displayed inside the dialogue box
style inline_choice_vbox:
    spacing 4
    xsize (gui.dialogue_width - gui.scrollbar_size)

style inline_choice_caption is say_dialogue:
    italic True

style inline_choice_button is default:
    background None
    padding (0, 3, 0, 3)
    xfill True

style inline_choice_button_text is default:
    properties gui.text_properties("dialogue")
    idle_color "#000000"
    hover_color gui.inline_choice_hover_text_color
    insensitive_color "#6060607f"


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

            


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    def start_over_reset():
        _active_slot = int(getattr(persistent, "active_profile_slot", 1) or 1)
        _pref_keys = [
            "font_choice",
            "text_size_offset",
            "text_outline",
            "dialogue_text_color",
            "inline_hover_text_color",
            "talking_animation_mode",
            "grid_choices", #TODO: This is probably fine to remove since I basically have no use for it anymore.
            "inline_choices",
            "inline_choice_grow",
            "number_keys",
            "auto_pick_underlined_choice",
            "pictureBookUnlocked",
            "gallery_unlocked",
            "menu_choice_history",
            "menu_choice_history_display",
            "menu_choice_history_current",
            "menu_choice_history_loop",
            "cheddar",
            "active_profile_slot",
            "profile_slot_data",
            "profile_preference_overrides",
            "profile_template_state",
            "profile_playtime_seconds",
            "total_playtime_seconds",
            "profile_schema_version",
        ]
        _saved = {k: getattr(persistent, k, None) for k in _pref_keys}
        persistent._clear()
        for k, v in _saved.items():
            if v is not None:
                setattr(persistent, k, v)

        # Start Over should not continue from an old quit-save; wipe active profile saves.
        try:
            profile_delete_slot(_active_slot, save_persistent=False)
        except Exception:
            try:
                qslot = profile_quitsave_slot(_active_slot)
                if renpy.can_load(qslot):
                    renpy.unlink_save(qslot)
            except Exception:
                pass

        renpy.save_persistent()

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action [Function(set_profile_save_context), Function(profile_sync_active, True), Function(profile_save_quitsave), Start()]
            textbutton _("Profiles") action ShowMenu("profiles")
        else:

            textbutton _("History") action ShowMenu("history")
            if persistent.canSave:
                textbutton _("Save") action ShowMenu("save")
        if persistent.canSave:
            textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if main_menu and getattr(persistent, "gallery_unlocked", True):
            textbutton _("Gallery") action Start("gallery")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action [Function(set_profile_save_context), Function(profile_sync_active, True), Function(profile_save_quitsave), MainMenu()]

        textbutton _("About") action ShowMenu("about")
        textbutton _("Fake Credits") action ShowMenu("fake_credits")
        textbutton _("Credits") action ShowMenu("real_credits")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")
        
        if not main_menu or getattr(store, "_profile_context_active", False):
            textbutton _("Start Over") action Show("start_over_confirm")



        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action [Function(set_profile_save_context), Function(profile_sync_active, True), Function(profile_save_quitsave), Quit(confirm=not main_menu)]

        if main_menu:
            null height 8
            text _("Total Playtime\n(All Profiles): \n[format_playtime_hms(profile_total_playtime_seconds(True))]")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    use menu_notebook_backdrop
    use menu_notebook_page_content

    ## Show an update notification banner if a newer version is available.
    use update_notification

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    use menu_notebook_tabs_overlay


screen notebook_closed_menu():

    tag menu
    default notebook_closing = False

    on "show" action [SetVariable("menu_notebook_open", False), SetVariable("menu_notebook_tab", "game"), SetVariable("menu_notebook_settings_page", "main")]

    if notebook_closing:
        timer 0.42 action Return()
        fixed:
            at notebook_ascend_close
            use menu_notebook_backdrop
            use menu_notebook_page_content
            use menu_notebook_tabs_overlay
    else:
        fixed:
            at notebook_descend_short
            use menu_notebook_backdrop
            use menu_notebook_page_content
            use menu_notebook_tabs_overlay

    key "game_menu" action (
        Return() if notebook_closing else
        [
            SetScreenVariable("notebook_closing", True),
            SetVariable("menu_notebook_open", False),
            SetVariable("menu_notebook_tab", "game"),
            SetVariable("menu_notebook_settings_page", "main")
        ]
    )
    key "mouseup_3" action (
        Return() if notebook_closing else
        [
            SetScreenVariable("notebook_closing", True),
            SetVariable("menu_notebook_open", False),
            SetVariable("menu_notebook_tab", "game"),
            SetVariable("menu_notebook_settings_page", "main")
        ]
    )


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True
    background None

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    use menu_notebook_backdrop

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    use menu_notebook_tabs_overlay

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background None

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1300

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


define menu_notebook_zoom = 2
default menu_notebook_tab = "game"
default menu_notebook_open = False
default menu_notebook_hovered_tab = ""
default menu_notebook_settings_page = "main"
define menu_notebook_tab_hover_push = 70
define menu_notebook_tab_1_x = 0
define menu_notebook_tab_2_x = 0
define menu_notebook_tab_3_x = -60
define menu_notebook_tab_hitbox_x_adjust = 22
define menu_notebook_tab_label_1_x = 604
define menu_notebook_tab_label_2_x = 604
define menu_notebook_tab_label_3_x = 676
define menu_notebook_tab_label_x_adjust = 0
define menu_notebook_tab_label_y_adjust = 0
define menu_notebook_tab_label_1_y = -112
define menu_notebook_tab_label_2_y = -242
define menu_notebook_tab_label_3_y = -378
define menu_notebook_tab_label_box_w = int(round(202 * menu_notebook_zoom))
define menu_notebook_tab_label_box_h = int(round(63 * menu_notebook_zoom))
define menu_notebook_tab_text_pad = 24
define menu_notebook_tab_labels = {1: (_("Info"), 30), 2: (_("Settings"), 28), 3: (_("Game"), 27)}
define menu_notebook_tab_art_right = {1: 806, 2: 806, 3: 818}

init python:
    def menu_notebook_tab_push(n):
        # Like the nametag: slide the tab out just far enough for its label to clear the paper edge.
        label, size = menu_notebook_tab_labels[n]
        tw = Text(label, font="custom_fonts/Scribble Show.ttf", size=size).size()[0]
        paper_right = (818 - 456) * menu_notebook_zoom
        visible = menu_notebook_tab_art_right[n] - paper_right
        return max(0, int(tw) + 2 * menu_notebook_tab_text_pad - visible)
define menu_notebook_postit_grid_center_x = 0
define menu_notebook_postit_grid_center_y = 60
define menu_notebook_postit_center_spacing = 410
define menu_notebook_postit_col_spacing = int(menu_notebook_postit_center_spacing / 2)
define menu_notebook_postit_row_spacing = menu_notebook_postit_center_spacing
define menu_notebook_settings_page_col_spacing = 395
define menu_notebook_settings_page_col_left_x = -menu_notebook_settings_page_col_spacing
define menu_notebook_settings_page_col_mid_x = 0
define menu_notebook_settings_page_col_right_x = menu_notebook_settings_page_col_spacing
define menu_notebook_postit_crop = (556, 111, 190, 192)
define menu_notebook_postit_col_left_x = menu_notebook_postit_grid_center_x - menu_notebook_postit_col_spacing
define menu_notebook_postit_col_mid_x = menu_notebook_postit_grid_center_x
define menu_notebook_postit_col_right_x = menu_notebook_postit_grid_center_x + menu_notebook_postit_col_spacing
define menu_notebook_postit_row_top_y = menu_notebook_postit_grid_center_y - int(menu_notebook_postit_row_spacing / 2)
define menu_notebook_postit_row_bottom_y = menu_notebook_postit_grid_center_y + int(menu_notebook_postit_row_spacing / 2)
define menu_notebook_postit_content_y = -40
define menu_notebook_postit_font = "defaultFonts/IndieFlower-Regular.ttf"
define menu_notebook_postit_title_text_size = 34
define menu_notebook_postit_body_text_size = 28
define menu_notebook_postit_slider_text_size = 28
define menu_notebook_postit_dropdown_main_size = 32
define menu_notebook_postit_dropdown_option_size = 30


transform notebook_page_flip_right:
    on show:
        alpha 0.0
        xoffset -140
        linear 0.24 alpha 1.0 xoffset 0

transform notebook_descend_short:
    on show:
        alpha 1.0
        yoffset -1200
        easeout 0.58 yoffset 0

transform notebook_ascend_close:
    yoffset 0
    linear 0.42 yoffset -1200


screen menu_notebook_backdrop():
    $ _tab_1_active = (menu_notebook_hovered_tab == "info")
    $ _tab_2_active = (menu_notebook_hovered_tab == "settings")
    $ _tab_3_active = (menu_notebook_hovered_tab == "game")
    $ _tab_1_on_top = menu_notebook_open and menu_notebook_tab == "info"
    $ _tab_2_on_top = menu_notebook_open and menu_notebook_tab == "settings"
    $ _tab_3_on_top = menu_notebook_open and menu_notebook_tab == "game"
    $ _tab_1_extend = _tab_1_active and not _tab_1_on_top
    $ _tab_2_extend = _tab_2_active and not _tab_2_on_top
    $ _tab_3_extend = _tab_3_active and not _tab_3_on_top

    add Transform("gui/tab 1.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_1_x + (menu_notebook_tab_push(1) if _tab_1_extend else 0), matrixcolor=ColorizeMatrix("#000000", "#E53935"))
    add Transform("gui/tab 2.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_2_x + (menu_notebook_tab_push(2) if _tab_2_extend else 0), matrixcolor=ColorizeMatrix("#000000", "#1E88E5"))
    add Transform("gui/tab 3.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_3_x + (menu_notebook_tab_push(3) if _tab_3_extend else 0), matrixcolor=ColorizeMatrix("#000000", "#FDD835"))

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset menu_notebook_tab_1_x + (menu_notebook_tab_push(1) if _tab_1_extend else 0) + menu_notebook_tab_label_1_x + menu_notebook_tab_label_x_adjust
        yoffset menu_notebook_tab_label_1_y + menu_notebook_tab_label_y_adjust
        xsize menu_notebook_tab_label_box_w
        ysize menu_notebook_tab_label_box_h
        text _("Info"):
            xanchor 1.0
            yanchor 0.5
            xpos menu_notebook_tab_label_box_w - menu_notebook_tab_text_pad
            ypos int(round(menu_notebook_tab_label_box_h / 2.0))
            text_align 1.0
            font "custom_fonts/Scribble Show.ttf"
            size 30
            color "#ffffff"
            outlines [(2, "#00000088", 0, 0)]

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset menu_notebook_tab_2_x + (menu_notebook_tab_push(2) if _tab_2_extend else 0) + menu_notebook_tab_label_2_x + menu_notebook_tab_label_x_adjust
        yoffset menu_notebook_tab_label_2_y + menu_notebook_tab_label_y_adjust
        xsize menu_notebook_tab_label_box_w
        ysize menu_notebook_tab_label_box_h
        text _("Settings"):
            xanchor 1.0
            yanchor 0.5
            xpos menu_notebook_tab_label_box_w - menu_notebook_tab_text_pad
            ypos int(round(menu_notebook_tab_label_box_h / 2.0))
            text_align 1.0
            font "custom_fonts/Scribble Show.ttf"
            size 28
            color "#ffffff"
            outlines [(2, "#00000088", 0, 0)]

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset menu_notebook_tab_3_x + (menu_notebook_tab_push(3) if _tab_3_extend else 0) + menu_notebook_tab_label_3_x + menu_notebook_tab_label_x_adjust
        yoffset menu_notebook_tab_label_3_y + menu_notebook_tab_label_y_adjust
        xsize menu_notebook_tab_label_box_w
        ysize menu_notebook_tab_label_box_h
        text _("Game"):
            xanchor 1.0
            yanchor 0.5
            xpos menu_notebook_tab_label_box_w - menu_notebook_tab_text_pad
            ypos int(round(menu_notebook_tab_label_box_h / 2.0))
            text_align 1.0
            font "custom_fonts/Scribble Show.ttf"
            size 27
            color "#ffffff"
            outlines [(2, "#00000088", 0, 0)]

    if menu_notebook_open:
        add Transform("gui/notebook paper full.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5)
    else:
        add Transform("gui/notebook paper full.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#7A5A32", "#E8D7BE"))
    add Transform("gui/rings.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#909090"))

    # Draw the selected tab above the paper so it appears attached to the active page.
    if menu_notebook_open and menu_notebook_tab == "info":
        add Transform("gui/tab 1.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_1_x, matrixcolor=ColorizeMatrix("#000000", "#E53935"))

        fixed:
            xalign 0.5
            yalign 0.5
            xoffset menu_notebook_tab_1_x + menu_notebook_tab_label_1_x + menu_notebook_tab_label_x_adjust
            yoffset menu_notebook_tab_label_1_y + menu_notebook_tab_label_y_adjust
            xsize menu_notebook_tab_label_box_w
            ysize menu_notebook_tab_label_box_h
            text _("Info"):
                xanchor 1.0
                yanchor 0.5
                xpos menu_notebook_tab_label_box_w - menu_notebook_tab_text_pad
                ypos int(round(menu_notebook_tab_label_box_h / 2.0))
                text_align 1.0
                font "custom_fonts/Scribble Show.ttf"
                size 30
                color "#ffffff"
                outlines [(2, "#00000088", 0, 0)]

    elif menu_notebook_open and menu_notebook_tab == "settings":
        add Transform("gui/tab 2.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_2_x, matrixcolor=ColorizeMatrix("#000000", "#1E88E5"))

        fixed:
            xalign 0.5
            yalign 0.5
            xoffset menu_notebook_tab_2_x + menu_notebook_tab_label_2_x + menu_notebook_tab_label_x_adjust
            yoffset menu_notebook_tab_label_2_y + menu_notebook_tab_label_y_adjust
            xsize menu_notebook_tab_label_box_w
            ysize menu_notebook_tab_label_box_h
            text _("Settings"):
                xanchor 1.0
                yanchor 0.5
                xpos menu_notebook_tab_label_box_w - menu_notebook_tab_text_pad
                ypos int(round(menu_notebook_tab_label_box_h / 2.0))
                text_align 1.0
                font "custom_fonts/Scribble Show.ttf"
                size 28
                color "#ffffff"
                outlines [(2, "#00000088", 0, 0)]

    elif menu_notebook_open and menu_notebook_tab == "game":
        add Transform("gui/tab 3.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_3_x, matrixcolor=ColorizeMatrix("#000000", "#FDD835"))

        fixed:
            xalign 0.5
            yalign 0.5
            xoffset menu_notebook_tab_3_x + menu_notebook_tab_label_3_x + menu_notebook_tab_label_x_adjust
            yoffset menu_notebook_tab_label_3_y + menu_notebook_tab_label_y_adjust
            xsize menu_notebook_tab_label_box_w
            ysize menu_notebook_tab_label_box_h
            text _("Game"):
                xanchor 1.0
                yanchor 0.5
                xpos menu_notebook_tab_label_box_w - menu_notebook_tab_text_pad
                ypos int(round(menu_notebook_tab_label_box_h / 2.0))
                text_align 1.0
                font "custom_fonts/Scribble Show.ttf"
                size 27
                color "#ffffff"
                outlines [(2, "#00000088", 0, 0)]

    if menu_notebook_open and menu_notebook_tab == "settings":
        # 2x2 corner layout: top-left/top-right and bottom-left/bottom-right.
        if menu_notebook_settings_page == "text_appearance":
            use notebook_text_appearance_page(back_action=SetVariable("menu_notebook_settings_page", "main"))
        else:
            use notebook_sound_settings_postit(menu_notebook_postit_col_left_x, menu_notebook_postit_row_top_y)
            use notebook_display_choices_postit(menu_notebook_postit_col_right_x, menu_notebook_postit_row_top_y)
            use notebook_character_postit(menu_notebook_postit_col_left_x, menu_notebook_postit_row_bottom_y)
            use notebook_text_flow_postit(menu_notebook_postit_col_right_x, menu_notebook_postit_row_bottom_y)


screen menu_notebook_tabs_overlay():
    $ _tab_1_active = (menu_notebook_hovered_tab == "info")
    $ _tab_2_active = (menu_notebook_hovered_tab == "settings")
    $ _tab_3_active = (menu_notebook_hovered_tab == "game")

    imagebutton:
        idle Transform("gui/tab 1.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_1_x + menu_notebook_tab_hitbox_x_adjust, alpha=0.01)
        hover Transform("gui/tab 1.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_1_x + menu_notebook_tab_hitbox_x_adjust, alpha=0.01)
        action [SetVariable("menu_notebook_tab", "info"), SetVariable("menu_notebook_open", True)]
        hovered SetVariable("menu_notebook_hovered_tab", "info")
        unhovered SetVariable("menu_notebook_hovered_tab", "")
        focus_mask True

    imagebutton:
        idle Transform("gui/tab 2.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_2_x + menu_notebook_tab_hitbox_x_adjust, alpha=0.01)
        hover Transform("gui/tab 2.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_2_x + menu_notebook_tab_hitbox_x_adjust, alpha=0.01)
        action [SetVariable("menu_notebook_tab", "settings"), SetVariable("menu_notebook_open", True), SetVariable("menu_notebook_settings_page", "main")]
        hovered SetVariable("menu_notebook_hovered_tab", "settings")
        unhovered SetVariable("menu_notebook_hovered_tab", "")
        focus_mask True

    imagebutton:
        idle Transform("gui/tab 3.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_3_x + menu_notebook_tab_hitbox_x_adjust, alpha=0.01)
        hover Transform("gui/tab 3.png", zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, xoffset=menu_notebook_tab_3_x + menu_notebook_tab_hitbox_x_adjust, alpha=0.01)
        action [SetVariable("menu_notebook_tab", "game"), SetVariable("menu_notebook_open", True)]
        hovered SetVariable("menu_notebook_hovered_tab", "game")
        unhovered SetVariable("menu_notebook_hovered_tab", "")
        focus_mask True


screen menu_notebook_page_content():
    frame:
        background None
        xalign 0.5
        yalign 0.5
        xsize 1280
        ysize 760

        if not menu_notebook_open:
            null

        elif menu_notebook_tab == "game":
            vbox:
                style_prefix "postit"
                at notebook_page_flip_right
                spacing 18
                xalign 0.48
                yalign 0.56

                text _("Game") size 52 color "#2d2d2d"

                textbutton _("Start") action [Function(set_profile_save_context), Function(profile_sync_active, True), Function(profile_save_quitsave), Start()] style "postit_button"
                if persistent.canSave:
                    textbutton _("Load") action ShowMenu("load") style "postit_button"
                textbutton _("Profiles") action ShowMenu("profiles") style "postit_button"
                textbutton _("Quit") action [Function(set_profile_save_context), Function(profile_sync_active, True), Function(profile_save_quitsave), Quit(confirm=False)] style "postit_button"

        elif menu_notebook_tab == "info":
            vbox:
                style_prefix "postit"
                at notebook_page_flip_right
                spacing 14
                xalign 0.48
                yalign 0.56

                text _("Info") size 52 color "#2d2d2d"

                textbutton _("About") action ShowMenu("about") style "postit_button"
                textbutton _("Fake Credits") action ShowMenu("fake_credits") style "postit_button"
                textbutton _("Credits") action ShowMenu("real_credits") style "postit_button"
                if main_menu and getattr(persistent, "gallery_unlocked", True):
                    textbutton _("Gallery") action Start("gallery") style "postit_button"
                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                    textbutton _("Help") action ShowMenu("help") style "postit_button"

        else:
            fixed:
                at notebook_page_flip_right
                xalign 0.48
                yalign 0.56
                xsize 1060
                ysize 620


screen notebook_overlay_slider(slider_value, slider_width=160):
    fixed:
        xsize slider_width
        ysize 14

        bar:
            value slider_value
            style "notebook_pref_slider_core"
            xsize slider_width

        # Keep the empty bar art on top so fill appears underneath it.
        add Frame(Transform("gui/horizontal bar empty.png", crop=(575, 177, 83, 14), matrixcolor=ColorizeMatrix("#000000", "#111111")), 7, 0, 7, 0, tile=False) xsize slider_width ysize 14


screen notebook_sound_settings_postit(xpos, ypos):
    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 220
            spacing 8

            text _("Sound"):
                xalign 0.5
                style "postit_title_text"

            fixed:
                xalign 0.5
                xsize 220
                ysize 158

                $ _col_w = 96
                $ _left_x = 4
                $ _right_x = 120
                $ _top_y = 4
                $ _bottom_y = 78
                $ _bar_y = 34

                if config.has_music or config.has_sound or config.has_voice:
                    fixed:
                        xpos _left_x
                        ypos _top_y
                        xsize _col_w
                        ysize 72
                        text _("Main"):
                            xsize _col_w
                            size menu_notebook_postit_slider_text_size
                            color "#2d2d2d"
                            font menu_notebook_postit_font
                            layout "subtitle"
                        fixed:
                            ypos _bar_y
                            xsize _col_w
                            use notebook_overlay_slider(slider_value=Preference("mixer main volume"), slider_width=_col_w)

                if config.has_music:
                    fixed:
                        xpos _right_x
                        ypos _bottom_y
                        xsize _col_w
                        ysize 72 #TODO: Do not make this a fixed height if possible, it should be possible to be adaptable.
                        text _("Music"):
                            xsize _col_w
                            size menu_notebook_postit_slider_text_size
                            color "#2d2d2d"
                            font menu_notebook_postit_font
                            layout "subtitle"
                        fixed:
                            ypos _bar_y
                            xsize _col_w
                            use notebook_overlay_slider(slider_value=Preference("music volume"), slider_width=_col_w)

                if config.has_voice:
                    fixed:
                        xpos _right_x
                        ypos _top_y
                        xsize _col_w
                        ysize 72
                        text _("Voice"):
                            xsize _col_w
                            size menu_notebook_postit_slider_text_size
                            color "#2d2d2d"
                            font menu_notebook_postit_font
                            layout "subtitle"
                        fixed:
                            ypos _bar_y
                            xsize _col_w
                            use notebook_overlay_slider(slider_value=Preference("voice volume"), slider_width=_col_w)

                if config.has_sound:
                    fixed:
                        xpos _left_x
                        ypos _bottom_y
                        xsize _col_w
                        ysize 72
                        text _("Effects"):
                            xsize _col_w
                            size menu_notebook_postit_slider_text_size
                            color "#2d2d2d"
                            font menu_notebook_postit_font
                            layout "subtitle"
                        fixed:
                            ypos _bar_y
                            xsize _col_w
                            use notebook_overlay_slider(slider_value=Preference("sound volume"), slider_width=_col_w)

                

            if config.has_music or config.has_sound or config.has_voice:
                textbutton _("Mute All"):
                    xalign 0.5
                    action Preference("all mute", "toggle")
                    style "postit_mute_all_button"


screen notebook_display_choices_postit(xpos, ypos):
    default display_open = False
    default choices_open = False

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 232
            spacing 3

            text _("Display"):
                xalign 0.5
                style "postit_title_text"

            if renpy.variant("pc") or renpy.variant("web"):
                vbox:
                    spacing 1

                    textbutton _("Display"):
                        action [ToggleLocalVariable("display_open"), SetLocalVariable("choices_open", False)]
                        style "postit_dropdown_toggle_button"

                    if display_open:
                        textbutton _("Window") action Preference("display", "window") style "postit_dropdown_button"
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") style "postit_dropdown_button"

            textbutton _("Text Appearance..."):
                action SetVariable("menu_notebook_settings_page", "text_appearance")
                style "postit_dropdown_button"

            vbox:
                spacing 1

                textbutton _("Choice Options"):
                    action [ToggleLocalVariable("choices_open"), SetLocalVariable("display_open", False)]
                    style "postit_dropdown_toggle_button"

                if choices_open:
                    textbutton _("Grow Inline") action ToggleField(persistent, "inline_choice_grow") style "postit_dropdown_button"
                    textbutton _("Number Keys") action ToggleField(persistent, "number_keys") style "postit_dropdown_button"
                    textbutton _("Auto Pick") action ToggleField(persistent, "auto_pick_underlined_choice") style "postit_dropdown_button"


screen notebook_character_postit(xpos, ypos):
    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 220
            spacing 10

            text _("Character"):
                xalign 0.5
                style "postit_title_text"

            textbutton _("Change Character Info") action Show("change_names_menu")
            textbutton _("Change Your Name") action [SetVariable("from_menu", True), Start("nameSelect")]


screen notebook_text_flow_postit(xpos, ypos):
    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 220
            spacing 6

            text _("Text Flow"):
                xalign 0.5
                style "postit_title_text"

            fixed:
                xalign 0.5
                xsize 220
                ysize 112

                $ _col_w = 90
                $ _left_x = 0
                $ _right_x = 130
                $ _label_y = 0
                $ _bar_y = 34
                $ _value_y = 66

                fixed:
                    xpos _left_x
                    ypos _label_y
                    xsize _col_w
                    ysize 100

                    text _("Text Speed"):
                        xsize _col_w
                        size 24
                        color "#2d2d2d"
                        font menu_notebook_postit_font
                        layout "nobreak"

                    fixed:
                        ypos _bar_y
                        xsize _col_w
                        use notebook_overlay_slider(slider_value=Preference("text speed"), slider_width=_col_w)

                    if preferences.text_cps == 0:
                        text _("Instant"):
                            xpos 0
                            ypos _value_y
                            xsize _col_w
                            size 22
                            color "#2d2d2d"
                            layout "nobreak"
                    else:
                        text "[int(preferences.text_cps)] chars/sec":
                            xpos 0
                            ypos _value_y
                            xsize _col_w
                            size 22
                            color "#2d2d2d"
                            layout "nobreak"

                fixed:
                    xpos _right_x
                    ypos _label_y
                    xsize _col_w
                    ysize 100

                    text _("Auto-Forward"):
                        xsize _col_w
                        size 24
                        color "#2d2d2d"
                        font menu_notebook_postit_font
                        layout "nobreak"

                    fixed:
                        ypos _bar_y
                        xsize _col_w
                        use notebook_overlay_slider(slider_value=Preference("auto-forward time"), slider_width=_col_w)

                    text "[skip_delay_seconds():.1f] sec/line":
                        xpos 0
                        ypos _value_y
                        xsize _col_w
                        size 22
                        color "#2d2d2d"
                        layout "nobreak"

            vbox:
                xalign 0.5
                xsize 220
                spacing 0

                text _("Skip Options"):
                    xalign 0.5
                    size 22
                    color "#2d2d2d"
                    font menu_notebook_postit_font

                textbutton _("Unseen Text"):
                    action Preference("skip", "toggle")
                    xalign 0.5
                    xsize 220
                    style "postit_mute_all_button"
                    text_style "postit_skip_button_text"

                textbutton _("After Choices"):
                    action Preference("after choices", "toggle")
                    xalign 0.5
                    xsize 220
                    style "postit_mute_all_button"
                    text_style "postit_skip_button_text"

                textbutton _("Transitions"):
                    action InvertSelected(Preference("transitions", "toggle"))
                    xalign 0.5
                    xsize 220
                    style "postit_mute_all_button"
                    text_style "postit_skip_button_text"


screen notebook_text_appearance_fonts_postit(xpos, ypos):
    default font_open = False
    default customfont_open = False
    default outline_open = False

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 220
            spacing 2

            text _("Text"):
                xalign 0.5
                size 30
                style "postit_title_text"

            textbutton ("[current_font().replace('-Regular','').replace('-',' ').replace('.ttf','').replace('.otf','').split('/')[-1]]  {font=DejaVuSans.ttf}[u'▲' if font_open else u'▼']{/font}"):
                action ToggleLocalVariable("font_open")
                style "postit_dropdown_toggle_button"
                text_size 26

            if font_open:
                frame:
                    padding (8, 6, 8, 6)
                    vbox:
                        style_prefix "postit_radio"
                        textbutton _("Default (DejaVu)"):
                            action [SetFont("DejaVuSans.ttf"), SetLocalVariable("font_open", False)]
                            text_font "DejaVuSans.ttf"
                            text_size 24
                        textbutton _("Pacifico"):
                            action [SetFont("defaultFonts/Pacifico-Regular.ttf"), SetLocalVariable("font_open", False)]
                            text_font "defaultFonts/Pacifico-Regular.ttf"
                            text_size 24
                        textbutton _("Indie Flower"):
                            action [SetFont("defaultFonts/IndieFlower-Regular.ttf"), SetLocalVariable("font_open", False)]
                            text_font "defaultFonts/IndieFlower-Regular.ttf"
                            text_size 24
                        textbutton _("Shadows Into Light"):
                            action [SetFont("defaultFonts/ShadowsIntoLight-Regular.ttf"), SetLocalVariable("font_open", False)]
                            text_font "defaultFonts/ShadowsIntoLight-Regular.ttf"
                            text_size 24

                        if CUSTOM_FONTS:
                            null height 4
                            for _cname, _cfile in CUSTOM_FONTS:
                                textbutton _(_cname):
                                    action [SetFont(_cfile), SetLocalVariable("font_open", False)]
                                    text_font _cfile
                                    text_size 24

            text _("Text Size"):
                size 24
                color "#2d2d2d"
                font menu_notebook_postit_font

            use notebook_overlay_slider(slider_value=TextSizeValue(), slider_width=160)

            textbutton ("[persistent.text_outline.capitalize()]  {font=DejaVuSans.ttf}[u'▲' if outline_open else u'▼']{/font}"):
                action ToggleLocalVariable("outline_open")
                style "postit_dropdown_toggle_button"
                text_size 26

            if outline_open:
                frame:
                    padding (8, 6, 8, 6)
                    vbox:
                        style_prefix "postit_radio"
                        textbutton _("None"):
                            action [SetTextOutline("none"), SetLocalVariable("outline_open", False)]
                            text_size 24
                        textbutton _("Outline"):
                            action [SetTextOutline("outline"), SetLocalVariable("outline_open", False)]
                            text_size 24
                        textbutton _("Shadow"):
                            action [SetTextOutline("shadow"), SetLocalVariable("outline_open", False)]
                            text_size 24

            hbox:
                spacing 10

                vbox:
                    xsize 100
                    spacing 2

                    text _("Textbox Spacing"):
                        size 22
                        color "#2d2d2d"
                        font menu_notebook_postit_font

                    use notebook_overlay_slider(slider_value=LetterSpacingValue(), slider_width=100)

                vbox:
                    xsize 100
                    spacing 2

                    text _("Textbox Opacity"):
                        size 22
                        color "#2d2d2d"
                        font menu_notebook_postit_font

                    use notebook_overlay_slider(slider_value=TextboxOpacityValue(), slider_width=100)


screen notebook_text_appearance_colors_postit(xpos, ypos):
    default color_picker_open = None
    default dialogue_text_color_draft = getattr(persistent, "dialogue_text_color", "#404040")
    default inline_hover_text_color_draft = getattr(persistent, "inline_hover_text_color", "#336600")

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 220
            spacing 3

            text _("Colors"):
                xalign 0.5
                size 30
                style "postit_title_text"

            textbutton _("Text Color"):
                action SetLocalVariable("color_picker_open", None if color_picker_open == "text" else "text")
                style "postit_dropdown_toggle_button"
                text_size 26

            if color_picker_open == "text":
                frame:
                    padding (10, 8, 10, 8)
                    background Transform(Frame("gui/frame_outline.png", gui.frame_borders, tile=gui.frame_tile), matrixcolor=ColorizeMatrix("#ffffff", getattr(persistent, "dialogue_text_color", "#404040")))
                    vbox:
                        spacing 8
                        hbox:
                            spacing 10
                            frame:
                                background Solid("#ffffff18")
                                padding (8, 4)
                                xsize 170
                                yminimum 40
                                input:
                                    id "dialogue_text_color_input"
                                    color getattr(persistent, "dialogue_text_color", "#404040")
                                    value LocalVariableInputValue("dialogue_text_color_draft")
                                    length 7
                                    allow "#0123456789abcdefABCDEF"
                                    xfill True
                                    yalign 0.5
                                    style "input"
                            textbutton _("Apply"):
                                action Function(request_dialogue_text_color_apply, dialogue_text_color_draft)
                                text_size 24
                            textbutton _("Default"):
                                action [SetLocalVariable("dialogue_text_color_draft", "#404040"), Function(sync_color_input, "dialogue_text_color_input", "#404040"), Function(request_dialogue_text_color_apply, "#404040")]
                                text_size 24

                        hbox:
                            spacing 8
                            for _label, _color in DIALOGUE_COLOR_PRESETS:
                                button:
                                    xsize 34
                                    ysize 24
                                    padding (0, 0)
                                    background Solid(_color)
                                    hover_background Solid(_color)
                                    focus_mask None
                                    action [SetLocalVariable("dialogue_text_color_draft", _color), Function(pick_color_preset, "dialogue_text_color", _color)]
                                    tooltip _label

            textbutton _("Hover Color"):
                action SetLocalVariable("color_picker_open", None if color_picker_open == "hover" else "hover")
                style "postit_dropdown_toggle_button"
                text_size 26

            if color_picker_open == "hover":
                frame:
                    padding (10, 8, 10, 8)
                    background Transform(Frame("gui/frame_outline.png", gui.frame_borders, tile=gui.frame_tile), matrixcolor=ColorizeMatrix("#ffffff", getattr(persistent, "inline_hover_text_color", "#336600")))
                    vbox:
                        spacing 8
                        hbox:
                            spacing 10
                            frame:
                                background Solid("#ffffff18")
                                padding (8, 4)
                                xsize 170
                                yminimum 40
                                input:
                                    id "inline_hover_text_color_input"
                                    color getattr(persistent, "inline_hover_text_color", "#336600")
                                    value LocalVariableInputValue("inline_hover_text_color_draft")
                                    length 7
                                    allow "#0123456789abcdefABCDEF"
                                    xfill True
                                    yalign 0.5
                                    style "input"
                            textbutton _("Apply"):
                                action Function(request_inline_hover_text_color_apply, inline_hover_text_color_draft)
                                text_size 24
                            textbutton _("Default"):
                                action [SetLocalVariable("inline_hover_text_color_draft", "#336600"), Function(sync_color_input, "inline_hover_text_color_input", "#336600"), Function(request_inline_hover_text_color_apply, "#336600")]
                                text_size 24

                        hbox:
                            spacing 8
                            for _label, _color in INLINE_HOVER_COLOR_PRESETS:
                                button:
                                    xsize 34
                                    ysize 24
                                    padding (0, 0)
                                    background Solid(_color)
                                    hover_background Solid(_color)
                                    focus_mask None
                                    action [SetLocalVariable("inline_hover_text_color_draft", _color), Function(pick_color_preset, "inline_hover_text_color", _color)]
                                    tooltip _label


screen notebook_text_appearance_extra_postit(xpos, ypos):
    default talking_mode_open = False

    fixed:
        xalign 0.5
        yalign 0.5
        xoffset xpos
        yoffset ypos
        xsize 260
        ysize 220

        add Transform("gui/post it 1.png", crop=menu_notebook_postit_crop, zoom=menu_notebook_zoom, xalign=0.5, yalign=0.5, matrixcolor=ColorizeMatrix("#000000", "#F4E7A3"))

        vbox:
            style_prefix "postit"
            xalign 0.5
            ypos menu_notebook_postit_content_y
            xsize 220
            spacing 3

            text _("Extra"):
                xalign 0.5
                size 30
                style "postit_title_text"

            textbutton ("[get_talking_animation_mode_label()]  {font=DejaVuSans.ttf}[u'▲' if talking_mode_open else u'▼']{/font}"):
                action ToggleLocalVariable("talking_mode_open")
                style "postit_dropdown_toggle_button"
                text_size 26

            if talking_mode_open:
                frame:
                    padding (8, 6, 8, 6)
                    vbox:
                        style_prefix "postit_radio"
                        textbutton _("Count + Text Speed"):
                            action [SetField(persistent, "talking_animation_mode", TALKING_MODE_ADAPTIVE), SetLocalVariable("talking_mode_open", False)]
                            text_size 24
                        textbutton _("Fixed Interval"):
                            action [SetField(persistent, "talking_animation_mode", TALKING_MODE_FIXED), SetLocalVariable("talking_mode_open", False)]
                            text_size 24
                        textbutton _("Count + Fixed Speed"):
                            action [SetField(persistent, "talking_animation_mode", TALKING_MODE_MIXED), SetLocalVariable("talking_mode_open", False)]
                            text_size 24


screen notebook_text_appearance_page(back_action=None):
    fixed:
        xalign 0.5
        yalign 0.5
        xsize 1060
        ysize 620

        use notebook_text_appearance_fonts_postit(menu_notebook_settings_page_col_left_x, menu_notebook_postit_row_top_y)
        use notebook_text_appearance_colors_postit(menu_notebook_settings_page_col_mid_x, menu_notebook_postit_row_top_y)
        use notebook_text_appearance_extra_postit(menu_notebook_settings_page_col_right_x, menu_notebook_postit_row_top_y)

        if back_action is not None:
            textbutton _("Back to Settings"):
                action back_action
                style "postit_button"
                xalign 0.5
                yalign 1.0
                yoffset -20


screen notebook_preferences_embedded():
    # Legacy fallback: notebook settings are now rendered directly inside post-it screens.
    null #TODO: Remove this later




screen profiles():

    tag menu
    default copy_source = int(getattr(persistent, "active_profile_slot", 1))

    use game_menu(_("Profiles"), scroll="viewport"):

        vbox:
            spacing 22
            #TODO: Rewrite this text, also probably not show the amount of loops and deaths to the player as to not really spoil as much.
            text _("Manage profile slots. Delete clears a slot. Copy duplicates one slot into another.")
            text _("Copy Source: Profile [copy_source]")

            for slot in range(1, 4):
                $ _used = profile_slot_is_used(slot)
                $ _deaths = int(profile_slot_state_value(slot, "lildeaths", 0) or 0)
                $ _retries = int(profile_slot_state_value(slot, "retry_counter", 0) or 0)
                $ _ptime = format_playtime_hms(profile_slot_playtime_seconds(slot, include_live=True))
                $ _source_used = profile_slot_is_used(copy_source)
                $ _bullet_num = min(7, max(0, _deaths))
                $ _bullet_img = "gui/bullet_loop.png" if _bullet_num == 0 else "gui/bullet_loop%s.png" % _bullet_num

                frame:
                    xfill True

                    vbox:
                        spacing 10

                        hbox:
                            spacing 12
                            yalign 0.5

                            add Transform(
                                _bullet_img,
                                zoom=0.11,
                                matrixcolor=ColorizeMatrix("#000000", "#ffffff")
                            ):
                                yalign 0.5

                            text _("Profile [slot] - [profile_slot_label(slot)]"):
                                yalign 0.5

                        text _("Deaths: [_deaths]    Loops: [_retries]")
                        text _("Playtime: [_ptime]")

                        hbox:
                            spacing 20

                            textbutton _("Use As Copy Source") action SetScreenVariable("copy_source", slot)

                            if copy_source != slot:
                                if _used:
                                    textbutton _("Copy Here (Overwrite)") action Show("profile_copy_overwrite_confirm", source_slot=copy_source, target_slot=slot) sensitive _source_used
                                else:
                                    textbutton _("Copy Here") action [Function(profile_copy_slot, copy_source, slot, False, True), Function(renpy.restart_interaction)] sensitive _source_used

                            textbutton _("Delete Slot") action Show("profile_delete_confirm", slot=slot)

            text _("Tip: Overwrite only appears when the target profile is already used.")
            
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.
screen about():
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                if persistent.lildeaths == 0:
                    $ persistent.fakeAbout_knowledge = True
                    text "[gui.about!t]\n"
                else:
                    $ persistent.trueAbout_knowledge = True
                    if persistent.fakeAbout_knowledge == True:
                        $ gui.about = _p("""
                        As you've already noticed I may have lied a little...

                        This is not really the game I said it would be.

                        It's more about choice, or the lack thereof.

                        No matter how much we try to branch off to different choices in games like this, they always tend to come together towards the same few endings with maybe a variation or two in it.

                        The game is also about something else but I don't want to spoil that for you, you'll need to learn it yourself.

                        To conclude this info I'd like to thank Chris Cornell/Paper Dino for making *Save the Date*, a work that heavily touched me and inspired this game (or these games — I went through a few iterations of this project before I ended up with this one.)

                        Thank you for reading this and for playing my game, I hope you are enjoying it.

                        - Red Semele
                        """)
                    else:
                        $ gui.about = _p("""
                        This is a game about choice, or the lack thereof, and how the players deal with that.

                        No matter how much we try to branch off to different choices in games like this, they always tend to come together towards the same few endings with maybe a variation or two in it.

                        The game is also about something else but I don't want to spoil that for you, you'll need to learn it yourself.

                        To conclude this info I'd like to thank Chris Cornell/Paper Dino for making *Save the Date*, a work that heavily touched me and inspired this game (or these games — I went through a few iterations of this project before I ended up with this one.)

                        Thank you for reading this and for playing my game, I hope you are enjoying it.

                        - Red Semele
                        """)
                    text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots("save", _("Save"))


screen load():

    tag menu

    use file_slots("load", _("Load"))


screen file_slots(mode, title):

    $ _active_profile = int(getattr(persistent, "active_profile_slot", 1))

    use game_menu(title):

        on "show" action FilePage(profile_page_name(1))

        fixed:

            text "Profile [_active_profile]":
                style "page_label_text"
                xalign 0.5

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action ([Function(profile_prepare_save), FileSave(slot)] if mode == "save" else FileLoad(slot))

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage(profile_page_name("auto"))

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage(profile_page_name("quick"))

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(profile_page_name(page))

                    textbutton _(">") action FilePageNext()

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("Profile 1") action [Function(profile_switch, 1), FilePage(profile_page_name(1)), Function(renpy.restart_interaction)]
                    textbutton _("Profile 2") action [Function(profile_switch, 2), FilePage(profile_page_name(1)), Function(renpy.restart_interaction)]
                    textbutton _("Profile 3") action [Function(profile_switch, 3), FilePage(profile_page_name(1)), Function(renpy.restart_interaction)]

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    ## Apply the saved text size once when leaving preferences so gui.rebuild()
    ## only fires once, keeping the slider drag smooth while open.
    on "hide" action Function(apply_text_size_current)
    on "replaced" action Function(apply_text_size_current)
    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "check"
                    label _("Choices")
                    textbutton _("Compact Grid") action ToggleField(persistent, "grid_choices")
                    textbutton _("Inline") action ToggleField(persistent, "inline_choices")
                    textbutton _("Grow Inline Textbox") action ToggleField(persistent, "inline_choice_grow")
                    textbutton _("Number Keys") action ToggleField(persistent, "number_keys")
                    textbutton _("Auto Pick Underlined") action ToggleField(persistent, "auto_pick_underlined_choice")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    ## Show the exact characters-per-second rate next to the bar.
                    if preferences.text_cps == 0:
                        text _("Instant") size (gui.label_text_size - 8) color gui.idle_color
                    else:
                        text "[int(preferences.text_cps)] chars/sec" size (gui.label_text_size - 8) color gui.idle_color

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            ## Add the new button here
            null height gui.pref_spacing
            textbutton _("Text Appearance...") action ShowMenu("text_settings")
            textbutton _("Alter characters") action Show("change_names_menu")
            textbutton _("Alter own info") action [SetVariable("from_menu", True), Start("nameSelect")]
            


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground Null()
    selected_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=42, xalign=0.0, yalign=0.5)
    selected_hover_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=42, xalign=0.0, yalign=0.5)

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground Null()
    selected_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=42, xalign=0.0, yalign=0.5)
    selected_hover_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=42, xalign=0.0, yalign=0.5)

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 160
    xalign 1.0
    ysize 14
    left_bar Frame(Transform("gui/horizontal bar filling.png", crop=(578, 201, 78, 14), matrixcolor=ColorizeMatrix("#000000", gui.hover_color)), 7, 0, 7, 0, tile=False)
    right_bar Frame(Transform("gui/horizontal bar empty.png", crop=(575, 177, 83, 14), matrixcolor=ColorizeMatrix("#000000", "#111111")), 7, 0, 7, 0, tile=False)
    thumb Transform(Solid(Color(gui.hover_color).shade(0.7)), xsize=12, ysize=12)

style notebook_pref_slider_core is slider_slider:
    xsize 160
    xalign 1.0
    ysize 14
    left_bar Frame(Transform("gui/horizontal bar filling.png", crop=(578, 201, 78, 14), matrixcolor=ColorizeMatrix("#000000", gui.hover_color)), 7, 0, 7, 0, tile=False)
    right_bar Solid("#0000")
    thumb Transform(Solid(Color(gui.hover_color).shade(0.7)), xsize=12, ysize=12)

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style postit_text is gui_text
style postit_button is button
style postit_button_text is button_text
style postit_dropdown_toggle_button is postit_button
style postit_dropdown_toggle_button_text is postit_button_text
style postit_dropdown_button is postit_button
style postit_dropdown_button_text is postit_button_text
style postit_mute_all_button_text is mute_all_button_text
style postit_skip_button_text is postit_button_text

style postit_text:
    font menu_notebook_postit_font
    size menu_notebook_postit_body_text_size
    color "#2d2d2d"

style postit_button_text:
    font menu_notebook_postit_font
    size menu_notebook_postit_body_text_size

style postit_title_text:
    font menu_notebook_postit_font
    size menu_notebook_postit_title_text_size
    bold True
    color "#2d2d2d"

style postit_dropdown_button:
    background None
    left_padding 0
    right_padding 0
    top_padding 0
    bottom_padding 0
    top_margin 0
    bottom_margin 0
    yminimum 0

style postit_dropdown_toggle_button:
    background None
    left_padding 0
    right_padding 0
    top_padding 0
    bottom_padding 0
    top_margin 0
    bottom_margin 0
    yminimum 0

style postit_dropdown_button_text:
    font menu_notebook_postit_font
    size menu_notebook_postit_dropdown_option_size
    layout "nobreak"
    idle_color "#2d2d2d"
    hover_color gui.hover_color
    selected_idle_color gui.hover_color
    selected_hover_color gui.hover_color


style postit_dropdown_toggle_button_text:
    font menu_notebook_postit_font
    size menu_notebook_postit_dropdown_main_size
    layout "nobreak"

style postit_mute_all_button_text:
    font menu_notebook_postit_font
    size menu_notebook_postit_body_text_size
    selected_idle_color gui.hover_color
    selected_hover_color gui.hover_color

style postit_mute_all_button is mute_all_button:
    foreground Null()
    selected_foreground Null()
    selected_hover_foreground Null()

style postit_radio_button is radio_button:
    foreground Null()
    selected_foreground Null()
    selected_hover_foreground Null()

style postit_radio_button_text is radio_button_text:
    selected_idle_color gui.hover_color
    selected_hover_color gui.hover_color

style postit_skip_button_text:
    font menu_notebook_postit_font
    size 22
    idle_color "#2d2d2d"
    selected_idle_color gui.hover_color
    selected_hover_color gui.hover_color


## Text Appearance screen ######################################################
##
## A dedicated sub-menu for all text customisation: font, outline, text size,
## letter spacing, textbox opacity, and a live preview.

screen text_settings():

    tag menu

    ## Screen-local state for which dropdown is open.
    default font_open        = False
    default outline_open     = False
    default customfont_open  = False
    default talking_mode_open = False
    default color_picker_open = None
    default dialogue_text_color_draft = getattr(persistent, "dialogue_text_color", "#404040")
    default inline_hover_text_color_draft = getattr(persistent, "inline_hover_text_color", "#336600")

    ## Rebuild styles once when the player navigates away so gui.rebuild()
    ## never fires mid-drag (which would kill the drag gesture).
    on "hide"     action Function(apply_text_size_current)
    on "replaced" action Function(apply_text_size_current)

    use game_menu(_("Text Appearance"), scroll="viewport"):

        vbox:
            xfill True

            ## -- Dropdowns row ------------------------------------------------
            vbox:
                spacing 28

                hbox:
                    box_wrap True
                    xfill True
                    xmaximum 1140
                    spacing 40

                    ## Font dropdown
                    vbox:
                        spacing 4

                        label _("Font"):
                            style "pref_label"

                        textbutton ("[current_font().replace('-Regular','').replace('-',' ').replace('.ttf','').replace('.otf','')]  [u'▲' if font_open else u'▼']"):
                            action ToggleLocalVariable("font_open")
                            style "pref_label_text"
                            ypadding 6
                            xsize 338
                            text_xalign 0.0

                        if font_open:
                            frame:
                                padding (8, 6, 8, 6)
                                vbox:
                                    style_prefix "radio"
                                    textbutton _("Default (DejaVu)"):
                                        action [SetFont("DejaVuSans.ttf"), SetLocalVariable("font_open", False)]
                                        text_font "DejaVuSans.ttf"
                                    textbutton _("Pacifico"):
                                        action [SetFont("defaultFonts/Pacifico-Regular.ttf"), SetLocalVariable("font_open", False)]
                                        text_font "defaultFonts/Pacifico-Regular.ttf"
                                    textbutton _("Indie Flower"):
                                        action [SetFont("defaultFonts/IndieFlower-Regular.ttf"), SetLocalVariable("font_open", False)]
                                        text_font "defaultFonts/IndieFlower-Regular.ttf"
                                    textbutton _("Shadows Into Light"):
                                        action [SetFont("defaultFonts/ShadowsIntoLight-Regular.ttf"), SetLocalVariable("font_open", False)]
                                        text_font "defaultFonts/ShadowsIntoLight-Regular.ttf"

                    if CUSTOM_FONTS:
                        vbox:
                            spacing 4

                            label _("Custom Font"):
                                style "pref_label"

                            textbutton ("[current_font().replace('-Regular','').replace('-',' ').replace('.ttf','').replace('.otf','').split('/')[-1] if current_font().startswith('custom_fonts/') else 'None selected']  [u'▲' if customfont_open else u'▼']"):
                                action ToggleLocalVariable("customfont_open")
                                style "pref_label_text"
                                ypadding 6
                                xsize 338
                                text_xalign 0.0

                            if customfont_open:
                                frame:
                                    padding (8, 6, 8, 6)
                                    vbox:
                                        style_prefix "radio"
                                        for _cname, _cfile in CUSTOM_FONTS:
                                            textbutton _(_cname):
                                                action [SetFont(_cfile), SetLocalVariable("customfont_open", False)]
                                                text_font _cfile

                hbox:
                    box_wrap True
                    xfill True
                    xmaximum 1140
                    spacing 40

                    ## Text Outline dropdown
                    vbox:
                        spacing 4

                        label _("Text Outline"):
                            style "pref_label"

                        textbutton ("[persistent.text_outline.capitalize()]  [u'▲' if outline_open else u'▼']"):
                            action ToggleLocalVariable("outline_open")
                            style "pref_label_text"
                            ypadding 6
                            xsize 338
                            text_xalign 0.0

                        if outline_open:
                            frame:
                                padding (8, 6, 8, 6)
                                vbox:
                                    style_prefix "radio"
                                    textbutton _("None"):
                                        action [SetTextOutline("none"), SetLocalVariable("outline_open", False)]
                                    textbutton _("Outline"):
                                        action [SetTextOutline("outline"), SetLocalVariable("outline_open", False)]
                                    textbutton _("Shadow"):
                                        action [SetTextOutline("shadow"), SetLocalVariable("outline_open", False)]

                    ## Talking Animation dropdown
                    vbox:
                        spacing 4

                        label _("Talking Animation"):
                            style "pref_label"

                        textbutton ("[get_talking_animation_mode_label()]  [u'▲' if talking_mode_open else u'▼']"):
                            action ToggleLocalVariable("talking_mode_open")
                            style "pref_label_text"
                            ypadding 6
                            xsize 338
                            text_xalign 0.0

                        if talking_mode_open:
                            frame:
                                padding (8, 6, 8, 6)
                                vbox:
                                    style_prefix "radio"
                                    textbutton _("Count + Text Speed"):
                                        action [SetField(persistent, "talking_animation_mode", TALKING_MODE_ADAPTIVE), SetLocalVariable("talking_mode_open", False)]
                                    textbutton _("Fixed Interval"):
                                        action [SetField(persistent, "talking_animation_mode", TALKING_MODE_FIXED), SetLocalVariable("talking_mode_open", False)]
                                    textbutton _("Count + Fixed Speed"):
                                        action [SetField(persistent, "talking_animation_mode", TALKING_MODE_MIXED), SetLocalVariable("talking_mode_open", False)]

                    ## Dialogue Text Color custom hex
                    vbox:
                        spacing 4

                hbox:
                    box_wrap True
                    xfill True
                    xmaximum 1140
                    spacing 40

                    ## Dialogue Text Color custom hex
                    vbox:
                        spacing 4

                        textbutton _("Dialogue Text Color  [u'▲' if dialogue_text_color_open else u'▼']"):
                            action ToggleLocalVariable("dialogue_text_color_open")
                            style "pref_label_text"
                            ypadding 6
                            xsize 338
                            text_xalign 0.0

                        if dialogue_text_color_open:
                            frame:
                                padding (10, 8, 10, 8)
                                background Transform(Frame("gui/frame_outline.png", gui.frame_borders, tile=gui.frame_tile), matrixcolor=ColorizeMatrix("#ffffff", gui.hover_color))
                                vbox:
                                    spacing 8
                                    hbox:
                                        spacing 10
                                        frame:
                                            background Solid("#ffffff18")
                                            padding (8, 4)
                                            xsize 170
                                            yminimum 40
                                            input:
                                                value LocalVariableInputValue("dialogue_text_color_draft")
                                                length 7
                                                allow "#0123456789abcdefABCDEF"
                                                xfill True
                                                yalign 0.5
                                                style "input"
                                        textbutton _("Apply"):
                                            action Function(request_dialogue_text_color_apply, dialogue_text_color_draft)
                                        textbutton _("Default"):
                                            action [SetScreenVariable("dialogue_text_color_draft", "#404040"), Function(request_dialogue_text_color_apply, "#404040")]

                                    hbox:
                                        spacing 8
                                        for _label, _color in DIALOGUE_COLOR_PRESETS:
                                            button:
                                                xsize 34
                                                ysize 24
                                                background Solid(_color)
                                                action [SetScreenVariable("dialogue_text_color_draft", _color), Function(request_dialogue_text_color_apply, _color)]
                                                tooltip _label

                    ## Global Hover Color custom hex
                    vbox:
                        spacing 4

                        textbutton _("Hover Color (Global)  [u'▲' if inline_hover_text_color_open else u'▼']"):
                            action ToggleLocalVariable("inline_hover_text_color_open")
                            style "pref_label_text"
                            ypadding 6
                            xsize 338
                            text_xalign 0.0

                        if inline_hover_text_color_open:
                            frame:
                                padding (10, 8, 10, 8)
                                background Transform(Frame("gui/frame_outline.png", gui.frame_borders, tile=gui.frame_tile), matrixcolor=ColorizeMatrix("#ffffff", gui.hover_color))
                                vbox:
                                    spacing 8
                                    hbox:
                                        spacing 10
                                        frame:
                                            background Solid("#ffffff18")
                                            padding (8, 4)
                                            xsize 170
                                            yminimum 40
                                            input:
                                                id "inline_hover_text_color_input"
                                                value LocalVariableInputValue("inline_hover_text_color_draft")
                                                length 7
                                                allow "#0123456789abcdefABCDEF"
                                                xfill True
                                                yalign 0.5
                                                style "input"
                                        textbutton _("Apply"):
                                            action Function(request_inline_hover_text_color_apply, inline_hover_text_color_draft)
                                        textbutton _("Default"):
                                            action [SetScreenVariable("inline_hover_text_color_draft", "#336600"), Function(request_inline_hover_text_color_apply, "#336600")]

                                    hbox:
                                        spacing 8
                                        for _label, _color in INLINE_HOVER_COLOR_PRESETS:
                                            button:
                                                xsize 34
                                                ysize 24
                                                background Solid(_color)
                                                action [SetScreenVariable("inline_hover_text_color_draft", _color), Function(request_inline_hover_text_color_apply, _color)]
                                                tooltip _label

                hbox:
                    box_wrap True
                    xfill True
                    xmaximum 1140
                    spacing 40

                    vbox:
                        style_prefix "check"
                        spacing 4

                        label _("Skip Behavior"):
                            style "pref_label"

                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            ## -- Sliders + live preview side by side --------------------------
            hbox:
                style_prefix "slider"
                spacing 40

                vbox:

                    label _("Text Size")
                    bar value TextSizeValue()

                    label _("Letter Spacing")
                    bar value LetterSpacingValue()

                    label _("Textbox Opacity")
                    bar value TextboxOpacityValue()

                vbox:
                    label _("Preview")
                    frame:
                        xsize 580
                        xanchor 0.0
                        padding (20, 16, 20, 16)
                        background Transform(Frame("gui/frame_outline.png", gui.frame_borders, tile=gui.frame_tile), matrixcolor=ColorizeMatrix("#ffffff", gui.hover_color))
                        text _("The quick brown fox jumps over the lazy dog.\nPack my box with five dozen liquor jugs."):
                            font current_font()
                            size (33 + (persistent.text_size_offset if persistent.text_size_offset else 0))
                            kerning (persistent.letter_spacing if persistent.letter_spacing else 0)
                            outlines ([(2, "#000000c0", 0, 0)] if persistent.text_outline == "outline" else ([(2, "#00000080", 2, 2)] if persistent.text_outline == "shadow" else []))
                            color gui.text_color
                            line_spacing 6


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                    if h.who:
                        ## If the name already contains a color tag, wrap only the name
                        if "{color=" in h.who:
                            ## Close the name color tag immediately, then add colon and dialogue
                            $ line = h.who + '{/color}: ' + renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        else:
                            $ line = '{color=#006400}' + h.who + '{/color}: ' + renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    else:
                        $ line = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)

                    text line:
                        substitute False
                        xalign 0.0  # left-align
                        yalign 0.0

        if not _history_list:
            label _("The dialogue history is empty.")







## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_name is text:
    xalign 0.0
    textalign 0.0

style history_text is text:
    xalign 0.0
    textalign 0.0


style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

## Start Over confirmation — right-click and escape are intentionally disabled
## so the player cannot accidentally back out of a destructive action.
screen start_over_confirm():

    modal True
    zorder 200
    style_prefix "confirm"

    add "#000000"
    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("This will erase all progress and restart the game. Continue?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action [
                    Hide("start_over_confirm"),
                    Function(start_over_reset),
                    Function(renpy.full_restart)
                ]

                textbutton _("No") action Hide("start_over_confirm")

    ## No key binding here — right-click and escape cannot dismiss this screen.


screen profile_delete_confirm(slot):

    modal True
    zorder 205
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 28

            label _("Delete Profile [slot]? This clears that profile's progress and removes its save slots."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 60

                textbutton _("Delete") action [Function(profile_delete_slot, slot, True), Hide("profile_delete_confirm"), Function(renpy.restart_interaction)]
                textbutton _("Cancel") action Hide("profile_delete_confirm")


screen profile_copy_overwrite_confirm(source_slot, target_slot):

    modal True
    zorder 206
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 28

            label _("Profile [target_slot] is already used. Overwrite it with Profile [source_slot]?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 60

                textbutton _("Overwrite") action [Function(profile_copy_slot, source_slot, target_slot, True, True), Hide("profile_copy_overwrite_confirm"), Function(renpy.restart_interaction)]
                textbutton _("Cancel") action Hide("profile_copy_overwrite_confirm")


screen preference_apply_scope_confirm(pref_key, pref_value):

    modal True
    zorder 205
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 28

            label _("Apply this preference to all profiles or only this profile?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 60

                textbutton _("All Profiles") action Function(apply_preference_scope_choice, pref_key, pref_value, "all")
                textbutton _("Only This Profile") action Function(apply_preference_scope_choice, pref_key, pref_value, "profile")
                textbutton _("Cancel") action Hide("preference_apply_scope_confirm")


screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.0
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground Null()
    selected_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=48, xalign=0.0, yalign=0.5)
    selected_hover_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=48, xalign=0.0, yalign=0.5)

style check_button:
    variant "small"
    foreground Null()
    selected_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=48, xalign=0.0, yalign=0.5)
    selected_hover_foreground Transform(Solid(gui.hover_color), xsize=10, ysize=48, xalign=0.0, yalign=0.5)

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background None

style game_menu_outer_frame:
    variant "small"
    background None

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Solid(gui.hover_color)
    right_bar Solid(gui.hover_muted_color)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Solid(gui.hover_color)
    bottom_bar Solid(gui.hover_muted_color)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Solid(gui.hover_muted_color)
    thumb Solid(gui.hover_color)

style slider_bar:
    variant "small"
    left_bar "gui/horizontal bar filling.png"
    right_bar "gui/horizontal bar empty.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Solid(gui.hover_muted_color)
    thumb Solid(gui.hover_color)

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 210
    xalign 1.0
    ysize 14
    left_bar Frame(Transform("gui/horizontal bar filling.png", crop=(578, 201, 78, 14), matrixcolor=ColorizeMatrix("#000000", gui.hover_color)), 7, 0, 7, 0, tile=False)
    right_bar Frame(Transform("gui/horizontal bar empty.png", crop=(575, 177, 83, 14), matrixcolor=ColorizeMatrix("#000000", "#111111")), 7, 0, 7, 0, tile=False)
    thumb Transform(Solid(Color(gui.hover_color).shade(0.7)), xsize=12, ysize=12)


init python:

    _PRONOUN_DEFAULTS = {
        "date":       {"sub": "she",  "obj": "her",  "pos": "her",   "ref": "herself",   "pred": "hers", "vs": "s"},
        "date_sis":   {"sub": "she",  "obj": "her",  "pos": "her",   "ref": "herself",   "pred": "hers", "vs": "s"},
        "date_dad":   {"sub": "he",   "obj": "him",  "pos": "his",   "ref": "himself",   "pred": "his",  "vs": "s"},
        "date_mom":   {"sub": "she",  "obj": "her",  "pos": "her",   "ref": "herself",   "pred": "hers", "vs": "s"},
        "date_ghost": {"sub": "he",   "obj": "him",  "pos": "his",   "ref": "himself",   "pred": "his",  "vs": "s"},
    }

    _NPC_DEFAULTS = [
        ("date",       "Lilith",  "Lilly"),
        ("date_sis",   "Abigail", "Abby"),
        ("date_dad",   "David",   "Dave"),
        ("date_mom",   "Lila",    "Mom"),
        ("date_ghost", "James",   "Jay"),
    ]

    def set_pronoun_form(npc_var, form_key, value):
        """Write a single pronoun form into the character's pronoun dict."""
        d = _get_pronoun_dict(npc_var)
        d[form_key] = value
        setattr(persistent, npc_var + "_pronouns", d)

    def _get_pronoun_dict(npc_var):
        """Safely retrieve the pronoun dict for a character, handling legacy string values.
        If the stored value is not a dict (None or old string from pre-dict saves),
        the default is written back to persistent so future swaps work correctly.
        If it is a dict but is missing keys (e.g. verb keys added in a later update),
        the missing keys are filled in from defaults so previews always show correctly."""
        stored = getattr(persistent, npc_var + "_pronouns", None)
        defaults = dict(_PRONOUN_DEFAULTS.get(npc_var, {}))
        if isinstance(stored, dict):
            # Merge: defaults first, then stored on top so custom values win.
            # Any keys that exist in defaults but not in stored (e.g. new verb keys)
            # are filled in automatically.
            merged = dict(defaults)
            merged.update(stored)
            return merged
        setattr(persistent, npc_var + "_pronouns", defaults)
        return defaults

    def reset_to_default_names():
        for npc_var, name_d, nick_d in _NPC_DEFAULTS:
            if not getattr(persistent, npc_var, "") or str(getattr(persistent, npc_var, "")).strip() == "":
                setattr(persistent, npc_var, name_d)
            if not getattr(persistent, npc_var + "_nickname", "") or str(getattr(persistent, npc_var + "_nickname", "")).strip() == "":
                setattr(persistent, npc_var + "_nickname", nick_d)
            setattr(persistent, npc_var + "_pronouns", dict(_PRONOUN_DEFAULTS[npc_var]))

    def conj(npc_prefix, singular, plural):
        """Return singular or plural verb form based on the character's grammatical number.
        Uses the stored 'vs' key: 's' = singular (she/he), '' = plural (they).
        Example: conj('date', 'tries', 'try')  →  'tries' or 'try'
        conj('date', 'is',    'are')  →  'is'    or 'are'"""
        vs = getattr(store, npc_prefix + "_vs", "s")
        return singular if vs == "s" else plural

    def updatePronouns():
        """Copy persistent pronoun dicts into shorthand store variables for use in dialogue."""
        # Ensure every pronoun dict is a valid dict before reading
        # (handles saves from before the pronoun system was added, and post-swap None values)
        for npc_var, defaults in _PRONOUN_DEFAULTS.items():
            stored = getattr(persistent, npc_var + "_pronouns", None)
            if not isinstance(stored, dict):
                setattr(persistent, npc_var + "_pronouns", dict(defaults))

        _prefix_map = [
            ("date",       "date"),
            ("date_sis",   "sis"),
            ("date_dad",   "dad"),
            ("date_mom",   "mom"),
            ("date_ghost", "ghost"),
        ]
        for npc_var, prefix in _prefix_map:
            defaults = _PRONOUN_DEFAULTS.get(npc_var, {})
            p = _get_pronoun_dict(npc_var)
            for form in ("sub", "obj", "pos", "ref", "pred", "is", "was", "has", "does", "vs"):
                setattr(store, prefix + "_" + form, p.get(form, defaults.get(form, "")))


screen show_pronoun_input_screen(npc_var, form_key, pronoun_label, pronoun_default):
    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            text f"Enter {pronoun_label}:" size 28
            input:
                default _get_pronoun_dict(npc_var).get(form_key, pronoun_default)
                changed (lambda v, nv=npc_var, fk=form_key: set_pronoun_form(nv, fk, v))
            hbox:
                spacing 10
                textbutton "Save" action [Function(updatePronouns), Hide('show_pronoun_input_screen')]
                textbutton "Cancel" action Hide('show_pronoun_input_screen')

screen show_nickname_input_screen(nickname_var, nickname_default):
    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 10
            text "Enter the new nickname:" size 30

            # Input field for nickname
            input:
                default getattr(persistent, nickname_var, nickname_default)
                changed (lambda value, nickname_var=nickname_var: setattr(persistent, nickname_var, value))

            hbox:
                spacing 10
                textbutton "Save" action Hide('show_nickname_input_screen')
                textbutton "Cancel" action Hide('show_nickname_input_screen')

screen change_names_menu():

    tag menu

    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        xsize 1220
        ysize 780

        vbox:
            spacing 14
            xfill True

            text "Character Info" style "charinfo_title_text" xalign 0.5
            text "Temporary menu for now" style "charinfo_subtitle_text" xalign 0.5

            $ _role_labels = {
                'date': 'Date',
                'date_sis': 'Younger Sibling',
                'date_dad': 'Lost Parent',
                'date_mom': 'Parent',
                'date_ghost': 'Lost Sibling',
            }

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xsize 1180
                ysize 590

                vbox:
                    spacing 16
                    xsize 1140


                    for npc_var, npc_default, nickname_default in _NPC_DEFAULTS:
                        $ _p = _get_pronoun_dict(npc_var)
                        $ _f = _get_family_dict(npc_var)
                        $ _family_defs = _FAMILY_DEFAULTS.get(npc_var, {})
                        $ _current_name = getattr(persistent, npc_var, npc_default)
                        $ _current_nickname = getattr(persistent, npc_var + '_nickname', nickname_default)
                        $ _vs_label = "Singular (she/he)" if _p.get('vs', 's') == 's' else "Plural (they/them)"

                        frame:
                            style "charinfo_card_frame"
                            xfill True

                            vbox:
                                spacing 14

                                hbox:
                                    spacing 24
                                    xfill True
                                    yalign 0.5

                                    vbox:
                                        spacing 4
                                        xfill True
                                        text _role_labels.get(npc_var, npc_var) style "charinfo_role_text"
                                        text _current_name style "charinfo_name_text"
                                        text "Nickname: [_current_nickname]" style "charinfo_nickname_text"

                                    textbutton "Change Pronouns":
                                        style "charinfo_action_button"
                                        action Show("change_pronouns_screen", npc_var=npc_var, npc_label=npc_default)
                                        yalign 0.5

                                hbox:
                                    box_wrap True
                                    spacing 14

                                    frame:
                                        style "charinfo_section_frame"
                                        xsize 520

                                        vbox:
                                            spacing 10
                                            text "Identity" style "charinfo_section_title_text"

                                            hbox:
                                                spacing 12
                                                yalign 0.5
                                                xalign 0.0
                                                text "Name" style "charinfo_label_text"
                                                text "[_current_name]" style "charinfo_value_text"
                                                textbutton "Edit":
                                                    style "charinfo_action_button"
                                                    action Show("show_name_input_screen", npc_var=npc_var, npc_default=npc_default)

                                            hbox:
                                                spacing 12
                                                yalign 0.5
                                                xalign 0.0
                                                text "Nickname" style "charinfo_label_text"
                                                text "[_current_nickname]" style "charinfo_value_text"
                                                textbutton "Edit":
                                                    style "charinfo_action_button"
                                                    action Show("show_nickname_input_screen", nickname_var=npc_var + "_nickname", nickname_default=nickname_default)

                                    frame:
                                        style "charinfo_section_frame"
                                        xsize 590

                                        vbox:
                                            spacing 10
                                            text "Grammar" style "charinfo_section_title_text"

                                            hbox:
                                                spacing 12
                                                yalign 0.5
                                                xalign 0.0
                                                text "Pronouns" style "charinfo_label_text"
                                                text "[_p.get('sub','')] / [_p.get('obj','')] / [_p.get('pos','')] / [_p.get('ref','')] / [_p.get('pred','')]" style "charinfo_value_text" xmaximum 360 layout "subtitle"

                                            hbox:
                                                spacing 12
                                                yalign 0.5
                                                xalign 0.0
                                                text "Verb Form" style "charinfo_label_text"
                                                text "[_vs_label]" style "charinfo_value_text"
                                                textbutton "Change":
                                                    style "charinfo_action_button"
                                                    action Show("change_verbs_screen", npc_var=npc_var, npc_label=npc_default)

                                if _family_defs:
                                    frame:
                                        style "charinfo_section_frame"

                                        vbox:
                                            spacing 8
                                            text "Family Terms" style "charinfo_section_title_text"
                                            for term_key, term_label in _family_defs.items():
                                                hbox:
                                                    spacing 12
                                                    yalign 0.5
                                                    xalign 0.0
                                                    text "[term_key]" style "charinfo_label_text"
                                                    text "[_f.get(term_key, term_label)]" style "charinfo_value_text"
                                                    textbutton "Edit":
                                                        style "charinfo_action_button"
                                                        action Show("show_family_input_screen", npc_var=npc_var, term_key=term_key, term_label=term_key, term_default=term_label)

            hbox:
                spacing 22
                xalign 0.5
                textbutton "Reset to Defaults" action [Function(reset_all_character_defaults), Function(renpy.restart_interaction)] style "menu_button"
                textbutton "Return" action Return() style "menu_button"


style charinfo_card_frame is frame
style charinfo_section_frame is frame
style charinfo_title_text is gui_label_text
style charinfo_subtitle_text is gui_text
style charinfo_role_text is gui_text
style charinfo_name_text is gui_label_text
style charinfo_nickname_text is gui_text
style charinfo_section_title_text is gui_label_text
style charinfo_label_text is gui_text
style charinfo_value_text is gui_text
style charinfo_action_button is button
style charinfo_action_button_text is button_text

style charinfo_card_frame:
    background "#F2ECE0"
    padding (22, 18)
    margin (4, 4)

style charinfo_section_frame:
    background "#FBF8F1"
    padding (14, 12)
    margin (2, 2)

style charinfo_title_text:
    size 34
    color gui.accent_color
    text_align 0.0

style charinfo_subtitle_text:
    size 17
    color "#5C5346"
    text_align 0.0

style charinfo_role_text:
    size 15
    color "#8D5A2B"

style charinfo_name_text:
    size 28
    color "#241B12"

style charinfo_nickname_text:
    size 17
    color "#6B6257"
    italic True

style charinfo_section_title_text:
    size 20
    color "#3B2E20"

style charinfo_label_text:
    size 16
    color "#7A6B59"
    xminimum 130
    yalign 0.5

style charinfo_value_text:
    size 18
    color "#1F1811"
    xalign 0.0
    text_align 0.0
    yalign 0.5
    xminimum 180
    xmaximum 360

style charinfo_action_button:
    properties gui.button_properties("button")
    xminimum 120
    ypadding 6

style charinfo_action_button_text:
    properties gui.button_text_properties("button")


screen change_verbs_screen(npc_var, npc_label):

    tag menu

    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 340

        vbox:
            spacing 20

            text f"Verbs — {npc_label}" size 26 xalign 0.5

            text "Choose verb form:" size 20 xalign 0.5

            hbox:
                spacing 20
                xalign 0.5

                textbutton "Singular (she/he)" action [
                    Function(set_pronoun_form, npc_var, "vs",   "s"),
                    Function(updatePronouns),
                    Return(),
                ]

                textbutton "Plural (they/them)" action [
                    Function(set_pronoun_form, npc_var, "vs",   ""),
                    Function(updatePronouns),
                    Return(),
                ]

            textbutton "Return" action Return() style "menu_button" xalign 0.5 top_margin 8


screen change_pronouns_screen(npc_var, npc_label):

    tag menu

    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500

        vbox:
            spacing 14

            text f"Pronouns — {npc_label}" size 26 xalign 0.5

            for form_key, form_label, form_hint in [
                ("sub",  "Subject",   "e.g. she / he / they"),
                ("obj",  "Object",    "e.g. her / him / them"),
                ("pos",  "Possessive","e.g. her / his / their"),
                ("ref",  "Reflexive", "e.g. herself / himself / themselves"),
                ("pred", "Predicative","e.g. hers / his / theirs"),
            ]:
                $ _p = _get_pronoun_dict(npc_var)

                frame:
                    background "#CCCCCC"
                    padding (10, 8)
                    xfill True

                    hbox:
                        spacing 16
                        xfill True
                        yalign 0.5

                        vbox:
                            yalign 0.5
                            text form_label size 18
                            text form_hint size 14 color "#666666"

                        text f"{_p.get(form_key, '')}" size 20 yalign 0.5 xalign 0.5

                        textbutton "Edit" yalign 0.5 xalign 1.0 action Show("show_pronoun_input_screen", npc_var=npc_var, form_key=form_key, pronoun_label=form_label, pronoun_default=_p.get(form_key, ""))

            textbutton "Return" action Return() style "menu_button" xalign 0.5
    
screen retry_wall():

    tag menu

    # Fullscreen container
    frame:
        xfill True
        yfill True
        background "#000000"

        grid 20 12:
            xfill True
            yfill True

            spacing 10

            # Fill the grid with "retry"
            for i in range(240):
                text "{glitch=50}{color=#ff0000}retry{/color}{/glitch}"
                #text "retry" size 20 color "#ff4444"