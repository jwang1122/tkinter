from playsound import playsound
from gamebase import *

class Circle:
    def __init__(self, x, y, radius, color, canvas):
        self.x1, self.y1 = x, y
        self.x0, self.y0 = x + radius, y+ radius
        self.r = radius
        self.x2, self.y2 = x+2*radius, y+2*radius
        self.color = color
        self.canvas = canvas
        self.tag = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=color, outline=color)
    
    def __repr__(self):
        return f"({self.x0}, {self.y0}, {self.r})"

    def setRect(self, rect):
        self.rect = rect

    def move(self, dx, dy):
        if self.collide():
            self.play()
        self.x1, self.y1 = self.x1+dx, self.y1+dy
        self.x2, self.y2 = self.x2+dx, self.y2+dy
        self.x0, self.y0 = self.x1 + self.r, self.y1+ self.r
        self.canvas.move(self.tag, dx, dy)

    def collide(self):
        if abs(self.x0-self.rect.left)<=self.r and self.y1>=self.rect.top and self.y2<=self.rect.bottom:
            return True
        if abs(self.x0-self.rect.right)<=self.r and self.y1>=self.rect.top and self.y2<=self.rect.bottom:
            return True 
        if abs(self.y0-self.rect.top)<=self.r and self.x1 >= self.rect.left and self.x2<=self.rect.right:
            return True
        if abs(self.y0-self.rect.bottom)<=self.r and self.x1 >= self.rect.left and self.x2<=self.rect.right:
            return True
        return False

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
    def __init__(self, title="Rect test", width=610, height=400):
        super().__init__(title, width, height)

    def buildWidgets(self):
        rect = Rect(100, 100, 75, 20, '#00FFFF', self.canvas)
        self.circle = Circle(50, 100, 10, '#FF0000', self.canvas)
        self.circle.setRect(rect)
        self.canvas.focus_set()
        self.canvas.bind('<Left>',lambda _: self.circle.move(-10, 0))
        self.canvas.bind('<Right>',lambda _: self.circle.move(10, 0))
        self.canvas.bind('<Up>',lambda _: self.circle.move(0, -10))
        self.canvas.bind('<Down>',lambda _: self.circle.move(0, 10))
        self.rect1 = Rect(200,200,75,20,'#FFFF00', self.canvas)
        self.canvas.bind('<space>', lambda _:self.rect1.delete())

if __name__ == '__main__':
    Game()