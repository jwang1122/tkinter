'''
using canvas draw pie chart
'''
from tkinter import *
 
root = Tk()
 
frame=Frame(root,width=300,height=300)
frame.pack(expand = True, fill=BOTH)
 
canvas = Canvas(frame,bg='white', width = 300,height = 300)
 
coordinates = 20, 50, 210, 230
arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
 
canvas.pack(expand = True, fill = BOTH)
 
root.mainloop()