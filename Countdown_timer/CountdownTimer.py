from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global eventDate

# *argu is mandatory for using bind method
def quit(*argu):
    master.destroy()

def time_lft():
    time_left = eventDate - datetime.datetime.now()
    #removing microseconds from time_left
    time_left = time_left - datetime.timedelta(microseconds=time_left.microseconds)
    txt.set(time_left)
    master.after(1000,time_lft)

master = Tk()
master.title("Countdown timer")
master.attributes("-fullscreen", False)
master.configure(background="black")
master.bind("x",quit)
master.after(1000,time_lft)

txt = StringVar()
fnt = font.Font(family="Helvetica",size=120,weight="bold")
lbl = ttk.Label(master,textvariable=txt,background="black",foreground="white",font=fnt)
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)

eventDate = datetime.datetime(2021,4,24,11,50)

master.mainloop()