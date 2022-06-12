"""
add button on window
"""
import tkinter as tk

def do():
    print("You clicked me.")

# Create a window
root = tk.Tk()

root.title("My Window")
root.geometry('600x400') # '<width>x<height>'

tk.Button(root, text="Click Me", command=do, pady=5).pack()
tk.Button(root, text="Quit", height=2, width=5, command=root.destroy, pady=5).pack()
root.mainloop()