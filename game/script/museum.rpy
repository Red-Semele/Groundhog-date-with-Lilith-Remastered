screen fanart_gallery(img_path):
    vbox:
        spacing 2
        xalign 0.5
        yalign 0.20
        frame:
            background Solid("#d4af37") # gold color
            padding (20, 20, 20, 20)
            add Transform(img_path, fit="contain", xysize=(900,600)) xalign 0.5 yalign 0.5

label gallery:
    n "You find yourself in a small room tucked away somewhere between loops."
    n "The walls are lined with old monitors, each one displaying something familiar yet unfinished."
    n "A plaque on the wall reads: {i}Where it all began.{/i}"

    label gallery_menu:
        menu:
            "View a random fanart":
                jump gallery_fanart_random
            "Read a random fanwriting":
                jump gallery_fanwriting_random
            "Prototype 1 GdwL1":
                $ launch_quest_game("GdwL1.quest")
                n "The game launches in a separate window. Come back whenever you're done."
                jump gallery_menu
            "Prototype 2 GdwL2":
                $ launch_quest_game("GdwL2.quest")
                n "The game launches in a separate window. Come back whenever you're done."
                jump gallery_menu
            "Prototype 4 GdwL4":
                $ launch_quest_game("GdwL4.quest")
                n "The game launches in a separate window. Come back whenever you're done."
                jump gallery_menu
            "Leave the gallery.":
                pass

    return

# Utility to list files in a folder (requires Ren'Py 7.4+)
init python:
    import os
    import re
    def show_commentary_lines(commentary_lines):
        import renpy
        import re
        for line in commentary_lines:
            m = re.match(r'([a-zA-Z0-9_]+)\s+"(.*)"', line)
            if m:
                who, what = m.group(1), m.group(2)
                renpy.exports.say(eval(who), what)
            else:
                renpy.exports.say(n, line)
    def read_commentary_lines(path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            return [line.strip() for line in content.splitlines() if line.strip()]
        return None
    def get_fanart_files(debug=False):
        try:
            folder = os.path.join(config.gamedir, "gallery", "fanart")
            files = os.listdir(folder)
            images = [f for f in files if f.lower().endswith(('.png','.jpg','.jpeg','.webp'))]
            if debug:
                return files, images
            return images
        except Exception:
            if debug:
                return [], []
            return []
    def get_fanwriting_files():
        try:
            folder = renpy.loader.transfn("gallery/fanwriting")
            files = os.listdir(folder)
            texts = [f for f in files if f.lower().endswith('.txt') and not f.endswith('_comment.txt')]
            return texts
        except Exception:
            return []

label gallery_fanart_random:
    if not hasattr(store, 'last_fanart'):
        $ last_fanart = None
    $ files, fanart_files = get_fanart_files(debug=True)
    if not fanart_files:
        n "There is no fanart in the gallery yet. Raw files: [files] | Filtered images: [fanart_files]"
        $ last_fanart = None
        jump gallery_menu
    $ available = [f for f in fanart_files if f != last_fanart] if last_fanart and len(fanart_files) > 1 else fanart_files
    $ chosen = renpy.random.choice(available)
    $ last_fanart = chosen
    $ base = os.path.splitext(chosen)[0]
    python:
        import os
        comment_path = os.path.join(config.gamedir, "gallery", "fanart", f"{base}_comment.txt")
        commentary_lines = read_commentary_lines(comment_path)
    scene black
    $ max_width = 700
    $ max_height = 500
    show screen fanart_gallery("gallery/fanart/" + chosen)
    if commentary_lines:
        $ show_commentary_lines(commentary_lines)
    else:
        n "(No commentary for this piece.)"
    menu:
        "See another fanart":
            jump gallery_fanart_random
        "Back to gallery menu":
            $ last_fanart = None
            jump gallery_menu

label gallery_fanwriting_random:
    $ fanwriting_files = get_fanwriting_files()
    if not fanwriting_files:
        n "There is no fanwriting in the gallery yet."
        jump gallery_menu
    $ chosen = renpy.random.choice(fanwriting_files)
    $ base = os.path.splitext(chosen)[0]
    $ text_path = "gallery/fanwriting/" + chosen
    $ comment = get_commentary('fanwriting', base)
    $ story = renpy.file(text_path).read().decode('utf-8')
    n "[story]"
    if comment:
        n "{i}[comment]{/i}"
    menu:
        "Read another fanwriting":
            jump gallery_fanwriting_random
        "Back to gallery menu":
            jump gallery_menu

label test_fanart_folder:
    $ import os
    $ folder = renpy.loader.transfn('gallery/fanart')
    $ files = os.listdir(folder)
    n "Direct folder test: [files]"
    return
