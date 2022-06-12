from tkinter import *


dialog = Dialog(
        Label(text="enter your name"),
        Entry(width=20, name="name"),
        ButtonBox(
            Button(text="OK", command=self.ok),
            Button(text="Cancel", command=self.cancel)
            )
        )
result = dialog.display()
if result:
    print result.name