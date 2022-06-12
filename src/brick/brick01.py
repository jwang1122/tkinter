from tkinterbase import *

class Game(BaseWindow):
    def __init__(self, title="Hit Brick", width=610, height=400):
        self.width = width
        self.height = height
        super().__init__(title, width=width, height=height)

    def buildWidgets(self):
        self.canvas = Canvas(self.root, bg='#D6D1F5', width=self.width, height=self.height)
        self.canvas.pack()

if __name__ == '__main__':
    Game()