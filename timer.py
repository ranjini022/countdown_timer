from tkinter import *
from playsound import playsound
import time

root=Tk()
root.title("TIMER APP")
root.config(bg="#000")
root.geometry("330x370")
root.resizable(False,False)

heading=Label(root,text="TIMER", font=("arial",26,'bold'),fg="#1E90FF",bg="#000").place(x=105,y=15)

Label(root,font=("arial",11,"bold"),bg="#FAEBD7",fg="#000",text="CURRENT TIME :").place(x=50,y=63)
def clock():
    clock_time=time.strftime("%H:%M:%S %p")
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

current_time=Label(root,font=("arial",11,"bold"),text="",fg="#FCFCFC",bg="#000")
current_time.place(x=180,y=63)
clock()

def timer():
    times=int(hrs.get())*3600 + int(mins.get())*60 + int(secs.get())
    while times>-1:
        minute,second=(times//60,times%60)
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)
        secs.set(second)
        mins.set(minute)
        hrs.set(hour)
        root.update()
        time.sleep(1)
        if (times==0):
            playsound("alarm-clock-short-6402.mp3")
            secs.set("00")
            mins.set("00")
            hrs.set("00")
        times-=1



hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 40",fg="white",bg="#000").place(x=45,y=150)
hrs.set("00")
mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 40",fg="white",bg="#000").place(x=130,y=150)
mins.set("00")
secs=StringVar()
Entry(root,textvariable=secs,width=2,font="arial 40",fg="white",bg="#000").place(x=215,y=150)
secs.set("00")
Label(root,text=":",font="arial 35",fg="white",bg="#000").place(x=109,y=149)
Label(root,text=":",font="arial 35",fg="white",bg="#000").place(x=195,y=149)

bt=Button(root,text="Start",bg="#EE0000",fg="white",width=20,height=3,font="arial 12 bold",command=timer)
bt.pack(padx=5,pady=30,side=BOTTOM)

root.mainloop()