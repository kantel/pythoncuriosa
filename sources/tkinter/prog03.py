import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
win.resizable(False, False)
win.configure(background = "grey94")

a_label = ttk.Label(win, text = "Gib Deinen Namen ein:")
a_label.grid(column = 0, row = 0)
a_label.grid_configure(padx = 8, pady = 8)

def clickMe():
    action.configure(text = "Hallöchen " + name.get())

name = tk.StringVar()
name_entered = ttk.Entry(win, width = 12, textvariable = name)
name_entered.grid(column = 0, row = 1)
name_entered.grid_configure(padx = 8, pady = 8)
name_entered.focus()

action = ttk.Button(win, text = "Drück mich!", command = clickMe)
action.grid(column = 1, row = 1)
action.grid_configure(padx = 8, pady = 8)


win.mainloop()