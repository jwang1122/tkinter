from tkinterbase import *

class Paddle:
    width = 80
    height = 15
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x, self.y = x, y
        self.paddle = self.canvas.create_rectangle(x, y, self.x+self.width, self.y+self.height, fill="#228f6d")
    
    def move(self, speed):
        self.x += speed
        self.canvas.move(self.paddle, speed, 0)

class Ball:
    diameter = 20
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x, self.y = x, y
        self.dx, self.dy = 1, 1
        self.speed = 5
        self.ball = self.canvas.create_oval(x,y,x+Ball.diameter,y+Ball.diameter,fill="white")

    def setPaddle(self, paddle):
        self.paddle = paddle

    def setBrick(self, brick):
        self.brick = brick

    def move(self):
        if self.x<0 or self.x >= Game.width-self.diameter:
            self.dx = -self.dx
        if self.y<0 or self.y >=Game.height-self.diameter:
            self.dy = -self.dy
        if self.y>=self.paddle.y-self.diameter and self.paddle.x <= self.x <= self.paddle.x+self.paddle.width:
            self.dy = -self.dy
        for i in range(len(self.brick.bricks)):
            for j in range(len(self.brick.bricks[i])):
                brick = self.brick.bricks[i][j]
                if self.y <= j*self.brick.height and i*self.brick.width <=self.x <(i+1)*self.brick.width:
                    self.canvas.delete(brick)
                    self.dy = -self.dy
        dx, dy = self.dx*self.speed, self.dy*self.speed
        self.x, self.y = self.x + dx, self.y + dy
        self.canvas.move(self.ball, dx, dy)

class Brick:
    width, height = 75, 20
    color = ('#8FE1A2','#ED639E','#4535AA')
    def __init__(self, canvas, left, top, ball):
        self.canvas = canvas
        self.left, self.top = left, top
        self.ball = ball
        self.colors = [[self.color[i] for i in range(3)] for j in range(8)]
        self.bricks = []
        for i in range(len(self.colors)):
            self.bricks.append([])
            for j in range(len(self.colors[i])):
                color = self.colors[i][j]
                x,y = i*self.width+5,j*self.height+40
                brick = self.canvas.create_rectangle(x,y,x + self.width,y+self.height,fill=color)
                self.bricks[i].append(brick)
                # self.canvas.create_rectangle(x+1,y+1,x + self.width+1,y+self.height+1,outline='white')

    def remove(self, row, col):
        self.canvas.delete(self.bricks[col][row])

class Game(Frame):
    width = 610
    height = 400
    root = Tk()
    def __init__(self):
        super().__init__(Game.root)
        self.canvas = Canvas(self, bg='#D6D1F5', width = self.width , height=self.height)
        self.canvas.pack()
        self.pack()
        self.ball = Ball(self.canvas,100,300)
        self.brick=Brick(self.canvas, 0,0, self.ball)
        self.paddle = Paddle(self.canvas, 170, 310)
        self.ball.setPaddle(self.paddle)
        self.ball.setBrick(self.brick)
        self.canvas.focus_set()
        self.canvas.bind('<Left>',
                         lambda _: self.paddle.move(-10))
        self.canvas.bind('<Right>',
                         lambda _: self.paddle.move(10))
        self.loop()

    def loop(self):
        self.ball.move()
        self.after(20, self.loop)

if __name__ == '__main__':
    Game().mainloop()