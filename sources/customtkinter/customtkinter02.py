# Custom Tkinter Test
# Stage 2: Custom Tkinter (Default Theme)

from tkinter import *
import customtkinter as ctk

# Fenster mit Titel erzeugen und die Größe festlegen
wn = ctk.CTk()
wn.title("Standard Ctk-Fenster")
wn.geometry("300x400")

# Button erzeugen und anzeigen
mybutton = ctk.CTkButton(wn, text = "Hallo Jörg! 🤓")
mybutton.place(relx = .5, rely = .5, anchor = CENTER)

wn.mainloop()