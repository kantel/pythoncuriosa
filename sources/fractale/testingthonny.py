from tkinter import *
root = Tk()
root.title("Tk Canvas")

cw = 400            # canvas width
ch = 400            # canvas height
canvas = Canvas(root, width = cw, height = ch, background = "white")
canvas.grid(row = 0, column = 0)

root.mainloop()
