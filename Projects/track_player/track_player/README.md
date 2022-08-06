# Basic Meditation track player using python and Tkinter

The whole idea began when I wanted to play some mp3 application using a mainstream application application yet it didn’t convince me enough to use it.

Also the main problem here to solve it that I needed to keep track of what i have been listening before, to finish the playlist of the meditation journey without getting lost. 

[insert image here]

So the libraries that has been used in this challenge are : 

- Tkinter
    
    Tkinter is the de facto way in Python to **create Graphical User interfaces (GUIs)**
    
- Mixer
    
    In order to play music/audio files mixer is used (**pygame module for loading and playing sounds**). This module contains classes for loading Sound objects and controlling playback
    
- Pickle
    
    The `[pickle](https://docs.python.org/3/library/pickle.html#module-pickle)`module implements binary protocols for serializing and de-serializing a Python object structure. *“Pickling”*is the process whereby a Python object hierarchy is converted into a byte stream.
    

First of all we declare the window, its name, and its resolution by : 

```python
root = Tk()
root.title("Meditation Player")

root.configure(background="#424651")
# root.resizable(True,True)
root.geometry("1193x581")
```

staring the mixer : 

```python
mixer.init()
```

We can check if the window is showing or not by :

```python
root.mainloop()
```

we initialize the list box partition by : 

```python
song_box = Listbox(root, bg = "white", fg = "#424651", width=100, selectbackground='#00FFFF', selectforeground="#424651")
song_box.pack(pady=(130, 0))
```

And we have to use the pack() function to be revealed on the window. 

This list box has many functionalities or many ways of functioning , for example: when we load a new track to Listbox, the track will be inserted at the END of the list which will give us the ability to check whether the list is empty or not by :

```python
if song_box.get(0,END): 
	# put code here
```

After adding the list box now we add the buttons simply by : 

giving these buttons some sort of images 

```python
pause_btn_img = PhotoImage(file = 'pause.png')
play_btn_img = PhotoImage(file = 'resume.png')
stop_btn_img = PhotoImage(file = 'stop.png')
```

then we acutally create the buttons by the help of the button function:

```python
pause_btn = Button(controls_frame,image =pause_btn_img,borderwidth=0,background="#424651", activebackground="#424651", command=lambda: pause(paused))
play_btn = Button(controls_frame,image =play_btn_img,borderwidth=0,background="#424651",activebackground="#424651", command=lambda: play(paused))
stop_btn = Button(controls_frame,image =stop_btn_img,borderwidth=0,background="#424651",activebackground="#424651", command=stop)
```

Notice here that we didn’t make these buttons parts of the root() window yet we added them in the control frame, so this control frame purpose is to put these buttons on a grid to add some readability and nice appearance to the user.

so the control frame will belong to the main root() window : 

```python
controls_frame = Frame(root,borderwidth=0,background="#424651")
controls_frame.pack(pady=20)
```

then we place these buttons on the correspondent frame partition : 

```python
pause_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
stop_btn.grid(row=0,column=3,padx=10)
```

so in the button() function there is an attribute where you pass a function to it 

```html
command=lambda: pause(paused)
```

Now we create these functions : 

```python
def add_song():
    song = filedialog.askopenfilename(initialdir = 'Waking Up - A Meditation Course/', title ='Choose a song', filetypes = (('mp3 Files','*.mp3'), ))
    # We need to change the look of the link 
    # and make it only the song name
    song = song.replace("--Directory of the tracks--", "")
    song = song.replace(".mp3", "")

    # Insert the song at the end of the list box
    song_box.insert(END, song)
```

the add_song() function, we filter and select only mp3 files with the help of the filedialog library, also we can set the initial directory.

Then we can strip the the whole directory to make the list box show only the title of the track.

```python
def play(is_paused):
    global paused 
    paused = is_paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        song = song_box.get(ACTIVE)
        song = f"--Directory of the tracks--{song}.mp3"
        mixer.music.load(song)
        mixer.music.play(loops=0)
```

the play function takes an argument which is a global variable that can be used in and outside functions, the reason for this is to check whether this variable was altered by a function and that will help us define which state the track is on, maybe it is paused or unpaused so the global variable helps define that state. 

Now we head out to the saving tracks and showing them on the window : 

```python
T = Text(root, height = 5, width = 52)
l = Label(root, text = f"أخر جلسة", font=("Noto Kufi Arabic", 20), background="#424651", fg="#00FFFF")
l.pack()
x = Text(root, height = 5, width = 52)
h = Label(root, text = f"{history[-1]}", font=("Montserrat", 20), background="#424651", fg="#00FFFF")
h.pack()
```

and in order to save date in to a pickle file we can dictate what will the window do once it is closed so:

```python
def on_closing():
    if song_box.get(0,END):
        song = song_box.get(ACTIVE)
        history.append(song)
        pickle.dump( history, open( "history.p", "wb" ) )
    root.destroy()
```

and we add this to the actually on closing event : 

```python
root.protocol("WM_DELETE_WINDOW", on_closing)
```