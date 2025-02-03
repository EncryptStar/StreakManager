'''
Currently for testing purposes.
Upon completion of main.py, use this to store functions for GUI
'''
import tkinter as tk
from os import getcwd

imageName = "DiscreteMeme.png"

def createWindow():
    root = tk.Tk()
    root.title("Test GUI")
    root.minsize(200,200)
    root.geometry("900x600+100+100")

    # Text Elements
    tk.Label(root, text="The pain of failure is less than the pain of not trying").pack()
    tk.Label(root, text="- Some wise old dude").pack()

    # Image Element
    # For the file path, get current directory (assume StreakManager fldr), go to assets fldr, and add imageName
    image = tk.PhotoImage(file=getcwd()+"\\assets\\"+imageName) # WINDOWS ONLY (address this later)
    tk.Label(root, image=image).pack()

    root.mainloop()

createWindow()
