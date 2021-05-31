from tkinter import *

class CurrencyConverter:

    def __init__(self):
        window = Tk()
        window.title("Currency converter")
        window.geometry("400x250")
        window.configure(bg="orange")
        window.resizable(width=False,height=False)

        Label(window,text="Enter the amount:",bg="yellow",font="Helventica 12 bold").grid(row=1,column=1,sticky=W,padx=20,pady=15)
        Label(window,text="Conversion rate:",bg="yellow",font="Helventica 12 bold").grid(row=2,column=1,sticky=W,padx=20,pady=15)
        Label(window,text="Converted amount:",bg="Yellow",font="Helventica 12 bold").grid(row=3,column=1,sticky=W,padx=20,pady=15)

        self.amount = StringVar()
        Entry(window, textvariable=self.amount, justify=RIGHT).grid(row=1,column=2,sticky=E)
        self.rate = StringVar()
        Entry(window, textvariable=self.rate, justify=RIGHT).grid(row=2,column=2,sticky=E)
        self.convertedamount = StringVar()
        Label(window,textvariable=self.convertedamount,font="Helventica 12 bold",bg="orange").grid(row=3,column=2,sticky=E)

        Button(window,text="Convert",font="Helventica 12 bold",command=self.convertamt,bg="red",fg="white").grid(row=4,column=1,padx=20,pady=15)
        Button(window,text="Clear",font="Helventica 12 bold",command=self.clearall,bg="red",fg="white").grid(row=4,column=2)

        window.mainloop()

    def convertamt(self):
        amt = float(self.rate.get())
        ConvertedAmt = float(self.amount.get()) * amt
        self.convertedamount.set(format(ConvertedAmt, '10.2f'))

    def clearall(self):
        self.amount.set("")
        self.rate.set("")
        self.convertedamount.set("")

CurrencyConverter()