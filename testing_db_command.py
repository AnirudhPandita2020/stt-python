import mysql.connector as db
import googlestt
import pyautogui 


def run():
    mydb=db.connect(
        host="127.0.0.1",
        user="root",
        password="Kuld1972poon",
        database="python"
        )
    googlestt.main()
    command=googlestt.printtext()
    if "pause" in command:
        return command
    else:
        cursor=mydb.cursor()
        cursor.execute("Select expression from python_commands where command='{}'".format(command))
        myresult=cursor.fetchall()
        try:
            pyautogui.typewrite(*myresult[0],0.1)
            return command
        except IndexError:
            return ("Cannot find the snippet with the command '{}'".format(command))


