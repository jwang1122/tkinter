from tkinterbase import *

class Board(TkinterBase):
    def buildWidget(self):
        westValue = StringVar()
        westValue.set(0)
        resultFrame = LabelFrame(self.root, text="Game Result", bg='yellow')
        Label(resultFrame, text="East", bg='yellow').grid(row=1, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=1, column=2)
        Label(resultFrame, text="South", bg='yellow').grid(row=2, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=2, column=2)
        Label(resultFrame, text="West", bg='yellow').grid(row=3, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=3, column=2)
        Label(resultFrame, text="Dealer", bg='yellow').grid(row=4, column=1)
        Label(resultFrame, textvariable=westValue, bg='yellow').grid(row=4, column=2)
        resultFrame.place(x=800, y=50)

if __name__ == '__main__':
    Board()