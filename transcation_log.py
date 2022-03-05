from tkinter import *
import forsyn 
from tkinter.ttk import *
import pyautogui
from tkinter import filedialog
import threading
import time
b = 0
path = ""
def run():
    time.sleep(5)
    global b,path
    with open(path,"r") as f:
        c = f.readlines()
    li =[]
    for p in c:
        s = str(p.replace("\n",""))
        li.append(s)
    print(li)
    for a in li:
        print(a)
        if "import" in a:
            a.lower()
            pyautogui.typewrite(a, 0.0025)
            pyautogui.press("enter")
            


        elif "enter" in a:
            pyautogui.press("enter")
            

        elif "new function" in a:
            b = a[13:len(a)]
            b=b.replace(" ","_")
            pyautogui.typewrite("def "+b+"():",0.0025)
            pyautogui.press("enter")
            pyautogui.typewrite("pass")
            pyautogui.press("enter")
            

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
            

        elif "output" in a and "variable" in a:
            pyautogui.typewrite("print({})".format(a[16:len(a)]),0.0025)
            pyautogui.hold("left")
            pyautogui.press("enter")
            

        elif "start" in a or "run" in a:
            pyautogui.hotkey("ctrl", "f5")
            
        
        elif "initial variable" in a:
            pyautogui.typewrite(a[17:len(a)]+"=0",0.0025)
            pyautogui.press("enter")
            
        
        elif "value" in a:
            b = a[6:len(a)].lower()
            pyautogui.typewrite(b,0.0025)
            pyautogui.hold("left")
            pyautogui.press("enter")
            
        
        elif "above" in a:
            pyautogui.hold("left")
            pyautogui.press("up")
            
        
        elif "line number" in a or "line Number" in a or "Line number" in a:
            pyautogui.hotkey("ctrl","g")
            pyautogui.typewrite(a[11:len(a)],0.0025)
            pyautogui.press("enter")
            b = int(a[11:len(a)])
            
        elif "multiplies" in a and "return" in a:
            pyautogui.typewrite("return "+a[7:14]+"*factorial(number-1)",0.0025)
            
        
        elif "power variable" in a:
            pyautogui.typewrite(a[15:20]+"**"+a[27:])
            pyautogui.hold("left")
            
        elif "for loop" in a:
            s = forsyn.returnsyntax(a)
            if "in range():" in s:
                pyautogui.typewrite(s,0.0025)
                pyautogui.press("left")
                pyautogui.press("left")
                
            elif "in :" in s:
                pyautogui.typewrite(s)
                pyautogui.press("left")
                
        elif "undo" in a:
            pyautogui.hotkey("ctrl","z")
            
        elif "redo" in a:
            pyautogui.hotkey("ctrl","y")
            
        elif "details" in a:
            pyautogui.typewrite("#THIS IS MADE BY ANIRUDH PANDITA\n#USN 1NH19CS018 NHCE BLR!!!\n",0.0025)   
            
        elif "comment" in a:
            pyautogui.hotkey("ctrl","/")
            
        elif "end of line" in a:
            pyautogui.hotkey("fn","end")
            
        elif "remove" in a:
            pyautogui.hotkey("ctrl","shift","k")
            pyautogui.hotkey("ctrl","g")
            pyautogui.typewrite(str(b-1))
            pyautogui.press("enter")
            pyautogui.hotkey("fn","end")
            pyautogui.press("enter")
            
        elif "argument" in a:
            b = a[9:len(a)]
            b = b.replace(" ",",")
            pyautogui.typewrite(b)
            pyautogui.press("right",2)
            pyautogui.press("enter")
            
        elif "quit" in a or "exit" in a or "pause" in a:
            return

def tr():
    global path
    path = filedialog.askopenfilename(title = "Select your Transcation log",filetypes=(("text files","*.txt"),("all files","*.*")))
    run()
tr()
