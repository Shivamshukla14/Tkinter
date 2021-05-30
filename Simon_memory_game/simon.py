import tkinter as tk
from tkinter import StringVar,ACTIVE,NORMAL,DISABLED
import random

#Define Functions
def pick_sequence():
    
    #generating a non repeating list sequence on comparing with last element of list
    while True:
        value = random.randint(1,4)
        if len(game_sequence) == 0:
            game_sequence.append(value)
            break
        elif game_sequence[-1] != value:
            game_sequence.append(value)
            break

    play_sequence()
            

def play_sequence():
    
    delay = 0
    #looping after each sequence is generated and animating buttons according to sequence value
    for value in game_sequence:
        if value == 1:
            root.after(delay,lambda: animate(white_button))
        elif value == 2:
            root.after(delay,lambda: animate(maginta_button))
        elif value == 3:
            root.after(delay,lambda: animate(cyan_button))
        elif value == 4:
            root.after(delay,lambda: animate(yellow_button))
        #incrementing delay based on difficulty
        delay += time

def animate(button):
    #Changing text of button to playing
    change_label("Playing!")
    #Setting the button color to activebackground color for a period of time
    button.config(state=ACTIVE)
    root.after(time,lambda: button.config(state=NORMAL))

def press(value):
    #appending game_sequnce list according to user presses the button
    player_sequence.append(value)

    #matching the no of game_sequence to no. of player sequence value
    if len(game_sequence) == len(player_sequence):
        check_round()
        disable()
    else:
        enable()

def disable():
    white_button.config(state=DISABLED)
    cyan_button.config(state=DISABLED)
    yellow_button.config(state=DISABLED)
    maginta_button.config(state=DISABLED)

def enable():
    white_button.config(state=NORMAL)
    cyan_button.config(state=NORMAL)
    yellow_button.config(state=NORMAL)
    maginta_button.config(state=NORMAL)

def check_round():
    global player_sequence
    global game_sequence
    global score
    #comparing game_sequence list with player_sequence list
    if game_sequence == player_sequence:
        change_label("Correct!")
        root.after(1000,test)
        enable()
        score += len(game_sequence) + int(1000/time)
        score_label.config(text="Score: " + str(score))
        player_sequence = []
    else:
        change_label("Wrong!")
        root.after(1000,lambda:change_label("New Game"))
        player_sequence = []
        game_sequence = []
        score = 0
        score_label.config(text="Score: " + str(score))
        start_button.config(state=NORMAL)

def difficulty_level():
    global time
    if difficulty.get() == "Easy":
        time = 1000
    elif difficulty.get() == "Medium":
        time = 500
    else:
        time = 200


def change_label(message):
    #Changing the label of button based on state of the game
    start_button.config(text=message)
    if message == "Correct!":
        start_button.config(bg="light green")
        root.after(1000,lambda: start_button.config(bg="white"))
    elif message == "Wrong!":
        start_button.config(bg="Red")
        root.after(1000,lambda: start_button.config(bg="white"))
    else:
        start_button.config(bg="White")

def test():
    pick_sequence()
    start_button.config(state=DISABLED)

#Define colors and variables
root_color = "#23796f"
white_color = "#cacfd1"
white_light_color = "#f5f6f6"
maginta_color = "#8d21a1"
maginta_light_color = "#ea05ed"
cyan_color = "#079598"
cyan_light_color = "#01ecec"
yellow_color = "#a4a80e"
yellow_light_color = "#e4e503"
game_sequence = []
player_sequence = []
time = 500
score = 0
font_fam = ("Arial",12)
radio_font = ("Arial",10)

#Define window
root = tk.Tk()
root.title("Simons-Memory game")
root.iconbitmap("images/Simon.ico")
root.geometry("400x440")
root.resizable(0,0)
root.config(bg=root_color)

#Define Frames
input_frame = tk.Frame(root,bg=root_color)
output_frame = tk.Frame(root)
input_frame.pack()
output_frame.pack()

#Define layout
#Input frame
start_button = tk.Button(input_frame,text="Start Game!",font=font_fam,command=test)
score_label = tk.Label(input_frame,text="Score: " + str(score),font=font_fam,bg=root_color)
start_button.grid(row=0,column=0,pady=(10,20),padx=20,ipadx=20)
score_label.grid(row=0,column=1,padx=20)

#output frame
white_button = tk.Button(output_frame,bg=white_color,activebackground=white_light_color,width=17,height=8,bd=3,command=lambda:press(1),state=DISABLED)
maginta_button = tk.Button(output_frame,bg=maginta_color,activebackground=maginta_light_color,width=17,height=8,bd=3,command=lambda:press(2),state=DISABLED)
cyan_button = tk.Button(output_frame,bg=cyan_color,activebackground=cyan_light_color,width=17,height=8,bd=3,command=lambda:press(3),state=DISABLED)
yellow_button = tk.Button(output_frame,bg=yellow_color,activebackground=yellow_light_color,width=17,height=8,bd=3,command=lambda:press(4),state=DISABLED)
white_button.grid(row=0,column=0,columnspan=2,padx=(20,10),pady=(20,10))
maginta_button.grid(row=0,column=2,columnspan=2,padx=(10,20),pady=(20,10))
cyan_button.grid(row=1,column=0,columnspan=2,padx=(20,10),pady=(10,20))
yellow_button.grid(row=1,column=2,columnspan=2,padx=(10,20),pady=(10,20))

tk.Label(output_frame,text="Difficulty:",font=radio_font).grid(row=2,column=0)

difficulty = StringVar()
difficulty.set("Medium")
tk.Radiobutton(output_frame,text="Easy",font=radio_font,variable=difficulty,value="Easy",command=difficulty_level).grid(row=2,column=1)
tk.Radiobutton(output_frame,text="Medium",font=radio_font,variable=difficulty,value="Medium",command=difficulty_level).grid(row=2,column=2)
tk.Radiobutton(output_frame,text="Hard",font=radio_font,variable=difficulty,value="Hard",command=difficulty_level).grid(row=2,column=3)
root.mainloop()
#Call the mainloop