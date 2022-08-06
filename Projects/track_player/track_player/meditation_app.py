import os 
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer 
from tkinter import messagebox
import pickle

os.chdir("C://Users//ElHassen//Desktop//Meditation")
# open listening history file
history = pickle.load(open("history.p","rb"))
# Create a GUI window 
global paused
paused = False
root = Tk()
root.title("Meditation Player")

root.configure(background="#424651")
# root.resizable(True,True)
root.geometry("1193x581")
mixer.init()
#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir = 'Waking Up - A Meditation Course/', title ='Choose a song', filetypes = (('mp3 Files','*.mp3'), ))
    # We need to change the look of the link 
    # and make it only the song name
    song = song.replace("C:/Users/ElHassen/Desktop/Meditation/Waking Up - A Meditation Course/Practice/Introductory Course/", "")
    song = song.replace(".mp3", "")

    # Insert the song at the end of the list box
    song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir = 'Waking Up - A Meditation Course/', title ='Choose a song', filetypes = (('mp3 Files','*.mp3'), ))
    # loop through all the songs and strip them from
    # the names 
    for song in songs : 
        song = song.replace("C:/Users/ElHassen/Desktop/Meditation/Waking Up - A Meditation Course/Practice/Introductory Course/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END,song)

# Define the play function
def play(is_paused):
    global paused 
    paused = is_paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        song = song_box.get(ACTIVE)
        song = f"C:/Users/ElHassen/Desktop/Meditation/Waking Up - A Meditation Course/Practice/Introductory Course/{song}.mp3"
        mixer.music.load(song)
        mixer.music.play(loops=0)
# Stop the current song 
def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)

def pause(is_paused):
    global paused 
    paused = is_paused
    if not paused:
        mixer.music.pause()
        paused = True

def on_closing():
    if song_box.get(0,END):
        song = song_box.get(ACTIVE)
        history.append(song)
        pickle.dump( history, open( "history.p", "wb" ) )
    root.destroy()


    
vector = PhotoImage(file = "vector.png")
Label(root,pady=500, image=vector, bg = "#424651").pack(side="left")
song_box = Listbox(root, bg = "white", fg = "#424651", width=100, selectbackground='#00FFFF', selectforeground="#424651")
song_box.pack(pady=(130, 0))

pause_btn_img = PhotoImage(file = 'pause.png')
play_btn_img = PhotoImage(file = 'resume.png')
stop_btn_img = PhotoImage(file = 'stop.png')


# Create Player control frames to make the button on a grid
controls_frame = Frame(root,borderwidth=0,background="#424651")
controls_frame.pack(pady=20)

# Create Player control Buttons

pause_btn = Button(controls_frame,image =pause_btn_img,borderwidth=0,background="#424651", activebackground="#424651", command=lambda: pause(paused))
play_btn = Button(controls_frame,image =play_btn_img,borderwidth=0,background="#424651",activebackground="#424651", command=lambda: play(paused))
stop_btn = Button(controls_frame,image =stop_btn_img,borderwidth=0,background="#424651",activebackground="#424651", command=stop)

pause_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
stop_btn.grid(row=0,column=3,padx=10)


T = Text(root, height = 5, width = 52)
l = Label(root, text = f"أخر جلسة", font=("Noto Kufi Arabic", 20), background="#424651", fg="#00FFFF")
l.pack()
x = Text(root, height = 5, width = 52)
h = Label(root, text = f"{history[-1]}", font=("Montserrat", 20), background="#424651", fg="#00FFFF")
h.pack()
# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add "Add Songs" Menu

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Tracks", menu = add_song_menu)
add_song_menu.add_command(label="Add one Track to Playlist", command = add_song)
# Add many tracks
add_song_menu.add_command(label = "Add many tracks to playlist",command = add_many_songs)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()