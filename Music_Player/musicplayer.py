import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music player")
musicplayer.geometry("450x350")

list1 = askdirectory()
os.chdir(list1)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer,font="Helventica 12 bold",bg="yellow",selectmode=tkr.SINGLE)

font_effect = ("Helventica 12 bold")

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicplayer,font=font_effect,bg="red",fg="white",text="PLAY",command=play)
Button2 = tkr.Button(musicplayer,font=font_effect,bg="blue",fg="white",text="STOP",command=stop)
Button3 = tkr.Button(musicplayer,font=font_effect,bg="orange",fg="white",text="PAUSE",command=pause)
Button4 = tkr.Button(musicplayer,font=font_effect,bg="green",fg="white",text="UNPAUSE",command=unpause)

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,textvariable=var,font=font_effect)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()
