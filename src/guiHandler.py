'''
Currently for testing purposes.
Upon completion of main.py, use this to store functions for GUI
'''

import tkinter as tk

root = tk.Tk()
root.title("Test GUI")
root.minsize(200,200)
root.geometry("300x300+50+50")

# Text Elements
tk.Label(root, text="The pain of failure is less than the pain of not trying").pack()
tk.Label(root, text="- Some wise old dude").pack()

root.mainloop()
