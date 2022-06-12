from tkinter import *
from tkinter import ttk

root = Tk()

#Tab Widget
tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=TRUE)

frame1 = ttk.Frame(tabs)
Label(frame1, text='Tab - 1').pack(pady=10)

frame2 = ttk.Frame(tabs)
Label(frame2, text='Tab - 2').pack(pady=10)

tabs.add(frame1, text="Tab One")
tabs.add(frame2, text="Tab Two")

root.geometry("400x240")
root.title("华夏中文学校")
root.mainloop()