"""A MODULE MADE TO RETRIEVE THE DATA FROM THE USER CODE SNIPPET REPO"""

import mysql.connector as db
import pyautogui as py
import googlestt
def run():
    mydb = db.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Kuld1972poon",
        database = "python"
    )
    googlestt.main()
    command = googlestt.printtext()
    if "pause" in command:
        return command
    else:
        cursor = mydb.cursor()
        cursor.execute("Select expression from user_commands where commands = '{}'".format(command))
        myreult = cursor.fetchall()
        try:
            b = str(*myreult[0])
            for i in range(len(b)):
                if b[i] =="_":
                    py.press("enter")
                elif b[i] == "-":
                    py.press("backspace")
                else:
                    py.typewrite(b[i])
        except IndexError:
            return ("Cannot find the snippet with the command '{}'".format(command))
            
        return command