#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:16:54 2023

@author: Jörg Kantel
"""

import pygame
from pygame.locals import *
import os, sys

WIDTH, HEIGHT = 640, 480
TITLE = "🐍 Pygame Boilerplate 🐍"
FPS = 60
BG_COLOR = (0, 80, 125)    # Mittelblau

# Hier wird der Pfad zum Verzeichnis der Assets gesetzt
DATAPATH = os.path.join(os.getcwd(), "data")

# Pygame und das Fenster initialisieren
clock = pygame.time.Clock()
pygame.init()
# Ein übler Hack, um die Position des Fensters
# auf meinen zweiten Bildschirm zu setzen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1320, 60)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)


# Hauptschleife
keep_going = True
while keep_going:
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if ((event.type == pygame.QUIT)
            or (event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE)):
            keep_going = False
            print("Bye, Bye, Baby!")
            # pygame.quit()
            # sys.exit()
                           
    screen.fill(BG_COLOR)
    pygame.display.flip()
    
pygame.quit()
sys.exit()