"""
This program creates the Nerve of Steel game, where players stand then the players sit down
after a certain amount of random time set (5-25 seconds) set by the program

"""
import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import ImageTk# the pillow library makes it easy to display images
import random as rd #random number generator for our program
import tkinter as tk #alloiws to open imagebox which contains our image
from urllib.request import urlopen #reads Image URLs


def timesUp (): 
    
    print ('Times Up! Last to sit down wins!')
    root = tk.Tk()
    u = urlopen("https://deadline.com/wp-content/uploads/2023/01/times-up-halt-operations.jpg?w=681&h=383&crop=1")
    #users may not have the image dowloaded into their system; this code reads an IMGUrl and outputs it in a tKinter box
    rawData = u.read()
    u.close()
    photo = ImageTk.PhotoImage(data = rawData)
    label = tk.Label(image = photo)
    label.image = photo
    label.pack()
    root.mainloop()

print ('Players Stand!')
timer = rd.randint(5,25)
time.sleep(timer)
timesUp()







 
