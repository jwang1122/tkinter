import tkinter as tk

root = tk.Tk()
root.title("ComboBox")

root.geometry('200x200')

options = ["Monday","Tuesday",'Wednesday','Thursday','Friday','Saturday','Sunday']
clicked = tk.StringVar()
clicked.set(options[0])

tk.OptionMenu(root, clicked, *options).pack()
tk.Label(root, textvariable=clicked).pack()

root.mainloop()