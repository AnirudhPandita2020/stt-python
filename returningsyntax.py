def returnsyntax(args):
    if args == "return" and len(args) == 6:
        syn = "return\n"
        return syn
    elif len(args) > 6 and "true" in args or "false" in args:
        prost = args.split(" ")
        if prost[1] == "true":
            syn  = "return true\n"
            return syn
        else:
            syn = "return false\n"
            return syn
    else:
        prost = args.split(" ")
        if prost[1].isnumeric():
            syn = "return "+prost[1]+"\n"
            return syn
        else:
            syn = "return " + prost[1]
            return syn
            