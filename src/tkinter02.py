"""
Add lable on window
"""
import tkinter as tk

# Create a window
root = tk.Tk()

root.title("My First Window")
root.geometry('600x400') # '<width>x<height>'
tk.Label(root, text="Hello, the world!").pack() # put label on root
tk.Label(root, text="Hello, John").pack() # put label on root
tk.Label(root, text="Hello, Hongkai").pack() # put label on root
# keep window open
root.mainloop()