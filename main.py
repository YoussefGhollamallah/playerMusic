from pygame import mixer
from tkinter import *
import os

root = Tk()
root.title('Music player')

def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

def pausesong():
    mixer.music.pause()

def stopsong():
    mixer.music.stop()

def resumesong():
    mixer.music.unpause()

def set_volume(value):
    volume = float(value) / 100
    mixer.music.set_volume(volume)

def loop_song():
    mixer.music.play(loops=-1)

mixer.init()
playlist = Listbox(root, selectmode=SINGLE, bg="#032a55", fg="white", font=('arial', 25), width=50)
playlist.grid(columnspan=5)

# Change the current directory to where your MP3 files are located
os.chdir('.\musiques')

# Filter only MP3 files
songs = [s for s in os.listdir() if s.lower().endswith('.mp3')]

for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text="Play", command=playsong)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.grid(row=1, column=1)

stopbtn = Button(root, text="Stop", command=stopsong)
stopbtn.grid(row=1, column=2)

volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Volume", command=set_volume)
volume_scale.set(50)
volume_scale.grid(row=2, column=0, columnspan=4)

loopbtn = Button(root, text="Aléatoire", command=loop_song)
loopbtn.grid(row=3, column=0, columnspan=4)

mainloop()
