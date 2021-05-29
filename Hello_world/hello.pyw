import tkinter as tk
from tkinter import StringVar,BOTH

#Defining Functions
def submit_text():
    if user_input.get() == "":
        pass
    else:
        if case_style.get() == 'normal':
            final_state = "Hello {}! Welcome to the world!".format(user_input.get())
            lbl = tk.Label(output_frame,text=final_state,font=("Arial",10,"bold"),fg="#ffffff",bg="#33C3FF")
        elif case_style.get() == 'upper':
            final_state = ("Hello {}! Welcome to the world!".format(user_input.get())).upper()
            lbl = tk.Label(output_frame,text=final_state,font=("Arial",10,"bold"),fg="#ffffff",bg="#33C3FF")
        lbl.pack()
    user_input.delete(0,"end")

  
#Create Windows
root = tk.Tk()
root.title("Hello World app!")
root.iconbitmap("images/wave.ico")
root.geometry("400x400")
root.resizable(0,0)
root.configure(background="#123456")

#Create Frames
input_frame = tk.LabelFrame(root,bg="#0000ff")
output_frame = tk.LabelFrame(root,bg="#33C3FF")
input_frame.pack(padx=10,pady=10)
output_frame.pack(padx=10,pady=(0,10),fill=BOTH,expand=True)

#Create Widgets
user_input = tk.Entry(input_frame,text="Enter any name",width=20)
submit = tk.Button(input_frame,text="Submit",activebackground="#123456",width=10,command=submit_text)
user_input.grid(row=0,column=0,padx=10,pady=10)
submit.grid(row=0,column=1,padx=10)

#Radio Buttons
case_style = StringVar()
case_style.set('normal')
rad_lower = tk.Radiobutton(input_frame,text="Normal Case",variable=case_style,value="normal",bg="#0000ff",activebackground="#123456")
rad_upper = tk.Radiobutton(input_frame,text="Upper Case",variable=case_style,value="upper",bg="#0000ff",activebackground="#123456")
rad_lower.grid(row=1,column=0)
rad_upper.grid(row=1,column=1)

#Adding image to Output Frame
smile_image = tk.PhotoImage(file="images/smile.png")
smile_lbl = tk.Label(output_frame,image=smile_image,bg="#33C3FF")
smile_lbl.pack()

root.mainloop()