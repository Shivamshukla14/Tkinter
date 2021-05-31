from tkinter import Tk,Label,Entry,Button,Radiobutton,StringVar,IntVar,DoubleVar

class TipCalc():
    def __init__(self):
        master = Tk()
        master.title("Tip Calculator")
        master.geometry("375x270")
        master.configure(background="orange")
        master.resizable(width=False,height=False)

        self.og_bill= StringVar()
        self.tip_percent = IntVar()
        self.tip_val = StringVar()
        self.total_bill = StringVar()

        Bill_amount = Label(master,text="Bill amount:",bg="red",fg="white",width=14)
        Tip_amount = Label(master,text="Tip amount:",bg="purple",fg="white",width=14)
        Total_amount = Label(master,text="Total amount:",bg="brown",fg="white",width=14)
        five_p = Radiobutton(master,text="5%",variable=self.tip_percent,value=5,width=10)
        ten_p = Radiobutton(master,text="10%",variable=self.tip_percent,value=10,width=10)
        fifteen_p = Radiobutton(master,text="15%",variable=self.tip_percent,value=15,width=10)
        twenty_p = Radiobutton(master,text="20%",variable=self.tip_percent,value=20,width=10)
        twenty_five_p = Radiobutton(master,text="25",variable=self.tip_percent,value=25,width=10)
        Tip_Perc = Label(master,text="Tip %",bg="red",fg="white",width=14)
        Bill_entry = Entry(master,textvariable=self.og_bill,width=15)
        Tip_entry = Entry(master,textvariable=self.tip_val,width=15)
        Total_entry = Entry(master,textvariable=self.total_bill,width=15)
        calculate_btn = Button(master,text="Calculate",command=self.calculate,width=10,bg="blue",fg="white")
        clear_btn = Button(master,text="Clear",command=self.clear,width=10,bg="blue",fg="white")

        Tip_Perc.grid(row=0,column=0,padx=15,pady=10)
        Bill_amount.grid(row=0,column=1,pady=10)
        Tip_amount.grid(row=3,column=1)
        Bill_entry.grid(row=0,column=2,pady=10,padx=15)
        Tip_entry.grid(row=3,column=2)
        five_p.grid(row=1,column=0)
        ten_p.grid(row=2,column=0)
        fifteen_p.grid(row=3,column=0)
        twenty_p.grid(row=4,column=0)
        twenty_five_p.grid(row=5,column=0)
        Total_amount.grid(row=7,column=1)
        Total_entry.grid(row=7,column=2)
        calculate_btn.grid(row=9,column=1,pady=10)
        clear_btn.grid(row=9,column=2,pady=10)

        master.mainloop()

    def calculate(self):
        bill = float(self.og_bill.get())
        percent = self.tip_percent.get()/100
        tip_percent = bill * percent
        self.tip_val.set(tip_percent)

        total_value = bill + tip_percent
        self.total_bill.set(total_value)


    def clear(self):
        self.og_bill.set("")
        self.tip_val.set("")
        self.total_bill.set("")


TipCalc()