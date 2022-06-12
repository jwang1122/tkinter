from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Chart")
root.geometry('400x200')

def graph():
    housePrices = np.random.normal(200000, 25000, 5000)
    plt.hist(housePrices, 50)
    plt.show()

Button(root, text="graph", command=graph).pack()

root.mainloop()
