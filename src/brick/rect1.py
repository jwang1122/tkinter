from gamebase import *

class Circle:
    def __init__(self, x, y, radius, color, canvas):
        self.x, self.y = x, y
        self.r = radius
        self.color = color
        self.canvas = canvas
        self.tag = canvas.create_oval(x-self.r, y-self.r, x+self.r, y+self.r, fill=color, outline=color)
    
    def setRect(self, rect):
        self.rect = rect

    def move(self, dx, dy):
        self.canvas.move(self.tag, dx, dy)

    def collide(self):
        pass
    
class Rect:
    def __init__(self, left, top, width, height, color, canvas):
        self.left, self.top = left, top
        self.width, self.height = width, height
        self.color = color
        self.canvas = canvas
        self.right, self.bottom = left + width,  top + height
        self.tag = canvas.create_rectangle(left, top, self.right, self.bottom, fill=color)


class Game(BaseFrame):
    def __init__(self, title="Rect test", width=610, height=400):
        super().__init__(title, width, height)

    def buildWidgets(self):
        Rect(100, 100, 75, 20, '#00FFFF', self.canvas)
        self.circle = Circle(100, 100, 10, '#FF0000', self.canvas)
        self.canvas.focus_set()
        self.canvas.bind('<Left>',lambda _: self.circle.move(-10, 0))
        self.canvas.bind('<Right>',lambda _: self.circle.move(10, 0))
        self.canvas.bind('<Up>',lambda _: self.circle.move(0, -10))
        self.canvas.bind('<Down>',lambda _: self.circle.move(0, 10))

if __name__ == '__main__':
    Game()