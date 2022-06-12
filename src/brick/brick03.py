from tkinterbase import *

class Brick:
    width, height = 75, 20
    color = ('#8FE1A2','#ED639E','#4535AA')
    def __init__(self, canvas, left, top):
        self.canvas = canvas
        self.left, self.top = left, top
        self.colors = [[self.color[i] for i in range(3)] for j in range(8)]
    
    def draw(self):
        for i in range(len(self.colors)):
            for j in range(len(self.colors[i])):
                color = self.colors[i][j]
                x,y = i*self.width+5,j*self.height+40
                self.canvas.create_rectangle(x,y,x + self.width,y+self.height,fill=color)

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