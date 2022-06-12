"""
Add label to window
pack() function attributes:
before, after, anchor, fill, padx, pady, ipadx, ipady
"""
import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter")
parent.geometry('600x300')

sideLbl = tk.Label(parent, text="side=right", bg='black', fg='white')
sideLbl.pack(side='right') # start after previous widget and always centered on right border
myLabel = tk.Label(parent, text="Label widget")
# myLabel.grid(column=0, row=0) # put label on location (0,0)
myLabel.pack()
enterName = "Enter a name: "
firstLbl = tk.Label(parent, text=enterName, bg='pink') # named color
firstLbl.pack(before=myLabel, pady=5)
westLbl = tk.Label(parent, text="West Label", bg='#76B8F2') # RGB in Hex
westLbl.pack(anchor='w') # must be n, ne, e, se, s, sw, w, nw, or center
ipadLbl = tk.Label(parent, text="Internal Padding", bg='black', fg='white')
ipadLbl.pack(ipadx=20, ipady=20) # integer for pixels
fillLbl = tk.Label(parent, text="Fill Label", bg='yellow')
fillLbl.pack(fill='x', pady=10) # fill in x direction, x or y

parent.mainloop()
