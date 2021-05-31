from tkinter import *
from time import strftime

master = Tk()
master.title("Digital Computer")

def time():
    stg = strftime("%H:%M:%S %p")
    lbl.config(text = stg)
    lbl.after(1000,time)

lbl = Label(master,font=("Helvetica",120,"bold"),bg="black",fg="white")

lbl.pack(anchor="center",fill="both",expand=1)

time()

master.mainloop()