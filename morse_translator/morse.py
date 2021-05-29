import tkinter as tk
from tkinter import END

#Define functions
def clear_text():
    text_field_input.delete("1.0",END)
    text_field_output.delete("1.0",END)

#Define colors and fonts
root_bg = "#c0c3af"
frame_bg = "#f1e9de"
button_color = "#958884"
button_font = ("Cambria",13)
font_color = "#1e81b0"

#Define window
root = tk.Tk()
root.title('Morse-code Translator')
root.iconbitmap("images/network.ico")
root.geometry("500x400")
root.resizable(0,0)
root.config(bg=root_bg)

#Define dictionary
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
'y': '-.--', 'z': '--..', '1': '.----',
'2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
'0': '-----', ' ':' ', '|':'|', "":"" }

morse_to_english = dict([(value,key) for key,value in english_to_morse.items()])

#Define frames
input_frame = tk.LabelFrame(root,bg=frame_bg)
output_frame = tk.LabelFrame(root,bg=frame_bg)
input_frame.pack(padx=16,pady=15)
output_frame.pack(padx=16,pady=(0,15))

#Define layout

#Input frame
text_field_input = tk.Text(input_frame,width=27,height=8,font=button_font,fg=font_color)
radio_english_to_morsh = tk.Radiobutton(input_frame,text="English-->Morsh code",value=0,font=button_font,bg=frame_bg,activebackground=frame_bg)
radio_morse_to_english = tk.Radiobutton(input_frame,text="Morse code-->English",value=1,font=button_font,bg=frame_bg,activebackground=frame_bg)
guide_button = tk.Button(input_frame,text="Guide",bg=button_color,font=button_font)
text_field_input.grid(row=0,column=1,rowspan=3,padx=5,pady=5)
radio_english_to_morsh.grid(row=0,column=0,padx=5)
radio_morse_to_english.grid(row=1,column=0,padx=5)
guide_button.grid(row=2,column=0,sticky="WE",padx=5)

#Output Frame
text_field_output = tk.Text(output_frame,width=27,height=8,font=button_font,fg=font_color)
convert_button = tk.Button(output_frame,text="Convert",font=button_font,bg=button_color)
play_button = tk.Button(output_frame,text="Play Morse",font=button_font,bg=button_color)
clear_button = tk.Button(output_frame,text="Clear",bg=button_color,font=button_font,command=clear_text)
exit_button = tk.Button(output_frame,text="Exit",bg=button_color,font=button_font,command=root.destroy)

text_field_output.grid(row=0,column=1,rowspan=4,padx=5,pady=5)
convert_button.grid(row=0,column=0,padx=5,sticky="WE",ipadx=58)
play_button.grid(row=1,column=0,padx=5,sticky="WE")
clear_button.grid(row=2,column=0,padx=5,sticky="WE")
exit_button.grid(row=3,column=0,padx=5,sticky="WE")


root.mainloop()
#Main loop