# Motion 101 (Velocity
import asyncio
import pygame
from random import randint
import sys

# Einige nützliche Konstanten
WIDTH = 800
HEIGHT = 450
RADIUS = 24
TITLE = "Motion 101 (Velocity)"
FPS = 60  # Framerate

# Farben
BG_COLOR = 59, 122, 87, 255  # Billardtisch-Grün

vec2 = pygame.Vector2

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
        self.mover = Mover(self)

    def events(self):
        # Poll for events
        for event in pygame.event.get():
            if ((event.type == pygame.QUIT) or
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.keep_going = False

    def update(self):
        self.mover.update()

    def draw(self):
        self.screen.fill(BG_COLOR)
        # Game drawings go here
        self.mover.draw()

        # Alle Änderungen auf den Bildschirm
        pygame.display.flip()

# ---------------------------------------------------------------------- #
class Mover():

    def __init__(self, _world):
        self.world = _world
        self.position = vec2((randint(20, WIDTH - 20), randint(20, HEIGHT - 20 )))
        self.velocity = vec2((randint(-5, 5), randint(-5, 5)))
        self.radius = RADIUS

    def update(self):
        self.position += self.velocity
        if self.position.x > WIDTH - self.radius or self.position.x < self.radius:
            self.velocity.x *= -1
        if self.position.y > HEIGHT - self.radius or self.position.y < self.radius:
            self.velocity.y *= -1

    def draw(self):
        pygame.draw.aacircle(self.world.screen, (255, 191, 0, 255), self.position, self.radius)
        pygame.draw.aacircle(self.world.screen, (0, 0, 0, 255), self.position, self.radius, 1)

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