"""
add button
"""
import tkinter as tk 
parent = tk.Tk() 
parent.title('Title - button') 
parent.geometry('600x300')
tk.Button(parent, text='Click Me', padx=10, pady=8).pack() # padding
quitBtn = tk.Button(parent, text='Quit', height=1, width=20, command=parent.destroy) 
quitBtn.pack() 
parent.mainloop()
