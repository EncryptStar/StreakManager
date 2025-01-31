'''
Currently for testing purposes.
Upon completion of main.py, use this to store functions for GUI
'''
import tkinter as tk
import os

imageName = "NoSuccess.jpg"

def createWindow():
    root = tk.Tk()
    root.title("Test GUI")
    root.minsize(200,200)
    root.geometry("900x600+100+100")

    # Text Elements
    tk.Label(root, text="The pain of failure is less than the pain of not trying").pack()
    tk.Label(root, text="- Some wise old dude").pack()
    image = tk.PhotoImage(file=os.getcwd()+"\\assets\\"+imageName)
    tk.Label(root, image=image).pack()

    root.mainloop()

createWindow()
