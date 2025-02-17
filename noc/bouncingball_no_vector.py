# Bouncing Chicken with No Vectors
import asyncio
import pygame
import os, sys

# Hier wird der Pfad zum Verzeichnis der Assets gesetzt
DATAPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# Einige nützliche Konstanten
WIDTH = 800
HEIGHT = 450
CHICKEN_SIZE = 48
TITLE = "Bouncing Chicken with No Vectors (Pygame Version)"
FPS = 60  # Framerate

# Farben
BG_COLOR = 59, 122, 87, 255  # Billardtisch-Grün

# Klassen
# ---------------------------------------------------------------------- #
## Class GameWorld
class GameWorld:

    def __init__(self):
        # Pygame und das Fenster initialisieren
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.keep_going = True

    def reset(self):
        # Neustart oder Status zurücksetzen
        # Hier werden alle Elemente der GameWorld initialisiert
        self.all_sprites = pygame.sprite.Group()
        # Load Assets
        self.chicken_im = pygame.image.load(os.path.join(DATAPATH, "chick.png")).convert_alpha()
        self.chicken_im = pygame.transform.scale(self.chicken_im, (CHICKEN_SIZE, CHICKEN_SIZE))
        chicken = Chicken(self)
        self.all_sprites.add(chicken)

    def events(self):
        # Poll for events
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.keep_going = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        # Game drawings go here
        self.all_sprites.draw(self.screen)
        # Alle Änderungen auf den Bildschirm
        pygame.display.flip()

# ---------------------------------------------------------------------- #
## Class Chicken
class Chicken(pygame.sprite.Sprite):

    def __init__(self, _world):
        super().__init__()
        self.game_world = _world
        self.image = self.game_world.chicken_im
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = WIDTH / 2, HEIGHT / 2
        self.radius = CHICKEN_SIZE
        self.x_speed = 2.5
        self.y_speed = 2

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x > WIDTH - self.radius  or self.rect.x < 0:
            self.x_speed *= -1
        if (self.rect.y > HEIGHT - self.radius or self.rect.y < 0):
            self.y_speed *= -1

# ---------------------------------------------------------------------- #
# ## Hauptprogramm
world = GameWorld()
world.reset()

# Hauptschleife
async def main():
    while world.keep_going:
        # Framerate festsetzen
        world.clock.tick(FPS)

        world.events()
        world.update()
        world.draw()
        await asyncio.sleep(0)  # Very important, and keep it 0

    pygame.quit()
    sys.exit(0)

asyncio.run(main())