from tkinter import Tk
import mysql.connector as db
from tkinter.ttk import *
import pyautogui as py
import time
def send():
    a = e.get()
    b = e2.get()
    mydb = db.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Kuld1972poon",
        database = "python"
    )
    b = b.replace("\\n","_")
    cursor = mydb.cursor()
    sql = "insert into user_commands values(%s,%s)"
    val = (a,b)
    cursor.execute(sql,val)
    mydb.commit()
    
root = Tk()
root.title("TESTING DATABASE INPUT")
root.geometry("400x400")

e = Entry(root,width=100)
e2 = Entry(root,width=100)
b1 = Button(root,text="Insert into db!!",command=send)
e.pack()
e2.pack()
b1.pack()
root.mainloop()