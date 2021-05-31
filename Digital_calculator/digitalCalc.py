from tkinter import *

class App(Frame):

    def __init__(self,master):
        super(App,self).__init__(master)
        self.task=""
        self.UserIn = StringVar()
        self.grid()
        self.create_wid()

    def create_wid(self):

        self.font = ("Helvetica",12,"bold")
        self.bg= "light green"
        #Creating entry field
        self.calc_entry = Entry(self,textvariable=self.UserIn,bg=self.bg,insertwidth=4,font=self.font,
                                width=46,bd=10,justify=RIGHT)
        self.calc_entry.grid(columnspan=4,sticky=W)

        #Creating number buttons

        #button7
        self.button7 = Button(self,text="7",bg=self.bg,bd=12,font=self.font,command=lambda : self.button_click(7),padx=33,pady=25)
        self.button7.grid(row=2,column=0,sticky=W)

        #button8
        self.button8 = Button(self,text="8",bg=self.bg,bd=12,font=self.font,command=lambda : self.button_click(8),padx=35,pady=25)
        self.button8.grid(row=2,column=1,sticky=W)

        #button9
        self.button9 = Button(self,text="9",bg=self.bg,bd=12,font=self.font,command=lambda : self.button_click(9),padx=33,pady=25)
        self.button9.grid(row=2,column=2,sticky=W)

        #button4
        self.button4 = Button(self,text="4",font=self.font,bg=self.bg,command=lambda : self.button_click(4),padx=33,pady=25,bd=12)
        self.button4.grid(row=3,column=0,sticky=W)

        #button5
        self.button5 = Button(self,text="5",font=self.font,bg=self.bg,command=lambda : self.button_click(5),padx=35,pady=25,bd=12)
        self.button5.grid(row=3,column=1,sticky=W)

        #button6
        self.button6 = Button(self,text="6",font=self.font,bg=self.bg,command=lambda : self.button_click(6),padx=33,pady=25,bd=12)
        self.button6.grid(row=3,column=2,sticky=W)

        #button1
        self.button1 = Button(self,text="1",font=self.font,bg=self.bg,command=lambda : self.button_click(1),padx=33,pady=25,bd=12)
        self.button1.grid(row=4,column=0,sticky=W)

        #button2
        self.button2 = Button(self,text="2",font=self.font,bg=self.bg,command=lambda : self.button_click(2),padx=35,pady=25,bd=12)
        self.button2.grid(row=4,column=1,sticky=W)

        #button3
        self.button3 = Button(self,text="3",font=self.font,bg=self.bg,command=lambda : self.button_click(3),padx=33,pady=25,bd=12)
        self.button3.grid(row=4,column=2,sticky=W)

        #button0
        self.button0 = Button(self,text="0",font=self.font,bg=self.bg,command=lambda : self.button_click(0),padx=33,pady=25,bd=12)
        self.button0.grid(row=5,column=0,sticky=W)

        #operator button
        #equal_button
        self.equal_btn = Button(self,text="=",font=self.font,bg=self.bg,command=self.Calculate_task,padx=89,pady=25,bd=12)
        self.equal_btn.grid(row=5,column=1,columnspan=2,sticky=W)

        #add_btn
        self.add_btn = Button(self,text="+",font=self.font,bg=self.bg,command=lambda : self.button_click("+"),padx=35,pady=25,bd=12)
        self.add_btn.grid(row=2,column=3,sticky=W)

        #subtract_btn
        self.subtract_btn = Button(self,text="-",font=self.font,bg=self.bg,command=lambda : self.button_click("-"),padx=37,pady=25,bd=12)
        self.subtract_btn.grid(row=3,column=3,sticky=W)

        #multiply_btn
        self.mutlipy_btn = Button(self,text="*",font=self.font,bg=self.bg,command=lambda : self.button_click("*"),padx=37,pady=25,bd=12)
        self.mutlipy_btn.grid(row=4,column=3,sticky=W)

        #divide_btn
        self.divide_btn = Button(self,text="/",font=self.font,bg=self.bg,command=lambda : self.button_click("/"),padx=38,pady=25,bd=12)
        self.divide_btn.grid(row=5,column=3,sticky=W)

        #All_Clear
        self.allclr_btn = Button(self,text="AC",font=self.font,bg="orange",command=self.clear_screen,bd=12,width=40,padx=6)
        self.allclr_btn.grid(row=1,columnspan=4,sticky=W)


    def button_click(self,number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def Calculate_task(self):
        self.data = self.calc_entry.get()
        try:
            self.answer = eval(self.data)
            self.display_txt(self.answer)
            self.task=self.answer
        except SyntaxError as e:
            self.UserIn.set("Invalid Syntax")
            self.task=""

    def display_txt(self,value):
        self.calc_entry.delete(0,"end")
        self.calc_entry.insert(0,value)

    def clear_screen(self):
        self.UserIn.set("")
        self.task = ""


calculator = Tk()
calculator.title("Digital Calculator")
calculator.resizable(width=False,height=False)

App(calculator)
calculator.mainloop()
