import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Sqlite Database")
root.geometry('300x200')

conn = sqlite3.connect("address.db")

c = conn.cursor()
index = -1
records = None

def load():
    global records
    sql = "SELECT * FROM address"
    c.execute(sql)
    records = c.fetchall()
    next()
    conn.close()
    loadBtn['state']=tk.DISABLED

def next():
    global index
    index += 1
    if index == len(records):
        index = 0
    record = records[index]
    firstname.delete(0, tk.END)
    firstname.insert(0,record[1])
    lastname.delete(0, tk.END)
    lastname.insert(0,record[2])
    address.delete(0, tk.END)
    address.insert(0,record[3])
    city.delete(0, tk.END)
    city.insert(0,record[4])
    state.delete(0, tk.END)
    state.insert(0,record[5])
    zipcode.delete(0, tk.END)
    zipcode.insert(0,record[6])

tk.Label(root, text="First Name:", padx=5).grid(row=0, column=0, sticky='e')
tk.Label(root, text="Last Name:", padx=5).grid(row=1, column=0, sticky='e')
tk.Label(root, text="Street:", padx=5).grid(row=2, column=0, sticky='e')
tk.Label(root, text="City:", padx=5).grid(row=3, column=0, sticky='e')
tk.Label(root, text="State:", padx=5).grid(row=4, column=0, sticky='e')
tk.Label(root, text="Zip:", padx=5).grid(row=5, column=0, sticky='e')
firstname = tk.Entry(root, width=30)
firstname.grid(row=0, column=1, padx=20,columnspan=2)
lastname = tk.Entry(root, width=30)
lastname.grid(row=1, column=1, padx=20,columnspan=2)
address = tk.Entry(root, width=30)
address.grid(row=2, column=1, padx=20,columnspan=2)
city = tk.Entry(root, width=30)
city.grid(row=3, column=1, padx=20,columnspan=2)
state = tk.Entry(root, width=30)
state.grid(row=4, column=1, padx=20,columnspan=2)
zipcode = tk.Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20,columnspan=2)

loadBtn = tk.Button(root, text="Load record", command=load)
loadBtn.grid(row=6, column=0)
tk.Button(root, text="next record", command=next).grid(row=6, column=1)

root.mainloop()