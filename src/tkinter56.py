import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Using Frame")

frame = tk.LabelFrame(root, text='My Frame', padx=5, pady=5)
frame.pack(fill=tk.BOTH, padx=10, pady=10)

tk.Button(frame, text="Do nothing").pack()

root.mainloop()