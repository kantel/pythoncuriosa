import pygame
import os, sys

# Konstanten deklarieren
WIDTH, HEIGHT = 800, 450
ASSET_DIR = "data"
TITLE = "🐍 Pygame Boilerplate Objektorientiert 🐍"
FPS = 60

# Hier wird der Pfad zum Verzeichnis der Assets gesetzt
DATAPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ASSET_DIR)

# Farben
BG_COLOR = (59, 122, 87, 255) # Billardtisch-Grün
           
class GameWorld:
    
    def __init__ (self):
        # Initialisiert die Spielewelt
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.keep_going = True
        
    def reset(self):
        # Neustart oder Status zurücksetzen
        pass

    def events(self):
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT)
                or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.keep_going = False
                self.game_over()

    def update(self):
        pass
    
    def draw(self):
        self.screen.fill(BG_COLOR)
        pygame.display.flip()

    def start_screen(self):
        pass

    def game_over(self):
        print("Bye, Bye, Baby!")
        pygame.quit()
        sys.exit(0)

# Hauptprogramm
w = GameWorld()
w.start_screen()

while w.keep_going:
    w.clock.tick(FPS)
    w.events()
    w.update()
    w.draw()

w.game_over()