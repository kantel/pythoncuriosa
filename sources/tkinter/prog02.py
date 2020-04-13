import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")
win.resizable(False, False)

a_label = ttk.Label(win, text = "Jörgs Label")
a_label.grid(column = 0, row = 0)

def clickMe():
    action.configure(text = "** Ich wurde gedrückt! **")
    a_label.configure(foreground = "red")

action = ttk.Button(win, text = "Drück mich!", command = clickMe)
action.grid(column = 1, row = 0)

win.mainloop()