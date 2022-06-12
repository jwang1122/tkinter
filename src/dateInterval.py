"""
Calculate number of dates and weeks betweet two dates.
"""
import tkinter as tk
import datetime

class DateInterval:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Date Interval")
        self.root.geometry("380x75")
        self.initFields()
        self.initGUI()
        self.root.mainloop()

    def initFields(self):
        self.weeks = tk.IntVar()
        self.days = tk.IntVar()
        self.classes = tk.StringVar()

    def initGUI(self):
        tk.Label(self.root, text="Start Date").grid(row=0, column=0)
        self.entryStart = tk.Entry()
        self.entryStart.grid(row=0, column=1)
        tk.Label(self.root, text="End Date").grid(row=0, column=2)
        self.entryEnd = tk.Entry()
        self.entryEnd.grid(row=0, column=3)
        tk.Label(self.root, text="Number of weeks: ").grid(row=1, column=0, columnspan=2)
        tk.Label(self.root, textvariable=self.weeks).grid(row=1, column=2)
        tk.Label(self.root, text="Number of days: ").grid(row=2, column=0, columnspan=2)
        tk.Label(self.root, textvariable=self.days).grid(row=2, column=2)
        tk.Label(self.root, textvariable=self.classes).grid(row=1, column=3)
        tk.Button(self.root, text="OK", command=self.getResult).grid(row=2, column=3, ipadx=20)

    def getResult(self):
        startStr = self.entryStart.get()
        startList = startStr.split('/')
        startYear = int(startList[0])
        startMonth = int(startList[1])
        startDay = int(startList[2])

        endStr = self.entryEnd.get()
        endList = endStr.split('/')
        endYear = int(endList[0])
        endMonth = int(endList[1])
        endDay = int(endList[2])

        startDate = datetime.date(startYear,startMonth,startDay)
        endDate = datetime.date(endYear, endMonth, endDay)
        days = (endDate-startDate).days
        self.weeks.set(days//7)
        self.days.set(days)
        self.classes.set(f"{days//7*2} hours ${days//7*4*35}")

if __name__ == '__main__':
    DateInterval()