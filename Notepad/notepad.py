#icon http://www.doublejdesign.co.uk/

import tkinter as tk
from tkinter import font,ttk,StringVar,IntVar,scrolledtext,COMMAND,messagebox,END,filedialog
from PIL import ImageTk, Image

#Define functions
def change_font(event):
    if font_style_select.get() == 'none':
        my_font = (font_select.get(),font_size_select.get())
    else:
        my_font = (font_select.get(),font_size_select.get(),font_style_select.get())

    input_text.config(font=my_font)

def new_page():
    #use askyesno from messagebox with returning value in 1 & 0
    ans = messagebox.askyesno("New Page alert!","Are you sure you want a new page without saving!")
    if ans ==1:
        input_text.delete("1.0",END)
        font_select.set('Terminal')
        font_size_select.set(12)
        font_style_select.set('none')
        change_font(2)
    elif ans ==0:
        save_note()
        root.destroy()
    
def exit_page():
    try:
        if input_text.get("1.0",END) == '':
            #use askyesno from messagebox with returning value in 1 & 0
            ans = messagebox.askyesno("Exit alert!","Are you sure you want to exit!")
            if ans ==1:
                root.destroy()
        else:
            ans = messagebox.askyesno("Save prompt","Are you sure you want to exit without saving!")
            if ans ==0:
                save_note()
                root.destroy()
            elif ans==1:
                root.destroy()
    except:
        return

def save_note():
    #Get the file location to save
    file_loc = filedialog.asksaveasfilename(initialdir="./",title="Save file",filetypes=(("Text file","*.txt"),("All files","*.*")))
    with open(file_loc,"w")as f:
        #Saving first three line as font_fam,font_size,font_style
        f.write(font_select.get()+"\n")
        f.write(str(font_size_select.get())+"\n")
        f.write(font_style_select.get()+"\n")

        #Saving the rest of life
        f.write(input_text.get("1.0",END))

def open_note():
    #Get the file location to open
    file_loc = filedialog.askopenfilename(initialdir="./",title="Open file",filetypes=(("Text file","*.txt"),("All files","*.*")))
    
    with open(file_loc,"r") as f:
        input_text.delete("1.0",END)
        #fetching the first three lines and setting the values
        font_select.set(f.readline().strip())
        font_size_select.set(int(f.readline().strip()))
        font_style_select.set(f.readline().strip())
        change_font(1)
        #Printing the rest of values
        text = f.read()
        input_text.insert("1.0",text)

#Define colors
root_color = "#2596be"
button_bg = "#bcbcb1"

root = tk.Tk()
root.title("Notepad")
root.iconbitmap("images/icon.ico")
root.geometry("900x700")
root.resizable(0,0)
root.config(bg=root_color)

#Define Frames
button_frames = tk.Frame(root,bg=button_bg)
input_frames = tk.Frame(root)
button_frames.pack(padx=5,pady=(10,0))
input_frames.pack(pady=20,padx=20)

#Define Layout

#Button Frame
new_image = ImageTk.PhotoImage(Image.open("images/new.png"))
new_button = tk.Button(button_frames,image=new_image,command=new_page)
new_button.grid(row=0,column=0,padx=(10,5),pady=5)

open_image = ImageTk.PhotoImage(Image.open("images/open.png"))
open_button = tk.Button(button_frames,image=open_image,command=open_note)
open_button.grid(row=0,column=1,padx=5)

save_image = ImageTk.PhotoImage(Image.open("images/save.png"))
save_button = tk.Button(button_frames,image=save_image,command=save_note)
save_button.grid(row=0,column=2,padx=5)

close_image = ImageTk.PhotoImage(Image.open("images/exit.png"))
close_button = tk.Button(button_frames,image=close_image,command=exit_page)
close_button.grid(row=0,column=3,padx=5)


font_list = []
font_size = [i for i in range(1,61) if i%2==0]
font_style = ["none","bold","italic"]
font_fam = font.families()
for i in font_fam:
    font_list.append(i)

font_select = StringVar()
font_selection = ttk.Combobox(button_frames,values=font_list,textvariable=font_select)
font_selection.grid(row=0,column=4,padx=5)
font_select.set('Terminal')
font_selection.bind("<<ComboboxSelected>>",change_font)

font_size_select = IntVar()
font_size_selection = ttk.Combobox(button_frames,values=font_size,textvariable=font_size_select)
font_size_selection.grid(row=0,column=5,padx=5)
font_size_select.set(12)
font_size_selection.bind("<<ComboboxSelected>>",change_font)

font_style_select = StringVar()
font_style_selection = ttk.Combobox(button_frames,values=font_style,textvariable=font_style_select)
font_style_selection.grid(row=0,column=6,padx=5)
font_style_select.set('none')
font_style_selection.bind("<<ComboboxSelected>>",change_font)

my_font = (font_select.get(),font_size_select.get())

input_text = scrolledtext.ScrolledText(input_frames,width=1000,height=100,font=my_font)
input_text.pack()



root.mainloop()