from tkinter import *

class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x, self.y = x, y
        self.diameter = 20
        self.ball = canvas.create_oval(self.x, self.y, self.x+self.diameter, self.y+self.diameter, fill='yellow')
        self.speed = (0,1)

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.canvas.move(self.ball, self.x, self.y)

    
class Game(Frame):
    root = Tk()
    def __init__(self):
        super().__init__(Game.root)
        self.width = 610
        self.height = 400
        self.canvas = Canvas(self, bg='#D6D1F5', width = self.width , height=self.height)
        self.canvas.pack()
        self.pack()
        self.ball = Ball(self.canvas,0,0)
        self.loop()

    def loop(self):
        self.ball.move()
        self.after(200, self.loop)

if __name__ == '__main__':
    Game().mainloop()