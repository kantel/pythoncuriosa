# Custom Tkinter Test
# Stage 1: Tkinter ohne »Custom«

from tkinter import *

# Fenster mit Titel erzeugen und die Größe festlegen
wn = Tk()
wn.title("Standard Tkinter-Fenster")
wn.geometry("300x400")

# Button erzeugen und anzeigen
mybutton = Button(wn, text = "Hallo Jörg! 🤓", font = ("Inter", 14))
mybutton.place(relx = .5, rely = .5, anchor = CENTER)

wn.mainloop()