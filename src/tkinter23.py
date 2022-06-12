"""
better version of tkinter22
"""
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
import tkinter.scrolledtext as tkst

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.openBtn = tk.Button(self.master, text='Open a File', command=self.openFile)
        self.openBtn.pack(side="top")
        self.txt = tkst.ScrolledText(self.master, width=40, height=10)
        self.txt.pack(side="bottom")


    def openFile(self):
        self.filename = fd.askopenfilename()
        messagebox.showinfo("Selected File", self.filename)
        with open(self.filename) as f:
            contents = f.read()
        self.txt.insert(tk.INSERT, contents)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Open File Window")
    root.geometry('280x150')
    app = Application(master=root)
    
    app.mainloop()