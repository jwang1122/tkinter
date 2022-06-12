"""
using tk.Frame
"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        root = tk.Tk()
        root.geometry('1024x768+300+100') # top-left position at (300,100)
        super().__init__(root)
        self.master = root
        self.pack()
        self.create_widgets()
        root.mainloop()


    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.bind('<Enter>', self.turnBlue)
        self.hi_there.pack()

        self.text = tk.Text(self.master)
        self.quit = tk.Button(self, text="QUIT", fg="red", bg='yellow',
                              command=self.master.destroy)
        self.text.pack(fill=tk.BOTH)
        self.quit.pack()

    def say_hi(self):
        self.text.insert("1.0","hi there, everyone!")

    def turnBlue(self, event):
        event.widget['activeforeground'] = 'white'
        event.widget['activebackground'] = 'blue'

if __name__ == '__main__':   
    Application()
