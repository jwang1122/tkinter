import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Sqlite Database")
root.geometry('300x200')

conn = sqlite3.connect("address.db")

c = conn.cursor()
info = tk.StringVar()

def delete():
    id_ = id.get()
    sql = "DELETE FROM address WHERE _id=?"
    c.execute(sql, (id_,))
    conn.commit()
    info.set("record has been removed from Database.")

tk.Label(root, text="id:", padx=5).grid(row=1, column=0, sticky='e')
id = tk.Entry(root, width=50)
id.grid(row=1, column=1, padx=20)
tk.Button(root, text="Delete", command=delete).grid(row=2, column=1)
tk.Label(root, textvariable=info).grid(row=8, column=0, columnspan=2)

root.mainloop()