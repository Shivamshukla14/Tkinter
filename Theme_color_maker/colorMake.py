import tkinter as tk
from tkinter import BOTH,IntVar,filedialog

#Define Functions
def set_red(red_val):
    global red_value
    red_value = hex(int(red_val))
    red_value = red_value.lstrip("0x")
    while len(red_value) < 2:
        red_value = "0" + str(red_value)

    black_box = tk.Label(input_frame,bg="#" + red_value + green_value + blue_value,width=13,height=5)
    black_box.grid(row=1,column=3,columnspan=2)
    color_code.config(text="({}), ({}), ({})".format(slider_r.get(),slider_g.get(),slider_b.get()))
    hex_code.config(text="#" + red_value + green_value + blue_value)

def set_green(green_val):
    global green_value
    green_value = hex(int(green_val))
    green_value = green_value.lstrip("0x")
    while len(green_value) < 2:
        green_value = "0" + str(green_value)

    black_box = tk.Label(input_frame,bg="#" + red_value + green_value + blue_value,width=13,height=5)
    black_box.grid(row=1,column=3,columnspan=2)
    color_code.config(text="({}), ({}), ({})".format(slider_r.get(),slider_g.get(),slider_b.get()))
    hex_code.config(text="#" + red_value + green_value + blue_value)

def set_blue(blue_val):
    global blue_value
    blue_value = hex(int(blue_val))
    blue_value = blue_value.lstrip("0x")
    while len(blue_value) < 2:
        blue_value = "0" + str(blue_value)

    black_box = tk.Label(input_frame,bg="#" + red_value + green_value + blue_value,width=13,height=5)
    black_box.grid(row=1,column=3,columnspan=2)
    color_code.config(text="({}), ({}), ({})".format(slider_r.get(),slider_g.get(),slider_b.get()))
    hex_code.config(text="#" + red_value + green_value + blue_value)

def set_color(r,g,b):
    slider_r.set(r)
    slider_g.set(g)
    slider_b.set(b)

def store_color():
    #declaring stored_color to access and change value throughout the program according to need
    global stored_color

    #getting reference of each color and converting each value with three digit number 
    red_color = str(slider_r.get())
    while len(red_color) < 3:
        red_color = "0" + str(red_color)

    green_color = str(slider_g.get())
    while len(green_color) < 3:
        green_color = "0" + str(green_color)

    blue_color = str(slider_b.get())
    while len(blue_color) < 3:
        blue_color = "0" + str(blue_color)

    radio_button = tk.Radiobutton(output_frame,variable=stored_color,value=stored_color.get(),activebackground=frame_bg,bg=frame_bg)
    recall_button = tk.Button(output_frame,text="Recall",bg=root_bg,command=lambda: set_color(red_color,green_color,blue_color))
    new_color_code = tk.Label(output_frame,text="({}), ({}), ({})".format(red_color,green_color,blue_color),bg=frame_bg)
    new_hex_code = tk.Label(output_frame,text="#" + red_value + green_value + blue_value,bg=frame_bg)
    new_black_box = tk.Label(output_frame,bg="#000000",width=3,height=1)
    new_white_box = tk.Label(output_frame,bg="#" + red_value + green_value + blue_value,width=3,height=1)
    radio_button.grid(row=stored_color.get(),column=0,padx=20)
    recall_button.grid(row=stored_color.get(),column=1,padx=(0,20),ipadx=20)
    new_color_code.grid(row=stored_color.get(),column=2,padx=(0,20))
    new_hex_code.grid(row=stored_color.get(),column=3,padx=(0,20))
    new_black_box.grid(row=stored_color.get(),column=4,ipadx=2,ipady=2,padx=20,pady=8)
    new_white_box.grid(row=stored_color.get(),column=4)

    stored_colors[stored_color.get()] = [new_color_code.cget("text"),new_hex_code.cget("text")]

    if stored_color.get() < 5:
        stored_color.set(stored_color.get() + 1)

def save_color():
    #getting filelocation and username from user to save
    file_loc = filedialog.asksaveasfilename(initialdir="images/",title="Save file",filetypes=(("Text File","*.txt"),("All Files","*.*")))
    #Content in the file
    with open(file_loc,"w") as f:
        #head of the file
        f.write("Color code and hex value" + "\n")
        # looping throughout the dictionary
        for i in stored_colors.values():
            f.write("Color code: " + str(i[0]) + "\n" + "Hex code: " + str(i[1]) + "\n\n")

#Define colors
root_bg = "#123456"
frame_bg= "#ffffd5"

#Define window
root = tk.Tk()
root.title("Theme-Color maker")
root.iconbitmap("images/theme.ico")
root.geometry("450x500")
root.config(bg=root_bg)
root.resizable(0,0)

#Define Frames
input_frame = tk.Frame(root,bg=frame_bg)
output_frame = tk.Frame(root,bg=frame_bg)
input_frame.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=BOTH,expand=True)
output_frame.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=BOTH,expand=True)

#Define layout

#input frame

#labels
red_label = tk.Label(input_frame,text="R",bg=frame_bg)
green_label = tk.Label(input_frame,text="G",bg=frame_bg)
blue_label = tk.Label(input_frame,text="B",bg=frame_bg)
black_box = tk.Label(input_frame,bg="black",width=13,height=5)
color_code = tk.Label(input_frame,bg=frame_bg,text="(000), (000), (000)")
hex_code = tk.Label(input_frame,bg=frame_bg,text="#000000")

red_label.grid(row=0,column=0)
green_label.grid(row=0,column=1)
blue_label.grid(row=0,column=2)
black_box.grid(row=1,column=3,columnspan=2,ipadx=3,ipady=3)
color_code.grid(row=2,column=3,columnspan=2)
hex_code.grid(row=3,column=3,columnspan=2)

#sliders
slider_r = tk.Scale(input_frame,from_=0,to=255,bg=root_bg,command=set_red)
slider_g = tk.Scale(input_frame,from_=0,to=255,bg=root_bg,command=set_green)
slider_b = tk.Scale(input_frame,from_=0,to=255,bg=root_bg,command=set_blue)

slider_r.grid(row=1,column=0,pady=5)
slider_g.grid(row=1,column=1)
slider_b.grid(row=1,column=2)

#buttons
red_button = tk.Button(input_frame,text="Red",bg=root_bg,command=lambda:set_color(255,0,0))
green_button = tk.Button(input_frame,text="Green",bg=root_bg,command=lambda:set_color(0,255,0))
blue_button = tk.Button(input_frame,text="Blue",bg=root_bg,command=lambda:set_color(0,0,255))
yellow_button = tk.Button(input_frame,text="Yellow",bg=root_bg,command=lambda:set_color(255,255,0))
cyan_button = tk.Button(input_frame,text="Cyan",bg=root_bg,command=lambda:set_color(0,255,255))
maginta_button = tk.Button(input_frame,text="Maginta",bg=root_bg,command=lambda:set_color(255,0,255))
store_button = tk.Button(input_frame,text="Store Color",bg=root_bg,command=store_color)
save_button = tk.Button(input_frame,text="Save",bg=root_bg,command=save_color)
exit_button = tk.Button(input_frame,text="Exit",bg=root_bg,command=root.destroy)

red_button.grid(row=2,column=0,ipadx=20,padx=1,pady=1)
green_button.grid(row=2,column=1,ipadx=15,padx=1)
blue_button.grid(row=2,column=2,ipadx=18,padx=1)
yellow_button.grid(row=3,column=0,sticky="WE",padx=1)
cyan_button.grid(row=3,column=1,sticky="WE",padx=1)
maginta_button.grid(row=3,column=2,sticky="WE",padx=1)
store_button.grid(row=4,column=0,columnspan=3,sticky="WE",pady=1,padx=1)
save_button.grid(row=4,column=3,ipadx=38,padx=1)
exit_button.grid(row=4,column=4,ipadx=38,padx=1)

#Declaring an IntVar to identify position in output frame
stored_color = IntVar()

#Output Frame

for i in range(6):
    radio_button = tk.Radiobutton(output_frame,variable=stored_color,value=i,activebackground=frame_bg,bg=frame_bg)
    recall_button = tk.Button(output_frame,text="Recall",bg=root_bg,command=lambda: set_color(255,255,255))
    new_color_code = tk.Label(output_frame,text="(255), (255), (255)",bg=frame_bg)
    new_hex_code = tk.Label(output_frame,text="#ffffff",bg=frame_bg)
    new_black_box = tk.Label(output_frame,bg="#000000",width=3,height=1)
    new_white_box = tk.Label(output_frame,bg="#ffffff",width=3,height=1)
    radio_button.grid(row=i,column=0,padx=20)
    recall_button.grid(row=i,column=1,padx=(0,20),ipadx=20)
    new_color_code.grid(row=i,column=2,padx=(0,20))
    new_hex_code.grid(row=i,column=3,padx=(0,20))
    new_black_box.grid(row=i,column=4,ipadx=2,ipady=2,padx=20,pady=8)
    new_white_box.grid(row=i,column=4)

#Initializibg red_value, green_value, blue_value variable
red_value = "00"
green_value = "00"
blue_value = "00"

#Initializing a dictionary and setting values in it
stored_colors = {}
stored_colors[stored_color.get()] = [new_color_code.cget("text"),new_hex_code.cget("text")]

root.mainloop()
#Run mainloop