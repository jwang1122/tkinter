import tkinter as tk
import sqlite3
import uuid

root = tk.Tk()
root.title("Sqlite Database")
root.geometry('300x200')

conn = sqlite3.connect("address.db")

c = conn.cursor()
sql = """
CREATE TABLE address (
    _id text,
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zip text
)
"""
# c.execute(sql)

def new():
    firstname.delete(0, tk.END)
    lastname.delete(0, tk.END)
    address.delete(0, tk.END)
    city.delete(0, tk.END)
    state.delete(0, tk.END)
    zipcode.delete(0, tk.END)

def save():
    fname = firstname.get()
    lname = lastname.get()
    street = address.get()
    city_ = city.get()
    state_ = state.get()
    zip_ = zipcode.get()
    sql = "INSERT INTO address values(?,?,?,?,?,?,?)"
    _id = uuid.uuid4().hex
    c.execute(sql, (_id, fname, lname, street, city_, state_, zip_))
    # sql = "INSERT INTO address values(:fname,:lname,:street,:city,:state,:zip)"
    # c.execute(sql, {'fname':fname, 'lname':lname, 'street':street, 'city':city_, 'state':state_, 'zip':zip_})
    conn.commit()
    info.set("The data has been saved into database.")
    new()

def close():
    conn.close()
    addBtn['state'] = tk.DISABLED
    info.set("add button disabled")
    
info = tk.StringVar()
info.set("")

tk.Label(root, text='address book database was created.')
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

addBtn = tk.Button(root, text="Add record", command=save)
addBtn.grid(row=6, column=0)
tk.Button(root, text="Clear", command=new).grid(row=6, column=1)
tk.Button(root, text="Closs DB", command=close).grid(row=6, column=2)
tk.Label(root, textvariable=info).grid(row=7, column=0, columnspan=3)
root.mainloop()