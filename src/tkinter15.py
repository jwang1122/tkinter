"""
using progress bar
"""
# importing tkinter module
from tkinter import * 
from tkinter.ttk import *
import time


# creating tkinter window
root = Tk()
root.title("Window")

# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def bar():
    b1["state"] = "disabled"
    progress['value'] = 0
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
	
    progress['value'] = 100
    b1["state"] = "normal"

progress.pack(pady = 10)

# This button will initialize
# the progress bar
b1 = Button(root, text = 'Start', command = bar) # donot use .pack() here if you want to use the b1 object!! 
b1.pack(pady = 10)

# infinite loop
mainloop()
