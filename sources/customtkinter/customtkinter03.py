# Custom Tkinter Test
# Stage 3: Custom Tkinter (Dark Theme)

from tkinter import *
import customtkinter as ctk

# Erscheinungsbild (Theme) festlegen
ctk.set_appearance_mode("dark")

# Fenster mit Titel erzeugen und die Größe festlegen
wn = ctk.CTk()
wn.title("Dark Theme Ctk-Fenster")
wn.geometry("300x400")

# Button erzeugen und anzeigen
mybutton = ctk.CTkButton(wn, text = "Hallo Jörg! 🤓")
mybutton.place(relx = .5, rely = .5, anchor = CENTER)

wn.mainloop()