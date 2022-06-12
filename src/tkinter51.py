"""
Place system
"""
import tkinter as tk
parent = tk.Tk()
parent.title("Grid System")
parent.geometry('600x300')

sideLbl = tk.Label(parent, text="side=right", bg='black', fg='white')
sideLbl.place(x=10, y=10)
myLabel = tk.Label(parent, text="Label widget")
# myLabel.grid(column=0, row=0) # put label on location (0,0)
myLabel.place(x=100, y=10)

enterName = "Enter a name: "
firstLbl = tk.Label(parent, text=enterName, bg='pink') # named color
firstLbl.place(x=10, y=30)
westLbl = tk.Label(parent, text="West Label", bg='#76B8F2') # RGB in Hex
westLbl.place(x=30, y=60)
ipadLbl = tk.Label(parent, text="Internal Padding", bg='black', fg='white')
ipadLbl.place(x=30, y=120)
fillLbl = tk.Label(parent, text="Fill Label", width=30, bg='yellow')
fillLbl.place(x=0, y=90)

parent.mainloop()