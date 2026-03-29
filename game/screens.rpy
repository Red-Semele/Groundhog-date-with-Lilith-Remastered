screen show_name_input_screen(npc_var, npc_default):
    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 10
            text f"Enter Name:" size 28
            input:
                default getattr(persistent, npc_var, npc_default)
                changed (lambda v, nv=npc_var: setattr(persistent, nv, v))
            hbox:
                spacing 10
                textbutton "Save" action Hide('show_name_input_screen')
                textbutton "Cancel" action Hide('show_name_input_screen')
init python:
    def reset_all_character_defaults():
        for npc_var, name_d, nick_d in _NPC_DEFAULTS:
            setattr(persistent, npc_var, name_d)
            setattr(persistent, npc_var + "_nickname", nick_d)
            setattr(persistent, npc_var + "_pronouns", dict(_PRONOUN_DEFAULTS.get(npc_var, {})))
            setattr(persistent, npc_var + "_family_terms", dict(_FAMILY_DEFAULTS.get(npc_var, {})))
        updatePronouns()
        updateFamilyTerms()

    # --- FAMILY TERM SYSTEM ---
    _FAMILY_DEFAULTS = {
        "date":       {"sibling (short)": "sis", "sibling": "sister", "child": "daughter"},
        "date_sis":   {"sibling (short)": "sis", "sibling": "sister", "child": "daughter"},
        "date_dad":   {"parent (short)": "dad", "parent": "father"},
        "date_mom":   {"parent (short)": "mom", "parent": "mother"},
        "date_ghost": {"sibling (short)": "bro", "sibling": "brother", "child": "son"},
    }

    def set_family_term(npc_var, term_key, value):
        d = _get_family_dict(npc_var)
        d[term_key] = value
        setattr(persistent, npc_var + "_family_terms", d)

    def _get_family_dict(npc_var):
        stored = getattr(persistent, npc_var + "_family_terms", None)
        defaults = dict(_FAMILY_DEFAULTS.get(npc_var, {}))
        if isinstance(stored, dict):
            merged = dict(defaults)
            merged.update(stored)
            return merged
        setattr(persistent, npc_var + "_family_terms", defaults)
        return defaults

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

if persistent.canSave == False:
    define _game_menu_screen = "preferences"
define config.auto_load = "quitsave"


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
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


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

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        text what id "what"

    ## Namebox — rendered outside the main textbox window so it can sit
    ## as its own floating rectangle above it, connected by a slight overlap.
    if who is not None:
        window:
            id "namebox"
            style "namebox"
            text who id "who"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


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

    background At(Image("gui/textbox.png", xalign=0.5, yalign=1.0), Transform(alpha=gui.textbox_alpha))

style namebox:
    ## Flush to the left edge of the screen.
    xpos 0
    xanchor 0.0
    xminimum 180
    ## yanchor 1.0 + yalign 1.0 + yoffset = -gui.textbox_height puts the
    ## bottom of the namebox exactly at the top of the textbox — touching, not overlapping.
    yanchor 1.0
    yalign 1.0
    yoffset -(gui.textbox_height)

    background Frame(Solid(gui.accent_color), Borders(0, 0, 0, 0))
    padding (20, 10, 20, 10)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    text_align 0.5
    yalign 0.5
    color "#ffffff"

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

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
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    default max_visible = 5

    ## Tooltip captured reactively every interaction so the notecard updates live.
    $ tt = GetTooltip()

    ## Count only items with a live action — insensitive/disabled items
    ## (passed when config.menu_include_disabled is True) are excluded so
    ## a menu that looks like 2 choices isn't mis-classified as 3+.
    $ _active = [i for i in items if i.action]

    ## Scroll threshold: grid mode caps at 4 items (5+ scroll); default uses max_visible.
    $ _scroll_at = 4 if persistent.grid_choices else max_visible

    if len(_active) > _scroll_at:
        # ── Scrollable version — UNTOUCHED ─────────────────────────────
        window:
            background None
            xalign 0.5
            yalign 0.5
            

            viewport:
                draggable True
                mousewheel True
                pagekeys True
                scrollbars "vertical"
                xalign 0.5
                yalign 0.5
                xsize 1200  
                ymaximum 300 

                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5
                    for i in items:
                        textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=("{color=#7BCF7D}%s" % persistent.name), what=__(i.caption))]

    elif len(_active) == 2 or not persistent.grid_choices:
        # ── Default stacked layout (2 choices, or compact grid turned off) ─
        vbox:
            style "grid_choice_vbox"
            for i in items:
                textbutton i.caption action [i.action, Function(narrator.add_history, kind="adv", who=("{color=#7BCF7D}%s" % persistent.name), what=__(i.caption))]

    else:
        ## ── Compact grid layout (3–4 items, grid mode on) ──────────────
        vbox:
            style "grid_choice_vbox"
            if len(_active) == 3:
                # Row 1: first 2 side by side
                hbox:
                    spacing 30
                    xalign 0.5
                    for i in _active[:2]:
                        $ _short = truncate_choice(i.caption)
                        textbutton _short:
                            style "grid_choice_button"
                            tooltip (i.caption if _short != i.caption else "")
                            action [i.action, Function(narrator.add_history, kind="adv", who=("{color=#7BCF7D}%s" % persistent.name), what=__(i.caption))]
                # Row 2: last choice centered
                hbox:
                    spacing 30
                    xalign 0.5
                    for i in _active[2:]:
                        $ _short = truncate_choice(i.caption)
                        textbutton _short:
                            style "grid_choice_button"
                            tooltip (i.caption if _short != i.caption else "")
                            action [i.action, Function(narrator.add_history, kind="adv", who=("{color=#7BCF7D}%s" % persistent.name), what=__(i.caption))]

            else:
                # 4 items: 2×2 grid
                hbox:
                    spacing 30
                    xalign 0.5
                    for i in _active[:2]:
                        $ _short = truncate_choice(i.caption)
                        textbutton _short:
                            style "grid_choice_button"
                            tooltip (i.caption if _short != i.caption else "")
                            action [i.action, Function(narrator.add_history, kind="adv", who=("{color=#7BCF7D}%s" % persistent.name), what=__(i.caption))]
                hbox:
                    spacing 30
                    xalign 0.5
                    for i in _active[2:]:
                        $ _short = truncate_choice(i.caption)
                        textbutton _short:
                            style "grid_choice_button"
                            tooltip (i.caption if _short != i.caption else "")
                            action [i.action, Function(narrator.add_history, kind="adv", who=("{color=#7BCF7D}%s" % persistent.name), what=__(i.caption))]

    ## ── Tooltip notecard — yellow card with full text on hover ─────────────
    if tt and persistent.grid_choices and 2 < len(_active) <= 4:
        frame:
            style "notecard_frame"
            xalign 0.5
            yalign 0.90 # Slightly lower to ensure 30px gap
            xmaximum 820
            text tt:
                style "notecard_text"



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
    text_align 0.5
    xalign 0.5

## Tooltip notecard — yellow card showing full choice text on hover
style notecard_frame is frame:
    background Frame(Solid("#f5e179"), Borders(12, 10, 12, 10))
    padding (20, 14, 20, 14)
    xalign 0.5

style notecard_text:
    color "#1a1000"
    text_align 0.5
    size gui.text_size


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            if persistent.canSave:
                textbutton _("Save") action ShowMenu('save')
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

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

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")
            if persistent.canSave:
                textbutton _("Save") action ShowMenu("save")
        if persistent.canSave:
            textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")
        
        textbutton _("Start Over") action Show("start_over_confirm")



        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


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

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    ## Show an update notification banner if a newer version is available.
    use update_notification

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

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

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

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

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

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

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

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
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

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
            textbutton _("Change Character Info") action Show("change_names_menu")
            textbutton _("Change Your Name") action [SetVariable("from_menu", True), Start("nameSelect")]
            


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
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


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

    ## Rebuild styles once when the player navigates away so gui.rebuild()
    ## never fires mid-drag (which would kill the drag gesture).
    on "hide"     action Function(apply_text_size_current)
    on "replaced" action Function(apply_text_size_current)

    use game_menu(_("Text Appearance"), scroll="viewport"):

        vbox:

            ## ── Dropdowns row ────────────────────────────────────────────────
            hbox:
                box_wrap True
                spacing 40
                xoffset 60

                ## Font dropdown
                vbox:
                    spacing 4

                    label _("Font"):
                        style "pref_label"

                    ## Header button showing the active font name + arrow.
                    textbutton ("[current_font().replace('-Regular','').replace('-',' ').replace('.ttf','').replace('.otf','')]  [u'▲' if font_open else u'▼']"):
                        action ToggleLocalVariable("font_open")
                        style "pref_label_text"
                        ypadding 6

                    ## Options — only shown when open.
                    if font_open:
                        frame:
                            padding (8, 6, 8, 6)
                            vbox:
                                style_prefix "radio"
                                textbutton _("Default (DejaVu)"):
                                    action [SetFont("DejaVuSans.ttf"), SetLocalVariable("font_open", False)]
                                    text_font "DejaVuSans.ttf"
                                textbutton _("Pacifico"):
                                    action [SetFont("Pacifico-Regular.ttf"), SetLocalVariable("font_open", False)]
                                    text_font "Pacifico-Regular.ttf"
                                textbutton _("Indie Flower"):
                                    action [SetFont("IndieFlower-Regular.ttf"), SetLocalVariable("font_open", False)]
                                    text_font "IndieFlower-Regular.ttf"
                                textbutton _("Shadows Into Light"):
                                    action [SetFont("ShadowsIntoLight-Regular.ttf"), SetLocalVariable("font_open", False)]
                                    text_font "ShadowsIntoLight-Regular.ttf"

                ## Custom Font dropdown — only shown when custom fonts are present.
                if CUSTOM_FONTS:
                    vbox:
                        spacing 4

                        label _("Custom Font"):
                            style "pref_label"

                        textbutton ("[current_font().replace('-Regular','').replace('-',' ').replace('.ttf','').replace('.otf','').split('/')[-1] if current_font().startswith('custom_fonts/') else 'None selected']  [u'▲' if customfont_open else u'▼']"):
                            action ToggleLocalVariable("customfont_open")
                            style "pref_label_text"
                            ypadding 6

                        if customfont_open:
                            frame:
                                padding (8, 6, 8, 6)
                                vbox:
                                    style_prefix "radio"
                                    for _cname, _cfile in CUSTOM_FONTS:
                                        textbutton _(_cname):
                                            action [SetFont(_cfile), SetLocalVariable("customfont_open", False)]
                                            text_font _cfile

                ## Text Outline dropdown
                vbox:
                    spacing 4

                    label _("Text Outline"):
                        style "pref_label"

                    textbutton ("[persistent.text_outline.capitalize()]  [u'▲' if outline_open else u'▼']"):
                        action ToggleLocalVariable("outline_open")
                        style "pref_label_text"
                        ypadding 6

                    if outline_open:
                        frame:
                            padding (8, 6, 8, 6)
                            vbox:
                                style_prefix "radio"
                                textbutton _("None"):
                                    action [SetTextOutline("none"),    SetLocalVariable("outline_open", False)]
                                textbutton _("Outline"):
                                    action [SetTextOutline("outline"), SetLocalVariable("outline_open", False)]
                                textbutton _("Shadow"):
                                    action [SetTextOutline("shadow"),  SetLocalVariable("outline_open", False)]

            null height (4 * gui.pref_spacing)

            ## ── Sliders + live preview side by side ──────────────────────────
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
                        background At(Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile), Transform(alpha=(persistent.textbox_opacity * 0.01 if persistent.textbox_opacity is not None else 1.0)))
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
                    Function(lambda: setattr(persistent, "firstboot", None)),
                    Function(renpy.full_restart)
                ]

                textbutton _("No") action Hide("start_over_confirm")

    ## No key binding here — right-click and escape cannot dismiss this screen.


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
    text_align 0.5
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
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

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
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

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
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


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
        xsize 1150
        ysize 720

        vbox:
            spacing 8

            text "Change Character info" size 26 xalign 0.5

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xsize 1110
                ysize 620

                vbox:
                    spacing 10
                    xsize 1090


                    for npc_var, npc_default, nickname_default in _NPC_DEFAULTS:
                        $ _p = _get_pronoun_dict(npc_var)
                        $ _f = _get_family_dict(npc_var)
                        $ _family_defs = _FAMILY_DEFAULTS.get(npc_var, {})

                        frame:
                            background "#CCCCCC"
                            padding (12, 10)
                            margin (4, 4)
                            xfill True

                            vbox:
                                spacing 6

                                # Label for the character section
                                $ _role_labels = {
                                    'date': 'Date',
                                    'date_sis': 'Younger Sibling',
                                    'date_dad': 'Lost Parent',
                                    'date_mom': 'Parent',
                                    'date_ghost': 'Lost Sibling',
                                }
                                text _role_labels.get(npc_var, npc_var) size 20

                                ## Name + Nickname on one row
                                hbox:
                                    spacing 30
                                    xfill True

                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text f"Name: {getattr(persistent, npc_var, npc_default)}" yalign 0.5 size 18
                                        textbutton "Edit" yalign 0.5 action Show("show_name_input_screen", npc_var=npc_var, npc_default=npc_default)

                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text f"Nickname: {getattr(persistent, npc_var + '_nickname', nickname_default)}" yalign 0.5 size 18
                                        textbutton "Edit" yalign 0.5 action Show("show_nickname_input_screen", nickname_var=npc_var + "_nickname", nickname_default=nickname_default)

                                ## Pronoun preview + button
                                hbox:
                                    spacing 16
                                    yalign 0.5
                                    text f"Pronouns: {_p.get('sub','')} / {_p.get('obj','')} / {_p.get('pos','')} / {_p.get('ref','')} / {_p.get('pred','')}" yalign 0.5 size 17
                                    textbutton "Change Pronouns" yalign 0.5 action Show("change_pronouns_screen", npc_var=npc_var, npc_label=npc_default)

                                ## Verb singular/plural toggle
                                hbox:
                                    spacing 16
                                    yalign 0.5
                                    $ _vs_label = "Singular (she/he)" if _p.get('vs', 's') == 's' else "Plural (they/them)"
                                    text f"Verbs: {_vs_label}" yalign 0.5 size 17
                                    textbutton "Change Verbs" yalign 0.5 action Show("change_verbs_screen", npc_var=npc_var, npc_label=npc_default)

                                ## Family terms preview + edit buttons
                                if _family_defs:
                                    frame:
                                        background "#EEEEEE"
                                        padding (8, 6)
                                        margin (4, 2)
                                        vbox:
                                            spacing 4
                                            text "Family Terms:" size 16 color "#444"
                                            for term_key, term_label in _family_defs.items():
                                                hbox:
                                                    spacing 8
                                                    yalign 0.5
                                                    text f"{term_key}: {_f.get(term_key, term_label)}" yalign 0.5 size 15
                                                    textbutton "Edit" yalign 0.5 action Show("show_family_input_screen", npc_var=npc_var, term_key=term_key, term_label=term_key, term_default=term_label)

            hbox:
                spacing 16
                xalign 0.5
                textbutton "Reset to Defaults" action [Function(reset_all_character_defaults), Function(renpy.restart_interaction)] style "menu_button"
                textbutton "Return" action Return() style "menu_button"


screen change_verbs_screen(npc_var, npc_label):

    tag menu

    frame:
        style_prefix "menu"
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 280

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

            textbutton "Return" action Return() style "menu_button" xalign 0.5


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

