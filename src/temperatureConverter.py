"""
Temperature Converter
"""
import tkinter as tk

class Converter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Converter")
        self.root.geometry("252x75")
        self.text = tk.StringVar()
        self.initGUI()
        self.root.mainloop()
        
    
    def initGUI(self):
        tk.Label(self.root, text="Fahrenheit").grid(row=0, column=0)
        self.entryF = tk.Entry()
        self.entryF.grid(row=0, column=1)
        tk.Button(self.root, text="Convert", command=self.convertToC).grid(row=0, column=2)
        tk.Label(self.root, text="Celsius").grid(row=1, column=0)
        self.entryC = tk.Entry()
        self.entryC.grid(row=1, column=1)
        tk.Button(self.root, text="Convert", command=self.convertToF).grid(row=1, column=2,padx=5)
        self.text.set("Result")
        self.resultLbl = tk.Label(self.root, textvariable=self.text, bg='#69B2F1', width=34)
        self.resultLbl.grid(row=2, column=0, columnspan=3, padx=5)

    def convertToC(self):
        f = int(self.entryF.get())
        c = 5/9*(f-32)
        self.text.set(f"{f} Fahrenheit = {c:.0f} Celsuis")

    def convertToF(self):
        c = int(self.entryC.get())
        f = 9/5*c+32
        self.text.set(f"{c} Celsuis = {f:.0f} Fahrenheit")

if __name__ == '__main__':
    converter = Converter()