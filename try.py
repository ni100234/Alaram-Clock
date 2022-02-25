from logging import root
from tkinter import *
import datetime
import time
import winsound
 
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("*",winsound.SND_ASYNC)
            break
 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)
 
root = Tk()
root.title("Alarm Clock")
root.geometry("400x160")
root.config(bg="white")
root.resizable(width=False,height=False)
 
time_format=Label(root, text= "Remember to set time in 24 hour format!", fg="white",bg="black",font=("Arial",15)).place(x=20,y=125)
addTime = Label(root,text = "Hr      Min      Sec",font=60,fg="black").place(x = 210)
setYourAlarm = Label(root,text = "Time for alarm: ",fg="white",bg="black",relief = "solid",font=("Helevetica",15,"bold")).place(x=10, y=40)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
 
hourTime= Entry(root,textvariable = hour,bg = "sky blue",width = 4,font=(20)).place(x=210,y=40)
minTime= Entry(root,textvariable = min,bg = "sky blue",width = 4,font=(20)).place(x=270,y=40)
secTime = Entry(root,textvariable = sec,bg = "sky blue",width = 4,font=(20)).place(x=330,y=40)
 
submit = Button(root,text = "Set Alarm",fg="Black",bg="light grey",width = 15,command = get_alarm_time,font=(20)).place(x =215,,y=80)
                                                                                                                      
 
root.mainloop()
