"""
Add labels on window use pack() function attributes such as
before, after, anchor, fill, padx, pady, ipadx, ipady,side
"""

import tkinter as tk

# Create a window
root = tk.Tk()

root.title("My Window")
root.geometry('600x400') # '<width>x<height>'
tk.Label(root, text="side=right").pack(side='right') # put label on root
lbl1 = tk.Label(root, text="Hello, John")
lbl1.pack() # put label on root
tk.Label(root, text="before Hello, John").pack(before=lbl1) # put label on root
tk.Label(root, text="West Label", padx=20, bg='#91C5F2').pack(anchor='w')
tk.Label(root, text='Fill label', bg='yellow', fg='red', pady=10).pack(fill='x')

# keep window open
root.mainloop()