from tkinter import *

class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x, self.y = x, y
        self.diameter = 20
        self.ball = canvas.create_oval(self.x, self.y, self.x+self.diameter, self.y+self.diameter, fill='yellow')
        self.speed = 5
        self.dx=1
        self.dy=1

    def move(self):
        if self.x<0 or self.x >= Game.width-self.diameter:
            self.dx = -self.dx
        if self.y<0 or self.y >=Game.height-self.diameter:
            self.dy = -self.dy
        dx, dy = self.dx*self.speed, self.dy*self.speed
        self.x, self.y = self.x + dx, self.y + dy
        self.canvas.move(self.ball, dx, dy)

    
class Game(Frame):
    width = 610
    height = 400
    root = Tk()
    def __init__(self):
        super().__init__(Game.root)
        self.canvas = Canvas(self, bg='#D6D1F5', width = self.width , height=self.height)
        self.canvas.pack()
        self.pack()
        self.ball = Ball(self.canvas,0,0)
        self.loop()

    def loop(self):
        self.ball.move()
        self.after(20, self.loop)

if __name__ == '__main__':
    Game().mainloop()