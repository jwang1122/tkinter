"""
1. using close window call back protocol
2. display image as background
3. read text from file and display in the window
4. add text in file
"""
import tkinter as tk
import tkinter.messagebox
import os
from PIL import Image, ImageTk


def callback():
    """
    Asks the user if they really want to quit
    """
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

def PlaceRemoveFrame(frame1, frame2):
    """
    Forgets frame and places another
    """
    frame1.grid_forget()
    frame2.grid()

def get_entry():
    """
    Gets user input from entry, saves user input to file, and displays user input as label
    """

    x = entry.get()
    f = open("src/tkinter/categories.txt", "a")
    f.write(x + '\n')
    f.close()
    entry.delete(0, 'end')
    list_categories()

def list_categories():
    """
    Displays user input as label
    """

    try:
        f = open("src/tkinter/categories.txt", "r")
        contents = f.read()
        f.close()
    except FileNotFoundError:
        contents = ' '
    categories_list_label = tk.Label(None, text = "Categories: " + '\n'+ contents[:-1], bg = "darkorange", \
                                     fg ="black", font = "arial, 15")
    categories_list_label.place(x = 400, y = 350)

if __name__ == '__main__':
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", callback)
    root.geometry("1024x768")
    root.resizable(0, 0)
    root.title("tkinter21")

    CB1P = tk.Frame(root, width = 1024, height = 768)
    CB1P.grid()
    # image = Image.open("src/tkinter/snowCouple.png")
    image = Image.open("images/heartQ.gif")
    resizedImage = image.resize((1024, 768))

    CB1P_Image = ImageTk.PhotoImage(resizedImage)
    CB1P_Image_Pack = tk.Label(CB1P, image = CB1P_Image).grid()

    #CARGO BAY ONE LABEL
    CargoBayOne_Label = tk.Label(CB1P, text = "SNOW COUPLE", font =("Okuda", "16"), bg = "#9c3214", fg = "white")
    CargoBayOne_Label.place(x = 20, y = 20)
    tk.Label(root, text = "Category").place(x=20, y=80)
    entry = tk.Entry(root)
    entry.place(x=100, y=80)
    btn=tk.Button(root, text = "Add", activebackground = "green", activeforeground = "blue", command=get_entry)
    btn.place(x=200, y=80)

    root.mainloop()
