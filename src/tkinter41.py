"""
plot chart dynamically
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
 
fig = Figure(figsize = (9, 6), facecolor = "white")
 
axis = fig.add_subplot(111)
x_values = np.array([1,2,3,4,5,6,7])
axis.plot(x_values, x_values, "-r")
axis.plot(x_values, x_values ** 2, "--g")
axis.grid()
 
root = tk.Tk()
 
tk.Label(root, text = "x =" ).grid(row = 0, column = 0)
tk.Label(root, text = "y =" ).grid(row = 1, column = 0)
 
x = tk.DoubleVar()
y = tk.DoubleVar()
 
x_entry = tk.Entry(root, textvariable = x).grid(row = 0, column = 1)
y_entry = tk.Entry(root, textvariable = y).grid(row = 1, column = 1)
 

def plotgraphs():
    axis.plot(x.get(), y.get(), "ko")
     
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas._tkcanvas.grid(row = 2, column = 1)
 
def newGraph():
    axis.clear()
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas._tkcanvas.grid(row = 2, column = 1)

tk.Button(root, text = "Add", command = newGraph).grid(row = 0, column = 2)
tk.Button(root, text = "New Graphs", command = newGraph).grid(row = 0, column = 2)
tk.Button(root, text = "Plot", command = plotgraphs).grid(row = 1, column = 2)
 
canvas = FigureCanvasTkAgg(fig, master = root)
canvas._tkcanvas.grid(row = 2, column = 1)
 
root.mainloop()