init python:
    import builtins
    import renpy.store as rstore

    _SEE_ANY = object()

    # Type see("variable") in the console.
    # Optional filters:
    # see(kind="true")
    # see(kind="false")
    # see(kind="none")
    # see(kind="number")
    # see(kind="string")
    # see(value=123)
    def see(searchTxt="", kind=None, value=_SEE_ANY, searchDir=None):
        if searchDir is None:
            searchDir = vars(rstore)

        searchTxt = (searchTxt or "").lower()
        kind = (kind or "").lower()

        def matches_value(itm_value):
            if value is not _SEE_ANY:
                return itm_value == value

            if kind == "true":
                return itm_value is True
            if kind == "false":
                return itm_value is False
            if kind == "none":
                return itm_value is None
            if kind == "number":
                return isinstance(itm_value, (int, float)) and not isinstance(itm_value, bool)
            if kind == "string":
                return isinstance(itm_value, str)

            return True

        items = []

        for varname in sorted(searchDir):
            if searchTxt and searchTxt not in varname.lower():
                continue

            itm_value = searchDir[varname]

            if not matches_value(itm_value):
                continue

            items.append((varname, itm_value))

        for varname, itm_value in items:
            print(varname, " = ", repr(itm_value))

        if not items:
            print("No matches.")

    # Make the helper available from the console without a prefix.
    rstore.see = see
    builtins.see = see