from tkinterbase import *

class Brick:
    width, height = 75, 20
    def __init__(self, canvas, left, top):
        self.canvas = canvas
        self.left, self.top = left, top
        self.color = '#00FFFF'
    
    def draw(self):
        self.canvas.create_rectangle(
            self.left,self.top,
            self.left + self.width,
            self.top + self.height,
            fill=self.color)

class Game(BaseWindow):
    def __init__(self, title="Hit Brick", width=610, height=400):
        self.width = width
        self.height = height
        super().__init__(title, width=width, height=height)

    def buildWidgets(self):
        self.canvas = Canvas(self.root, bg='#D6D1F5', width=self.width, height=self.height)
        self.canvas.pack()
        brick=Brick(self.canvas, 0,0)
        brick.draw()


if __name__ == '__main__':
    Game()