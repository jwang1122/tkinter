"""
popup windows
"""
#Import the required library
from tkinter import*
text = ""

#Define a function to close the popup window
def close_win(top):
   global entry
   global text
   text = entry.get()
   top.destroy()

#Define a function to open the Popup Dialogue
def popupwin():
   global entry
   #Create a Toplevel window
   top= Toplevel(win)
   top.geometry("750x250")

   #Create an Entry Widget in the Toplevel window
   entry= Entry(top, width= 25)
   entry.pack()

  #Create a Button Widget in the Toplevel Window
   button= Button(top, text="Ok", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)

if __name__ == '__main__':    
    #Create an instance of tkinter frame
    win= Tk()

    #Define geometry of the window
    win.geometry("750x250")

    #Create a Label
    label= Label(win, text="Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
    label.pack(pady=20)
    text = StringVar()
    label1= Label(win, textvariable=text, font= ('Helvetica 15 bold'))
    label1.pack(pady=20)


   
    #Create a Button
    button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
    button.pack(pady=20)
    win.mainloop()