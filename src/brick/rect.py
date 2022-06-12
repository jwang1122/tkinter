from playsound import playsound
from gamebase import *

class Circle:
    def __init__(self, x, y, radius, color, canvas):
        self.x1, self.y1 = x, y
        self.x0, self.y0 = x + radius, y+ radius
        self.r = radius
        self.color = color
        self.canvas = canvas
        self.tag = canvas.create_oval(x, y, x + 2*radius, y + 2*radius, fill=color, outline=color)
        self.dx, self.dy = 1, 1
        self.speed = 5

    def __repr__(self):
        return f"({self.x0}, {self.y0}, {self.r})"

    def setRect(self, rects):
        self.rects = rects

    def move(self):
        if self.x1<0 or self.x1 >= Game.width-2*self.r:
            self.dx = -self.dx
        if self.y1<0 or self.y1 >=Game.height-2 *self.r:
            self.dy = -self.dy
        direction = self.collide()
        self.dx *= direction[0]
        self.dy *= direction[1]    
        # if self.y>=self.paddle.y-self.diameter and self.paddle.x <= self.x <= self.paddle.x+self.paddle.width:
        #     self.dy = -self.dy
        dx, dy = self.dx*self.speed, self.dy*self.speed
        self.x1, self.y1 = self.x1 + dx, self.y1 + dy
        self.x0, self.y0 = self.x1 + self.r, self.y1+ self.r
        self.canvas.move(self.tag, dx, dy)

    def collide(self):
        for rect in self.rects:
            if abs(self.x0-rect.left)<=self.r and self.y0>=rect.top and self.y0<=rect.bottom:
                return (-1, 1)
            if abs(self.x0-rect.right)<=self.r and self.y0>=rect.top and self.y0<=rect.bottom:
                return (-1, 1)
            if abs(self.y0-rect.top)<=self.r and self.x0 >= rect.left and self.x0<=rect.right:
                return (1, -1)
            if abs(self.y0-rect.bottom)<=self.r and self.x0 >= rect.left and self.x0<=rect.right:
                return (1, -1)
        return (1, 1)

    def play(self):
        playsound('src/brick/whiff.wav')

    
class Rect:
    def __init__(self, left, top, width, height, color, canvas):
        self.left, self.top = left, top
        self.width, self.height = width, height
        self.color = color
        self.canvas = canvas
        self.right, self.bottom = left + width,  top + height
        self.tag = canvas.create_rectangle(left, top, self.right, self.bottom, fill=color)

    def __repr__(self):
        return f"({self.left}, {self.top}, {self.right}, {self.bottom})"

    def delete(self):
        self.canvas.delete(self.tag)

class Game(BaseFrame):
    def __init__(self, title="Rect Test", width=610, height=400):
        super().__init__(title, width=width, height=height)
        
    def buildWidgets(self):
        self.rects = []
        rect = Rect(120, 100, 75, 20, '#00FFFF', self.canvas)
        self.rects.append(rect)
        rect = Rect(350, 200, 75, 20, '#00FFFF', self.canvas)
        self.rects.append(rect)
        self.circle = Circle(50, 100, 10, '#FF0000', self.canvas)
        self.circle.setRect(self.rects)
        self.loop()

    def loop(self):
        self.circle.move()
        self.after(20, self.loop)

if __name__ == '__main__':
    Game()