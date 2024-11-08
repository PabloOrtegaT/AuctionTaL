from tkinter import *
import  missions.general as general
from pynput import keyboard
import threading

def init():
    global root
    global auctionTracker

def on_press(key):
    if key == keyboard.Key.f8:
        root.destroy()
        
def selectOption():
    newArray = []
    if (auctionTracker.get()):
        newArray.append('Auction')

    global charactersToPlay 
    charactersToPlay = newArray

def startFarming():
    #root.iconify()
    for char in charactersToPlay:
        if char == 'Auction':
            general.run()

def generateOptions(frame):
    Checkbutton(frame, text="Auction", variable=auctionTracker, 
            onvalue=True, offvalue=False, command=selectOption, bg="#d4d4d4").pack(anchor="w")

    startFarm = threading.Thread(target=startFarming)
    startFarm.daemon = True
    Button(frame, text="Start", command=startFarm.start).pack(side=RIGHT)

root = Tk()
init()
auctionTracker = IntVar()
charactersToPlay = []

listener = keyboard.Listener(
    on_press=on_press)
threading.Thread(target=listener.start())


root.title("This is not a bot")
# root.iconphoto("metalmine2.png")
root.resizable(0, 0)
root.geometry("500x700")
root.config(bg="#c7c7c7", bd=5)
# Create a Frame that will be child of root
app = Frame(root)
# Pack the previous frame inside the root
app.pack(fill="both", expand=1)
# Give a size to the frame and change the color
app.config(bg="#d4d4d4", bd=10)
generateOptions(app)

root.update()
root.mainloop()