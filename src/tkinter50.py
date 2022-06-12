"""
Grid system
"""
import tkinter as tk
parent = tk.Tk()
parent.title("Grid System")
parent.geometry('600x300')

sideLbl = tk.Label(parent, text="side=right", bg='black', fg='white')
sideLbl.grid(row=0, column=0)
myLabel = tk.Label(parent, text="Label widget")
# myLabel.grid(column=0, row=0) # put label on location (0,0)
myLabel.grid(row=0, column=1)

enterName = "Enter a name: "
firstLbl = tk.Label(parent, text=enterName, bg='pink') # named color
firstLbl.grid(row=1, column=1)
westLbl = tk.Label(parent, text="West Label", bg='#76B8F2') # RGB in Hex
westLbl.grid(row=1, column=2)
ipadLbl = tk.Label(parent, text="Internal Padding", bg='black', fg='white')
ipadLbl.grid(row=2, column=0)
fillLbl = tk.Label(parent, text="Fill Label", width=30, bg='yellow')
fillLbl.grid(row=2, column=1, columnspan=2)

parent.mainloop()
