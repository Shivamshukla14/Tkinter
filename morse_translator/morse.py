import tkinter as tk
from tkinter import END,IntVar, Toplevel,DISABLED,NORMAL
from playsound import playsound
from PIL import Image, ImageTk

#Define functions
def convert_text():
    if language.get() == 0:
        morse_text()
    elif language.get() == 1:
        english_text()

def morse_text():
    #converting english to morse code
    #initializing empty string
    morse = ""
    #getting user_input
    text = text_field_input.get("1.0",END)
    text = text.lower()
    #removing characters from input which are not present in english_to_morse dictonary
    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, "")
    #creating list of word by using split function as empty place
    wordlist = text.split(" ")
    #create list of letters in a word in wordlist
    for word in wordlist:
        letters = list(word)
        #checking each item of list as key in english to morse dict
        for letter in letters:
            morse_key = english_to_morse[letter]
            #adding the key value stored in morse_key variable to morse variable
            morse += morse_key
            #adding space after every value
            morse += " "
        #adding pipe after a word is completed
        morse += "|"

    #Inserting the final morse value in output box
    text_field_output.insert("1.0",morse)


def english_text():
    #converting morse to english
    #initializing an empty string variable
    english = ""
    #getting user input
    text = text_field_input.get("1.0",END)
    #removing unwanted characters from the input
    for character in text:
        if character not in morse_to_english.keys():
            text = text.replace(character, "")
    #creating a list of words
    wordlist = text.split("|")
    #creating list of letter from each word in wordlist
    for word in wordlist:
        letters = word.split(" ")
        for letter in letters:
            #storing the key value in a variable
            english_key = morse_to_english[letter]
            #appending each value in empty string
            english += english_key
        #creating space after each word
        english += " "

    text_field_output.insert("1.0",english)

def play():
    if language.get() == 0:
        text = text_field_output.get("1.0",END)
    elif language.get() == 1:
        text = text_field_input.get("1.0",END) 

    for i in text:
        if i == '.':
            playsound("music/dot.mp3")
            root.after(200)
        elif i == "-":
            playsound("music/dash.mp3")
            root.after(500)
        elif i == " ":
            root.after(700)
        elif i == "|":
            root.after(1000)

def show_guide():
    global morse_img
    global guide
    guide = Toplevel()
    guide.title("Morse-code Guide")
    guide.iconbitmap("images/network.ico")
    guide.geometry("350x400+" + str(root.winfo_x()+500) + "+" +str(root.winfo_y()))
    guide.resizable(0,0)
    guide.config(bg=root_bg)

    morse_img = ImageTk.PhotoImage(Image.open("images/morse_chart.JPG"))
    morse_label = tk.Label(guide,image=morse_img)
    close_button = tk.Button(guide,text="Close",font=button_font,bg=button_color,command=close_opt)
    morse_label.pack(padx=20,pady=(20,0),ipadx=7,ipady=7)
    close_button.pack(padx=5,pady=20,ipady=10,ipadx=30)

    guide_button.config(state=DISABLED)


    guide.mainloop()

def close_opt():
    guide.destroy()
    guide_button.config(state=NORMAL)

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

#Creating a IntVar datatype to store value for radio button
language = IntVar()
#Input frame
text_field_input = tk.Text(input_frame,width=27,height=8,font=button_font,fg=font_color)
radio_english_to_morsh = tk.Radiobutton(input_frame,variable=language,text="English-->Morse code",value=0,font=button_font,bg=frame_bg,activebackground=frame_bg)
radio_morse_to_english = tk.Radiobutton(input_frame,variable=language,text="Morse code-->English",value=1,font=button_font,bg=frame_bg,activebackground=frame_bg)
guide_button = tk.Button(input_frame,text="Guide",bg=button_color,font=button_font,command=show_guide)
text_field_input.grid(row=0,column=1,rowspan=3,padx=5,pady=5)
radio_english_to_morsh.grid(row=0,column=0,padx=5)
radio_morse_to_english.grid(row=1,column=0,padx=5)
guide_button.grid(row=2,column=0,sticky="WE",padx=5)

#Output Frame
text_field_output = tk.Text(output_frame,width=27,height=8,font=button_font,fg=font_color)
convert_button = tk.Button(output_frame,text="Convert",font=button_font,bg=button_color,command=convert_text)
play_button = tk.Button(output_frame,text="Play Morse",font=button_font,bg=button_color,command=play)
clear_button = tk.Button(output_frame,text="Clear",bg=button_color,font=button_font,command=clear_text)
exit_button = tk.Button(output_frame,text="Exit",bg=button_color,font=button_font,command=root.destroy)

text_field_output.grid(row=0,column=1,rowspan=4,padx=5,pady=5)
convert_button.grid(row=0,column=0,padx=5,sticky="WE",ipadx=58)
play_button.grid(row=1,column=0,padx=5,sticky="WE")
clear_button.grid(row=2,column=0,padx=5,sticky="WE")
exit_button.grid(row=3,column=0,padx=5,sticky="WE")


root.mainloop()
#Main loop