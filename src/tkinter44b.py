import tkinter as tk
from tkinter44 import *

class Calculator(MyFrame):
    def createWidget(self): # override createWidget() function for different application
        for i in range(4):
            for j in range(6):
                tk.Button(self.root, text=str(i) + "," + str(j), padx = 40, pady=40).grid(row=j, column=i)

if __name__ == '__main__':
    Calculator()