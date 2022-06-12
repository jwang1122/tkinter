"""
using save file dialog
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
        self.openBtn.place(x=10, y=5)
        self.saveBtn = tk.Button(self.master, text='Save a File', command=self.saveFile)
        self.saveBtn.place(x=100, y=5)
        self.txt = tkst.ScrolledText(self.master, width=40, height=10)
        self.txt.place(x=5, y=30)


    def openFile(self):
        self.filename = fd.askopenfilename()
        messagebox.showinfo("Selected File", self.filename)
        with open(self.filename) as f:
            contents = f.read()
        self.txt.insert(tk.INSERT, contents)

    def saveFile(self):
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        self.file = fd.asksaveasfile(mode='w', filetypes=files, defaultextension=".py")
        self.file.write(self.txt.get(1.0, tk.END))

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Open File Window")
    root.geometry('280x250')
    app = Application(master=root)
    
    app.mainloop()