# the pyautoGUi can send virtual keypresses and mouse clicks 
# to windows,

# Controlling Mouse Movement
# the mouse functions of pyAutoGUI use x- and y- coordinates ; 
# ex : 
#              x
# #(0,0)----------------(1919,0)
#      |                |
#  y   |                |
#      |                |
#(0,1079 ---------------(1919,1079)

# the resolution is how many pixels wide and tall your secreen is

import pyautogui
import time
#####################
# wh = pyautogui.size()
# print(wh)
# # output : Size(width=1366, height=768)
# print(wh.height)  # Output : 1366
# print(wh.height)  # Output : 768
#############################################
# Moving the Mouse : 
# import pyautogui
# for i in range(10):
#     pyautogui.moveTo(100,100, duration=0.25)
#     pyautogui.moveTo(200,100, duration=0.25)
#     pyautogui.moveTo(200,200, duration=0.25)
#     pyautogui.moveTo(100,200, duration=0.25)

#############################################
# for i in range(10):
#     pyautogui.move(100,0,duration=0.25)
#     pyautogui.move(0,100,duration=0.25)
#     pyautogui.move(-100,0,duration=0.25)
#     pyautogui.move(0,-100,duration=0.25)

###############################################
# Getting the mouse Postition

# print(pyautogui.position())
# # Point(x=587, y=50)
# pyautogui.moveTo(587,50, duration=0.25)
################################################
# Clicking the Mouse 
# pyautogui.click(587, 50) # Move mouse to (587, 50) and click.and
################################################
# Draggin the Mouse  - Dragging means moving the mouse while holding down one of the mouse buttons
# check the spiralDraw.py 
#################################
# # Scrolling the Mouse : 
# pyautogui.scroll(200)
# # it will scroll down if the mouse is on the text 
##################################
# # gettng the mouse infos 
# print(pyautogui.mouseInfo())
# # this will generate all kind of infos about the mouse 
#####################################
# # getting a screenshot: 
# im = pyautogui.screenshot()
#####################################
# # Analyzing the screenshot
# print(pyautogui.pixel(0,0)) # get the color of a new pixel
####################################
# # Image recognition # you can make pyautoGui to click by the help of a photo
# b = pyautogui.locateOnScreen('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Controlling_keyboard_mouse\\minimize.png')
# print(b)
# # output : Box(left=0, top=731, width=52, height=37)
# pyautogui.click((0,731,52,37))
##################################
# Manipulatin windows :
# fw = pyautogui.getActiveWindow()
# print(fw)
# # Output :<Win32Window left="0", top="0", width="683", height="728", title="test.py - Python - Visual Studio Code">
# print(fw.isMinimized) # output : False
# print(fw.isActive) # output : True
# fw.maximize() # maximies the window
# time.sleep(2)
# fw.restore() # undoes a minimize\maximise action
#############
# Controlling the Keyboard 
# print(pyautogui.position())
# pyautogui.click(185,302)
# pyautogui.write('Hello, World!')
########################
# # Key Names
# pyautogui.write(['a','b','left','left','X','Y'])
# # output : pyautogui.write(['a','b','left','left','X','Y']XYab)
###########################
# # Pressing and releasing the keyboard
# pyautogui.keyDown('shift')
#####################################
# # hotkey combination : 
# pyautogui.hotkey('ctrl','c')
####################################
# Setting up ou GUI automation scrips 

# Use the same screen resolution each time you run a script
# the windows should be always maximiezed
# add generous pauses
# use locateOnScreen() to find buttons and menus to click 
# rather than relying on XY axis
# use getWindowsWithTitle() to ensure the script is clicking on it
# and use activate() to put the window in the foreground()
# supervise the script

# put a pause at the start of your script , ptyautoGUI() has 
# a sleep function  

import pyautogui
pyautogui.sleep(3) # pauses the program for 3 seconds 
pyautogui.countdown(10)
print('starting in', end='')
pyautogui.countdown(3)
# Starting in 3 2 1 .....





