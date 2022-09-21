# Custom Tkinter Test
# Stage 4: Custom Tkinter (Dark Theme, Green Button)

from tkinter import *
import customtkinter as ctk

# Erscheinungsbild (Theme) festlegen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Fenster mit Titel erzeugen und die Größe festlegen
wn = ctk.CTk()
wn.title("Dark Theme Ctk-Fenster")
wn.geometry("300x400")

# Button erzeugen und anzeigen
mybutton = ctk.CTkButton(wn, text = "Hallo Jörg! 🤓")
mybutton.place(relx = .5, rely = .5, anchor = CENTER)

wn.mainloop()