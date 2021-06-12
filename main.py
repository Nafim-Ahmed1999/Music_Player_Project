#Istalling the modules

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

#creating the application window

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

#creating a directory
directory = askdirectory()
os.chdir(directory)

#song list box
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font ="Helvetica 12 bold", bg="yellow",selectmode= tkr.SINGLE)

#add for loop
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

#functions for initialising buttons
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

#buttons colour
Button1 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="PLAY",command=play,bg="red")
Button2 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="STOP",command=ExitMusicPlayer,bg="purple")
Button3 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="PAUSE",command=pause,bg="green")
Button4 = tkr.Button(musicplayer,width=5,height=3, font="Helvetica 12 bold",text="UNPAUSE",command=unpause,bg="blue")

#Displaying song title
var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")

musicplayer.mainloop()
