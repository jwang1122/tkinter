from tkinter import *

class BaseFrame(Frame):
    root = Tk()
    def __init__(self, title="Game", width=1024, height=768):
        super().__init__(self.root)
        BaseFrame.width = width
        BaseFrame.height = height
        self.root.title(title)
        self.root.geometry('x'.join([str(width), str(height)])) # Super VGA monitor
        self.root.iconbitmap("src/images/blackjack.ico")
        self.canvas = Canvas(self, bg='#D6D1F5',width=width,height=height,)
        self.canvas.pack()
        self.pack()
        self.buildWidgets()
        self.mainloop()
    
    def buildWidgets(self):
        pass

if __name__ == '__main__':
    BaseFrame()