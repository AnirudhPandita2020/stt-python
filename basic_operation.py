from ctypes.wintypes import PUINT
import re
import googlestt
import pyautogui
import forsyn 
import ifelsesyn as ies
import returningsyntax as rs
import getoperator as go
b = 0
list_number = 0
def run():
    global b,list_number
    while True:
        googlestt.main()
        a = googlestt.printtext()
        
        if "import" in a:
            a.lower()
            pyautogui.typewrite(a, 0.0025)
            pyautogui.press("enter")
            return (a)
        
        elif "take" in a:
            pyautogui.typewrite(a[5:len(a)]+ " = input()")
            pyautogui.press("enter")
            return a
    
        elif "characters" in a:
            #characters <variable> <start of the string>
            prost = a.split(" ")
            st = " ".join(prost[2:])
            pyautogui.typewrite(prost[1]+" = '{}'".format(st),0.0025)
            pyautogui.press("right",2)
            pyautogui.press("enter")      
            return (a)
        
        elif "integer input" in a and "variable" in a:
            #integer input variable number
            pyautogui.typewrite(a[23:len(a)]+" = int(input())",0.0025)
            pyautogui.press("enter")
            return (a)
        elif "mapping number input" in a:
            #mapping number input variables distance time
            s = a[31:len(a)]
            s = s.replace(" ",",")
            pyautogui.typewrite(s+" = map(int,input().split())")
            pyautogui.press("enter")
            return (a)
            
        elif "create empty list" in a:
            list_number+=1
            pyautogui.typewrite("l"+str(list_number)+" = []\n",0.0025)
            return a
        elif "create list variable" in a:
            prost = a.split(" ")
            pyautogui.typewrite(prost[3]+" = []\n")  
            return a
        elif "list input variable" in a:
            prost = a.split(" ")
            pyautogui.typewrite(prost[3] + " = list(map(int,input().split()))\n",0.0025)
            return a
        elif "enter" in a:
            pyautogui.press("enter")
            return (a)
        elif "backspace" in a:
            pyautogui.press("backspace")
            return a
        elif "new function" in a:
            b = a[13:len(a)]
            b=b.replace(" ","_")
            pyautogui.typewrite("def "+b+"():",0.0025)
            pyautogui.press("enter")
            pyautogui.typewrite("pass")
            pyautogui.press("enter")
            pyautogui.press("up")
            pyautogui.hotkey("fn","end")
            for i in range(2):
                pyautogui.press("left")
            return (a)


        elif "message" in a:
            pyautogui.typewrite("print('""')",0.0025)
            for i in range(0, 2):
                pyautogui.keyDown("left")
            pyautogui.keyUp("left")
            pyautogui.typewrite(a[8:len(a)],0.0025)
            for i in range(0,2):
                pyautogui.keyDown("right")
            pyautogui.keyUp("right")
            pyautogui.press("enter")
            return (a)

        elif "output" in a and "variable" in a:
            syn = str(a[16:len(a)].lower())
            pyautogui.typewrite("print({})".format(syn),0.0025)
            pyautogui.hold("left")
            pyautogui.press("enter")
            return (a)

        elif "start" in a or "run" in a:
            pyautogui.hotkey("ctrl", "f5")
            return (a)
        
        elif "initial variable" in a:
            pyautogui.typewrite(a[17:len(a)]+"=0",0.0025)
            pyautogui.press("enter")
            return (a)
        
        elif "value" in a:
            prost = a.split(" ")
            if prost[2] =="equals":
                prost[2] = "="
            pyautogui.typewrite(" ".join(prost[1:]),0.0025)
            pyautogui.press("enter")
            return a
        
        elif "above" in a:
            pyautogui.hold("left")
            pyautogui.press("up")
            return (a)
        
        elif "line number" in a or "line Number" in a or "Line number" in a:
            pyautogui.hotkey("ctrl","g")
            pyautogui.typewrite(a[11:len(a)],0.0025)
            pyautogui.press("enter")
            b = int(a[11:len(a)])
            return (a)
        elif "return" in a:
            syn = rs.returnsyntax(a)
            pyautogui.typewrite(syn,0.0025)
            return a
        
        elif "power variable" in a:
            pyautogui.typewrite(a[15:20]+"**"+a[27:])
            pyautogui.hold("left")
            return (a)
        elif "for loop" in a:
            s = forsyn.returnsyntax(a)
            if "in range():" in s:
                pyautogui.typewrite(s,0.0025)
                pyautogui.press("enter")
                pyautogui.press("up",1)
                pyautogui.hotkey("fn","end")
                pyautogui.press("left",2)
                return (a)
            elif "in :" in s:
                pyautogui.typewrite(s,0.0025)
                pyautogui.press("enter")
                pyautogui.press("up",1)
                pyautogui.hotkey("fn","end")
                pyautogui.press("left",1)
                return (a)
        
        elif "if" in a or "else if" in a or "otherwise" in a:
             s = ies.returnsyntax(a)
             pyautogui.typewrite(s,0.0025)
             return a
        elif "undo" in a:
            pyautogui.hotkey("ctrl","z")
            return (a)
        elif "redo" in a:
            pyautogui.hotkey("ctrl","y")
            return (a)
        elif "details" in a:
            pyautogui.typewrite("#THIS IS MADE BY ANIRUDH PANDITA\n#USN 1NH19CS018 NHCE BLR!!!\n",0.0025)   
            return (a)
        elif "comment" in a:
            pyautogui.hotkey("ctrl","/")
            return (a)
        elif "end of line" in a:
            pyautogui.hotkey("fn","end")
            return (a)
        elif "remove" in a:
            pyautogui.hotkey("ctrl","shift","k")
            pyautogui.hotkey("ctrl","g")
            if b == 1:
                pyautogui.typewrite(str(b))
                pyautogui.press("enter",2,0.0025)
                pyautogui.press("up")
                
            else:
                pyautogui.typewrite(str(b-1))
                pyautogui.press("enter")
                pyautogui.hotkey("fn","end")
                pyautogui.press("enter")
            return (a)
        elif "argument" in a and a.count("pass") == 0 and a.count("range") == 0:
            b = a[9:len(a)]
            b = b.replace(" ",",")
            pyautogui.typewrite(b)
            pyautogui.press("right",2)
            pyautogui.press("enter")
            return (a)
        elif "operator" in a:
            syn = go.returnsyntax(a)
            pyautogui.typewrite(syn,0.0025)
            return a
        elif "call function" in a:
            b = a[14:len(a)]
            b=b.replace(" ","_")
            pyautogui.typewrite(b+"()",0.0025)
            pyautogui.press("left")
            return (a)
        elif "pass function argument" in a and a.count("pass") == 1:
            prost = a.split(" ")
            syn = "".join(prost[3:])
            pyautogui.typewrite(syn,0.0025)
            pyautogui.press("right")
            pyautogui.press("enter")
            return a
        elif "print function" in a and a.count("print") == 1:
            prost = a.split(" ")
            syn = prost[2]+"()"
            pyautogui.typewrite("print({})".format(syn))
            pyautogui.press("left",2)
            return a
        elif "range argument" in a and a.count("range") == 1:
            prost = a.split(" ")
            #range argument begin 1 end number
            syn = prost[3]+","+prost[5]
            pyautogui.typewrite(syn,0.0025)
            pyautogui.press("right",2)
            pyautogui.press("enter")
            return a
        elif "loop variable" in a and a.count("loop") == 1:
            prost = a.split(" ")
            syn = str(prost[2].tolower())
            pyautogui.typewrite(syn,0.0025)
            pyautogui.press("enter")
            return a
        elif "quit" in a or "exit" in a or "pause" in a:
            return (a)


'''
details
main funtion
line'''