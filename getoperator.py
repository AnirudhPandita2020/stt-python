def returnsyntax(args):
    if "operator" in args and len(args) == 8:
        syn = "#Please specify the operator\n"
        return syn
    elif len(args) > 8:
        d = {
            "add": "+",
            "minus":"-",
            "multiply":"*",
            "divide":"/"
        }
        prost = args.split(" ")
        syn = d[prost[1]]
        return syn
