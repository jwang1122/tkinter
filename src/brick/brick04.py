from tkinterbase import *

class Paddle:
    width = 70
    height = 15
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
    
    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill="white")

class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self):
        self.canvas.create_oval(200,300,210,310,fill="white")

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
                self.canvas.create_rectangle(x+1,y+1,x + self.width+1,y+self.height+1,outline='white')

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
        self.ball = Ball(self.canvas)
        self.ball.draw()
        self.paddle = Paddle(self.canvas, 170, 310)
        self.paddle.draw()

if __name__ == '__main__':
    Game()