import tkinter as tk

def number(n):
    print(f"button {n} is clicked.")

root = tk.Tk()

btn1= tk.Button(root, text="1", padx=40, command=lambda: number(1))
# btn1= tk.Button(root, text="1", padx=40, command=number(1))
btn1.pack()

root.mainloop()