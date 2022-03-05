"""Generates the if else statements"""

def returnsyntax(args):
    if "if" in args and args.count("else") == 0:
        if len(args) == 2:
            s = "if"
            return s
        else:
            # 
            prost = args.split(" ")
            if len(prost) == 5 and (" ".join(prost[2:4]) != "not in" or prost[2] == "in") :
                relational_operator = " ".join(prost[2:4])
                if prost[4] == "zero":
                    prost[4] = str(0)
                d = {
                    "less than":"<",
                    "greater than":">",
                    "equal to":"==",
                    
                }
                relation_type = d[relational_operator]
                syn = "if "+prost[1]+" "+relation_type+" "+prost[4]+":\n"
                return syn
            
            elif len(prost) == 6 and (" ".join(prost[2:5]) != "not in" or prost[2] == "in"):
                #if number greater than equal zero
                relational_operator = " ".join(prost[2:5])
                if prost[5] == "zero":
                    prost[5] =str(0)
                d = {
                    "less than equal":"<=",
                    "greater than equal":">=",
                    "not equal to":"!="
                }
                relation_type = d[relational_operator]
                syn = "if "+prost[1]+" "+relation_type+" "+prost[5]+":\n"
                return syn
            #if number not in l1
            elif " ".join(prost[2:4]) == "not in":
                syn = "if "+prost[1]+" not in "+prost[4]+":\n"
                return syn
            #if number in l1
            elif prost[2] == "in":
                syn = "if "+prost[1]+" in "+prost[3]+":\n"
                return syn
        
    elif "else if" in args and args.count("else") == 1:
        if len(args) == 6:
            return "elif"
        else:
            #else if number greater than 0
            prost = args.split(" ")
            if len(prost) == 6:
                relational_operator = " ".join(prost[3:5])
                if prost[5] == "zero":
                    prost[5] = str(0)
                d = {
                    "less than":"<",
                    "greater than":">",
                    "equal to":"=="
                }
                relation_type = d[relational_operator]
                syn = "elif "+prost[2]+" "+relation_type+" "+prost[5]+":\n"
                return syn
            else:
                #else if number greater than equal 0
                relational_operator = " ".join(prost[2:6])
                if prost[6] == "zero":
                    prost[6] =str(0)
                d = {
                    "less than equal":"<=",
                    "greater than equal":">=",
                    "not equal to":"!="
                }
                relation_type = d[relational_operator]
                syn = "elif "+prost[2]+" "+relation_type+" "+prost[6]+":\n"
                return syn
    elif "otherwise" in args:
        syn = "else:\n"
        return syn


