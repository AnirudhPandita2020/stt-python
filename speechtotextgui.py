from tkinter import Menu, PhotoImage, Tk, Toplevel, ttk
from tkinter.constants import END
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector as db
import time
import basic_operation as bo
import testing_db_command as tdb
import user_db as ud
import concurrent.futures
import threading
from tkinter import filedialog
import pyautogui
import forsyn
import returningsyntax as rs
import getoperator as go
import ifelsesyn as ies
records= []
b = 0
path =""
list_number = 0
def get_output():
    global records
    while True:
        with concurrent.futures.ThreadPoolExecutor() as ex:
            f = ex.submit(bo.run)
            l2['text'] = "You said:"+f.result()
            records.append(f.result())
            if f.result() != "pause":
                continue
            else:
                start['text'] = "Press here to start listening"
                l2['text'] = "You said:"
                return


def start_listening():
    start['text'] = "Say Pause to stop listening!!"
    time.sleep(1)
    t1 = threading.Thread(target=get_output)
    t1.start()


def get_output_db():
    while True:
        with concurrent.futures.ThreadPoolExecutor() as ex:
            f = ex.submit(tdb.run)
            l2['text'] = "ADDED CODE SNIPPET:"+f.result()
            if f.result() != "pause":
                continue
            else:
                start_db['text'] = "Enter the database mode to retrive the snippet!!"
                l2['text'] = "You said:"
                return


def start_listening_db():
    start_db['text'] = "SAY STOP TO COME OUT OF DB MODE!!"
    time.sleep(1)
    t1 = threading.Thread(target=get_output_db)
    t1.start()


def get_user_db():
    while True:
        with concurrent.futures.ThreadPoolExecutor() as ex:
            f = ex.submit(ud.run)
            l2['text'] = "ADDED CODE SNIPPET:"+f.result()
            if f.result() != "pause":
                continue
            else:
                start_user_db['text'] = "Enter the user mode to access your snippets!!"
                l2['text'] = "You said:"
                return


def start_listening_user():
    start_user_db['text'] = "SAY PAUSE TO COME OUT!!"
    time.sleep(1)
    t1 = threading.Thread(target=get_user_db)
    t1.start()


def add():
    a = e.get()
    b = e1.get()
    if a == b or (a == "" or b == ""):
        messagebox.showerror("ERROR","The command and the expression cant be same or empty!!")
        return
    else:
        e.delete(0, END)
        e1.delete(0, END)
        mydb = db.connect(
            host="127.0.0.1",
            user="root",
            password="Kuld1972poon",
            database="python"
        )
        b = b.replace("\\n", "_")
        b = b.replace("\\b","-")
        cursor = mydb.cursor()
        sql = "insert into user_commands values(%s,%s)"
        val = (a, b)
        cursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo(
            "SUCCESS", "The Snippets has been added to successfully.\nTry saying the following command:{}".format(a))

def our_command():
    global e,e1
    root1 = Tk()
    e = Entry(root1, width=50)
    e1 = Entry(root1, width=50)
    root1.title("Add your Snippets")
    root1.geometry("500x300")
    l1 = Label(root1,text = "Command:")
    l2 = Label(root1,text = "Expression:")
    add_snip = Button(root1, text="ADD SNIPPET!!", command=add)
    l1.pack()
    l2.pack()
    e.pack()
    e1.pack()
    add_snip.pack()
    root1.mainloop()

def run_log():
    global path,list_number
    time.sleep(3)
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
            
        
        elif "take" in a:
            pyautogui.typewrite(a[5:len(a)]+ " = input()")
            pyautogui.press("enter")
            
    
        elif "characters" in a:
            #characters <variable> <start of the string>
            prost = a.split(" ")
            st = " ".join(prost[2:])
            pyautogui.typewrite(prost[1]+" = '{}'".format(st),0.0025)
            pyautogui.press("right",2)
            pyautogui.press("enter")      
            
        
        elif "integer input" in a and "variable" in a:
            #integer input variable number
            pyautogui.typewrite(a[23:len(a)]+" = int(input())",0.0025)
            pyautogui.press("enter")
            
        elif "mapping number input" in a:
            #mapping number input variables distance time
            s = a[31:len(a)]
            s = s.replace(" ",",")
            pyautogui.typewrite(s+" = map(int,input().split())")
            pyautogui.press("enter")
            
            
        elif "create empty list" in a:
            list_number+=1
            pyautogui.typewrite("l"+str(list_number)+" = []\n",0.0025)
            
        elif "create list variable" in a:
            prost = a.split(" ")
            pyautogui.typewrite(prost[3]+" = []\n")  
            
        elif "list input variable" in a:
            prost = a.split(" ")
            pyautogui.typewrite(prost[3] + " = list(map(int,input().split()))\n",0.0025)
            
        elif "enter" in a:
            pyautogui.press("enter")
            
        elif "backspace" in a:
            pyautogui.press("backspace")
            
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
            syn = str(a[16:len(a)].lower())
            pyautogui.typewrite("print({})".format(syn),0.0025)
            pyautogui.hold("left")
            pyautogui.press("enter")
            

        elif "start" in a or "run" in a:
            pyautogui.hotkey("ctrl", "f5")
            
        
        elif "initial variable" in a:
            pyautogui.typewrite(a[17:len(a)]+"=0",0.0025)
            pyautogui.press("enter")
            
        
        elif "value" in a:
            prost = a.split(" ")
            if prost[2] =="equals":
                prost[2] = "="
            pyautogui.typewrite(" ".join(prost[1:]),0.0025)
            pyautogui.press("enter")
            
        
        elif "above" in a:
            pyautogui.hold("left")
            pyautogui.press("up")
            
        
        elif "line number" in a or "line Number" in a or "Line number" in a:
            pyautogui.hotkey("ctrl","g")
            pyautogui.typewrite(a[11:len(a)],0.0025)
            pyautogui.press("enter")
            b = int(a[11:len(a)])
            
        elif "return" in a:
            syn = rs.returnsyntax(a)
            pyautogui.typewrite(syn,0.0025)
        
        elif "power variable" in a:
            pyautogui.typewrite(a[15:20]+"**"+a[27:])
            pyautogui.hold("left")
            
        elif "for loop" in a:
            s = forsyn.returnsyntax(a)
            if "in range():" in s:
                pyautogui.typewrite(s,0.0025)
                pyautogui.press("enter")
                pyautogui.press("up",1)
                pyautogui.hotkey("fn","end")
                pyautogui.press("left",2)
                
            elif "in :" in s:
                pyautogui.typewrite(s,0.0025)
                pyautogui.press("enter")
                pyautogui.press("up",1)
                pyautogui.hotkey("fn","end")
                pyautogui.press("left",1)
                
        
        elif "if" in a or "else if" in a or "otherwise" in a:
             s = ies.returnsyntax(a)
             pyautogui.typewrite(s,0.0025)
             
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
            if b == 1:
                pyautogui.typewrite(str(b))
                pyautogui.press("enter",2,0.0025)
                pyautogui.press("up")
                
            else:
                pyautogui.typewrite(str(b-1))
                pyautogui.press("enter")
                pyautogui.hotkey("fn","end")
                pyautogui.press("enter")
            
        elif "argument" in a and a.count("pass") == 0 and a.count("range") == 0:
            b = a[9:len(a)]
            b = b.replace(" ",",")
            pyautogui.typewrite(b)
            pyautogui.press("right",2)
            pyautogui.press("enter")
            
        elif "operator" in a:
            syn = go.returnsyntax(a)
            pyautogui.typewrite(syn,0.0025)
        elif "call function" in a:
            b = a[14:len(a)]
            b=b.replace(" ","_")
            pyautogui.typewrite(b+"()",0.0025)
            pyautogui.press("left")
            
        elif "pass function argument" in a and a.count("pass") == 1:
            prost = a.split(" ")
            syn = "".join(prost[3:])
            pyautogui.typewrite(syn,0.0025)
            pyautogui.press("right")
            pyautogui.press("enter")
        elif "print function" in a and a.count("print") == 1:
            prost = a.split(" ")
            syn = prost[2]+"()"
            pyautogui.typewrite("print({})".format(syn))
            pyautogui.press("left",2)
        elif "range argument" in a and a.count("range") == 1:
            prost = a.split(" ")
            #range argument begin 1 end number
            syn = prost[3]+","+prost[5]
            pyautogui.typewrite(syn,0.0025)
            pyautogui.press("right",2)
            pyautogui.press("enter")
            
        elif "loop variable" in a and a.count("loop") == 1:
            prost = a.split(" ")
            syn = str(prost[2].tolower())
            pyautogui.typewrite(syn,0.0025)
            pyautogui.press("enter")
        
        elif "pause" in a:
            pyautogui.typewrite("#User said pause")
        elif "quit" in a or "exit" in a or "pause" in a:
            return
    messagebox.showinfo("Log","The log file was read succesfully!!")
def read_transcation_log():
    global path
    path = filedialog.askopenfilename(title = "Select your Transcation log",filetypes=(("text files","*.txt"),("all files","*.*")))
    t = threading.Thread(target = run_log)
    t.start()
def save_log():
    global records
    file = filedialog.asksaveasfile(defaultextension='.txt')
    b = str(file)
    b = b.replace("/","\\")
    b=b.replace("<_io.TextIOWrapper name=","")
    b=b.replace("mode='w' encoding='cp1252'","")
    b=b.replace(">","")
    b = b.replace("'","")
   
    with open(b,"w") as f:
        for i in records:
            file.writelines(i+"\n")
    messagebox.showinfo("Success","Transaction log saved.\nFile named in :{}".format(b))
    records.clear()
root = Tk()
root.geometry("400x650")
root.resizable(False,False)
root.title("Speech to text Python code editor")
root.iconbitmap(r"C:\\Users\\Anirudh Pandita\\Downloads\\images.ico")
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff="off")
file_menu.add_command(label="Insert", command=our_command)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save as",command=save_log)


file_menu.add_command(label = "Read Transcation log",command=read_transcation_log)
file_menu.add_command(label="Exit", command=root.quit)

start = Button(root, text="Press here to start listening",
               command=start_listening,padding=8)
start_db = Button(
    root, text="Enter the DATABASE mode to retrive the snippet!!!", command=start_listening_db,padding=8)
start_user_db = Button(
    root, text="Enter the user mode to access your snippets!!", command=start_listening_user,padding=8)
l = Label(root, text="PLEASE ENTER THE BUTTON TO START CODING!!",padding=8)
l.pack()


start.pack(pady=5)
start_db.pack(pady=5)
start_user_db.pack(pady=5)
l2 = Label(root,text = "You said:",padding=8)
l2.pack()
root.mainloop()
#this is working i guess??