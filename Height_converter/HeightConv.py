from tkinter import Tk,Label,Button,Entry,DoubleVar

master = Tk()
master.title("Height Convereter from Feet to meters")
master.geometry("320x220")
master.configure(background="light green")
master.resizable(width=False,height=False)


def convert():
    val = float(Text1.get())
    result = val * 0.3048
    data1.set("%.4f" % result)

def hello():
    Text1.delete(0,'end')
    Text2.delete(0,'end')

Label1 = Label(master,text="Feet:",bg="purple",fg="white",width=14)
Label1.grid(row=0,column=0,padx=15,pady=15)
Label2 = Label(master,text="Meter:",bg="brown",fg="white",width=14)
Label2.grid(row=1,column=0,padx=15,pady=20)

data = DoubleVar()
data1 = DoubleVar()

Text1 = Entry(master,textvariable=data,width=15)
Text1.delete(0,"end")
Text1.grid(row=0,column=1,pady=15,padx=15)

Text2 = Entry(master,textvariable=data1,width=15)
Text2.delete(0,'end')
Text2.grid(row=1,column=1,padx=15,pady=30)

Button1 = Button(master,text="Convert",bg="blue",fg="white",width=16,command=convert)
Button1.grid(row=2,column=0,padx=15,pady=10)

Button2 = Button(master,text="Clear",bg="blue",fg="white",width=16,command=hello)
Button2.grid(row=2,column=1,padx=15,pady=10)

master.mainloop()