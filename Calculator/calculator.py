from os import stat
import tkinter as tk
from tkinter import RIGHT,END,DISABLED,NORMAL
from tkinter.constants import INSERT

#Define Functions
def clear():
    input_entry.delete(0,END)
    enable_buttons()

def calc_entry(numbers):
    input_entry.insert(END,numbers)

    #Checking if . is used or not
    if '.' in input_entry.get():
        button_point.config(state=DISABLED)

def operation(operator):
    global first_number
    global operate

    if input_entry.get() == '':
        first_number = ''
        operate = ''
        pass
    else:
        operate = operator
        first_number = input_entry.get()

        input_entry.delete(0,END)
        button_point.config(state=NORMAL)
        square_button.config(state=DISABLED)
        inverse_button.config(state=DISABLED)
        raised_button.config(state=DISABLED)
        divide_button.config(state=DISABLED)
        multiply_button.config(state=DISABLED)
        add_button.config(state=DISABLED)
        subtract_button.config(state=DISABLED)
      
    
def enable_buttons():
    button_point.config(state=NORMAL)
    square_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    raised_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    

def square():

    if input_entry.get() == '':
        value = ''       
    else:
        value = float(input_entry.get()) ** 2

    input_entry.delete(0,END)
    input_entry.insert(0,value)

def final_ans():

    if input_entry.get() == '':
        value = 'ERROR'
        timeout()
    else:
        if operate == 'add':
            value = float(first_number) + float(input_entry.get())
        elif operate == 'subtract':
            value = float(first_number) - float(input_entry.get())
        elif operate == 'multiply':
            value = value = float(first_number) * float(input_entry.get())
        elif operate == 'divide':
            if input_entry.get() == '0':
                value = 'ERROR'
                timeout()
            else:
                value = float(first_number) / float(input_entry.get())
        elif operate == 'exponent':
            value = float(first_number) ** float(input_entry.get())
        else:
            value = 'ERROR'
            timeout()

    input_entry.delete(0,END)
    input_entry.insert(0,value)
    enable()
    
def enable():
    if '.' in input_entry.get():
        enable_buttons()
        button_point.config(state=DISABLED)
    else:
        enable_buttons()
        button_point.config(state=DISABLED)
            

def timeout():
    input_entry.after(2000,clear)

def inverse():
    if input_entry.get() == '':
        value = ''
    elif input_entry.get() == '0':
        value = 'ERROR'
        timeout()
    else:
        value = 1.0 / float(input_entry.get())
    
    input_entry.delete(0,END)
    input_entry.insert(0,value)

def conjugate():
    if input_entry.get() =='':
        value = 'ERROR'
        timeout()
    elif input_entry.get() =='0':
        value = '0'
    else:
        value = -1 * float(input_entry.get())

    input_entry.delete(0,END)
    input_entry.insert(0,value)
    

#Define colors
top_layer = "#4b5b63"
second_layer = "#6f8792"
num_layer1 = "#396a61"
num_layer2 = "#189174"
num_layer3 = "#64aea2"
num_layer4 = "#92a6ae"
font_fam=("Cambria",10)

#Define root
root = tk.Tk()
root.title("Calculator")
root.resizable(0,0)
root.iconbitmap("images/Calc.ico")

#Define Frame
input_frame = tk.Frame(root)
input_frame.pack(padx=3)
button_frame = tk.Frame(root)
button_frame.pack(pady=(20,5),padx=3)

#Define widgets

#Entry widget
input_entry = tk.Entry(input_frame,width=28,borderwidth=4,justify=RIGHT)
input_entry.pack(ipady=3)

#power_image
Power_img = tk.PhotoImage(file="images/power.png")

#Button widget
AC_button = tk.Button(button_frame,text="AC",bg=top_layer,fg="#ffffff",font=font_fam,pady=3,padx=31,command=clear)
Power_button = tk.Button(button_frame,image=Power_img,bg=top_layer,width=80,command=root.destroy)
inverse_button = tk.Button(button_frame,text="1/x",bg=second_layer,font=font_fam,padx=8,command=inverse)
square_button = tk.Button(button_frame,text="x^2",font=font_fam,bg=second_layer,padx=7,command=square)
raised_button = tk.Button(button_frame,text="x^n",font=font_fam,bg=second_layer,padx=7,command=lambda:operation('exponent'))
divide_button = tk.Button(button_frame,text="/",font=font_fam,bg=second_layer,padx=14,command=lambda:operation('divide'))
button_7 = tk.Button(button_frame,text="7",bg=num_layer1,font=font_fam,padx=14,command=lambda:calc_entry(7))
button_8 = tk.Button(button_frame,text="8",font=font_fam,bg=num_layer1,padx=13,command=lambda:calc_entry(8))
button_9 = tk.Button(button_frame,text="9",font=font_fam,bg=num_layer1,padx=13,command=lambda:calc_entry(9))
multiply_button = tk.Button(button_frame,text="*",font=font_fam,bg=second_layer,padx=14,command=lambda:operation('multiply'))
button_4 = tk.Button(button_frame,text="4",font=font_fam,bg=num_layer2,padx=14,command=lambda:calc_entry(4))
button_5 = tk.Button(button_frame,text="5",font=font_fam,bg=num_layer2,padx=13,command=lambda:calc_entry(5))
button_6 = tk.Button(button_frame,text="6",font=font_fam,bg=num_layer2,padx=13,command=lambda:calc_entry(6))
subtract_button = tk.Button(button_frame,text="-",font=font_fam,bg=second_layer,padx=15,command=lambda:operation('subtract'))
button_1 = tk.Button(button_frame,text="1",font=font_fam,bg=num_layer3,padx=14,command=lambda:calc_entry(1))
button_2 = tk.Button(button_frame,text="2",font=font_fam,bg=num_layer3,padx=13,command=lambda:calc_entry(2))
button_3 = tk.Button(button_frame,text="3",font=font_fam,bg=num_layer3,padx=13,command=lambda:calc_entry(3))
add_button = tk.Button(button_frame,text="+",font=font_fam,bg=second_layer,padx=13,command=lambda:operation('add'))
conjugate_button = tk.Button(button_frame,text="+/-",font=font_fam,bg=num_layer4,padx=9,command=conjugate)
button_0 = tk.Button(button_frame,text="0",font=font_fam,bg=num_layer4,padx=14,command=lambda:calc_entry(0))
button_point = tk.Button(button_frame,text=".",font=font_fam,bg=num_layer4,padx=15,command=lambda:calc_entry('.'))
equal_button = tk.Button(button_frame,text="=",font=font_fam,bg=second_layer,padx=14,command=final_ans)


AC_button.grid(row=0,column=0,columnspan=2,sticky="W")
Power_button.grid(row=0,column=2,columnspan=2)
inverse_button.grid(row=1,column=0,sticky="W")
square_button.grid(row=1,column=1,sticky="W")
raised_button.grid(row=1,column=2,sticky="W")
divide_button.grid(row=1,column=3)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
multiply_button.grid(row=2,column=3)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
subtract_button.grid(row=3,column=3)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
add_button.grid(row=4,column=3)
conjugate_button.grid(row=5,column=0)
button_0.grid(row=5,column=1)
button_point.grid(row=5,column=2)
equal_button.grid(row=5,column=3)

root.mainloop()