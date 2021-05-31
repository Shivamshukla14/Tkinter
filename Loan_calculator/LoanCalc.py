from tkinter import *

class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        window.geometry("400x300")
        window.resizable(width=False,height=False)
        window.configure(bg="light green")

        font_style = ("Helventica 12 bold")

        Label(window,text="Annual Interest Rate:",font=font_style,bg="light green").grid(row=0,column=0,sticky=W,padx=15,pady=(30,10))
        Label(window,text="Number of Years:",font=font_style,bg="light green").grid(row=1,column=0,sticky=W,padx=15,pady=(0,10))
        Label(window,text="Loan Amount:",font=font_style,bg="light green").grid(row=2,column=0,sticky=W,padx=15,pady=(0,10))
        Label(window,text="Monthly payment:",font=font_style,bg="light green").grid(row=3,column=0,sticky=W,padx=15,pady=(0,10))
        Label(window,text="Total payment:",font=font_style,bg="light green").grid(row=4,column=0,sticky=W,padx=15,pady=(0,10))

        self.AnnualIntRate = StringVar()
        Entry(window,textvariable=self.AnnualIntRate,justify=RIGHT,width=20).grid(row=0,column=1,sticky=E,pady=(30,10),padx=20)
        self.NumOfYears = StringVar()
        Entry(window,textvariable=self.NumOfYears,justify=RIGHT,width=20).grid(row=1,column=1,sticky=E,pady=(0,10),padx=20)
        self.LoanAmt = StringVar()
        Entry(window,textvariable=self.LoanAmt,justify=RIGHT,width=20).grid(row=2,column=1,pady=(0,10),padx=20)
        self.MonthlyPay = StringVar()
        Label(window,textvariable=self.MonthlyPay,bg="light green").grid(row=3,column=1,pady=(0,10),padx=20,sticky=E)
        self.TotalPay = StringVar()
        Label(window,textvariable=self.TotalPay,bg="light green").grid(row=4,column=1,pady=(0,10),padx=20,sticky=E)

        Button(window,text="Check Amount:",bg="red",fg="white",width=15,command=self.computepayment).grid(row=5,column=0,pady=15,padx=15,sticky=W)
        Button(window,text="Clear:",bg="red",fg="white",width=15,command=self.clearall).grid(row=5,column=1,pady=15,padx=20)

        window.mainloop()

    def computepayment(self):
        monthlypay = self.monthlycompute(
            float(self.LoanAmt.get()),
            float(self.AnnualIntRate.get()) / 1200,
            float(self.NumOfYears.get())
        )

        self.MonthlyPay.set(format(monthlypay, '10.2f'))

        totalpay = float(self.MonthlyPay.get()) * 12 * float(self.NumOfYears.get())
        self.TotalPay.set(format(totalpay, '10.2f'))

    def monthlycompute(self,loanamount,interest,numberofyrs):
        monthlypay = loanamount * interest / (1-1/(1 + interest) ** (numberofyrs * 12))
        return monthlypay

    def clearall(self):
        self.LoanAmt.set("")
        self.TotalPay.set("")
        self.MonthlyPay.set("")
        self.NumOfYears.set("")
        self.AnnualIntRate.set("")


LoanCalculator()
