import tkinter as tk
from tkinter import RIGHT,ttk

#Define fonts
bg_color = "#c75c5c"
button_color = "#f3cb83"
font_fam = ("Cambria",14)

#Create Window
root = tk.Tk()
root.title("Metric Helper")
root.configure(background=bg_color)
root.resizable(0,0)
root.iconbitmap("images/ruler.ico")

#Define Functions
def convert():

    #Creating a metric dataset using dictionary
    metrics_values = {
        "famto":10**-15,
        "pico":10**-12,
        "nano":10**-9,
        "micro":10**-6,
        "mili":10**-3,
        "centi":10**-2,
        "deci":10**-1,
        "base value":10**0,
        "deca":10**1,
        "hecto":10**2,
        "kilo":10**3,
        "mega":10**6,
        "giga":10**9,
        "tera":10**12,
        "peta":10**15
}
    #gathering user input
    user_input = float(input_entry.get())
    base_prefix = input_combobox.get()
    base_conversion = output_combobox.get()
    #conversion
    base_value = user_input * metrics_values[base_prefix]
    converted_value = base_value/metrics_values[base_conversion]
    #Clearing output screen
    output_entry.delete(0,'end')
    #Entering output
    output_entry.insert(0,str(converted_value))



#Creating Widgets
#Entry boxes
input_entry = tk.Entry(root,text="Enter your quantity",width=20,justify=RIGHT,bd=3)
input_entry.grid(row=0,column=0,padx=20,pady=20)
output_entry = tk.Entry(root,text="Output result",width=20,justify=RIGHT,bd=3)
output_entry.grid(row=0,column=2,padx=20)

#Labels
equal_lbl = tk.Label(root,text="=",font=font_fam,bg=bg_color)
equal_lbl.grid(row=0,column=1)
to_lbl = tk.Label(root,text="to",font=font_fam,bg=bg_color)
to_lbl.grid(row=1,column=1)

#Combox list
metrics = ["famto","pico","nano","micro","mili","centi","deci","base value","deca","hecto","kilo","mega","giga","tera","peta"]
input_combobox = ttk.Combobox(root,values=metrics,font=("Cambria",8),justify='center')
output_combobox = ttk.Combobox(root,values=metrics,font=("Cambria",8),justify='center')
input_combobox.grid(row=1,column=0,padx=(10,0))
output_combobox.grid(row=1,column=2)
input_combobox.set('base value')
output_combobox.set('base value')

#Define Button
convert_button = tk.Button(root,text="Convert",font=font_fam,bg=button_color,command=convert)
convert_button.grid(row=2,column=0,columnspan=3,pady=20,ipadx=10)

root.mainloop()