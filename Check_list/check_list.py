import tkinter as tk
from tkinter import END, ANCHOR

#Define Functions
def add_item():
    #adding item to listbox
    listbox.insert(END,input_entry.get())
    input_entry.delete(0,END)

def remove():
    listbox.delete(ANCHOR)

def remove_all():
    listbox.delete(0,END)
    
def save_item():
    with open("Checklist.txt","w") as f:
        #getting listbox item as tuple
        listbox_tuple = listbox.get(0,END)
        for item in listbox_tuple:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item + "\n")

def open_items():
    with open("Checklist.txt","r") as f:
        for line in f:
            listbox.insert(END,line)

#Define colors
root_clr = "#6d1cbc"
button_color = "#bc84f3"
font_fam = ("Cambria",12)

#Define root window
root = tk.Tk()
root.title("Check list")
root.iconbitmap("images/check.ico")
root.configure(background=root_clr)
root.geometry("400x400")
root.resizable(0,0)

#Define Frames
input_frame = tk.Frame(root,bg=root_clr)
output_frame = tk.Frame(root)
button_frame = tk.Frame(root,bg=root_clr)

input_frame.pack()
output_frame.pack()
button_frame.pack(pady=5)

#Define Widgets in input frame
input_entry = tk.Entry(input_frame,borderwidth=2,width=43)
add_button = tk.Button(input_frame,text="Add item",font=font_fam,bg=button_color,padx=10,command=add_item)
input_entry.grid(row=0,column=0,padx=5,pady=5)
add_button.grid(row=0,column=1,padx=5,pady=5)

#Define listbox and scrollbar in output frame
listbox = tk.Listbox(output_frame,width=40,height=15,font=font_fam,borderwidth=2)
scrollbar = tk.Scrollbar(output_frame,command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
listbox.grid(row=0,column=0,ipady=5)
scrollbar.grid(row=0,column=1,sticky="NS")

#Define Buttons in Button Frame
remove_button = tk.Button(button_frame,text="Remove Item",font=font_fam,bg=button_color,command=remove)
remove_all_button = tk.Button(button_frame,text="Clear List",font=font_fam,bg=button_color,command=remove_all)
save_button = tk.Button(button_frame,text="Save Item",font=font_fam,bg=button_color,command=save_item)
quit_button = tk.Button(button_frame,text="Quit",font=font_fam,bg=button_color,command=root.destroy)

remove_button.grid(row=0,column=0,padx=5)
remove_all_button.grid(row=0,column=1,padx=(0,5),ipadx=7)
save_button.grid(row=0,column=2,padx=(0,5),ipadx=5)
quit_button.grid(row=0,column=3,padx=(0,5),ipadx=12)

open_items()

root.mainloop()