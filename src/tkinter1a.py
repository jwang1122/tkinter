import tkinter as tk

root = tk.Tk()
root.title("Hello")
root.geometry('200x40')
tk.Label(root, text="Hello, the world!", bg='yellow').pack()
root.mainloop()
