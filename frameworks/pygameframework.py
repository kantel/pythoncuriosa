# Minimales PyGame-Grundgerüst
# Als Template für PyGame-Projekte zu verwenden

import pygame as pg
import os

# Einige nützliche Konstanten
WIDTH = 800
HEIGHT = 450
TITLE = "🐍 Hällo Wörld! 🐍"
FPS = 60   # Framerate

# Farben
BG_COLOR = 59, 122, 87, 255   # Billardtisch-Grün

# Pygame initialisieren
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()

# Assets laden
# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

keep_going = True
while keep_going:
    # Framerate festlegen
    clock.tick(FPS)
    # Eingabe verarbeiten (Input Events)
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            keep_going = False

    # Update

    # Draw
    screen.fill(BG_COLOR)
    
    # Wenn *alles* gezeichnet ist
    pg.display.flip()

print("I did it, Babe!")
pg.quit()