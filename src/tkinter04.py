import tkinter as tk

# Create a window
root = tk.Tk()

root.title("My Window")
root.geometry('600x400') # '<width>x<height>'
tk.Label(root, text="side=right").pack(side='right') # put label on root
tk.Label(root, text="side=right 2nd").pack(side='right')
lbl1 = tk.Label(root, text="Hello, John", font=('AR DECODE', 50))
lbl1.pack() # put label on root
tk.Label(root, text="before Hello, John").pack(before=lbl1) # put label on root
tk.Label(root, text="West Label", padx=20, bg='#91C5F2').pack(anchor='w')
tk.Label(root, text='Fill label', font=('Bradley Hand ITC', 20),bg='yellow', fg='red', pady=10).pack(fill='x')
tk.Button(root, text="Click Me place(100,100)").place(x=100,y=100)
# keep window open
root.mainloop()