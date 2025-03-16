# Motion 101 (Velocity and Random Acceleration)
import pygame
from random import random, uniform
import sys

# Einige nützliche Konstanten
WIDTH = 800
HEIGHT = 450
TITLE = "Motion 101 (Velocity and Random Acceleration)"
FPS = 60  # Framerate

# Farben
BG_COLOR = 59, 122, 87  # Billardtisch-Grün

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
        self.mover.check_borders()

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
        self.position = vec2(WIDTH//2, HEIGHT//2)
        self.velocity = vec2(0, 0)
        self.acceleration = vec2(0, 0)
        self.radius = 24
        self.limit = 10

    def update(self):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        self.acceleration.update(x, y)
        self.acceleration.normalize_ip()
        self.acceleration *= random()*2
        self.velocity += self.acceleration
        self.velocity.clamp_magnitude_ip(self.limit)
        self.position += self.velocity

    def check_borders(self):
        # Check borders
        if self.position.x > WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y > HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = HEIGHT

    def draw(self):
        pygame.draw.aacircle(self.world.screen, (255, 191, 0), self.position, self.radius)
        pygame.draw.aacircle(self.world.screen, (0, 0, 0), self.position, self.radius, 1)

        # sysfont = pygame.font.get_default_font()
        self.font = pygame.font.SysFont("American Typewriter", 16)
        # self.vel_txt = self.font.render("Hello", True, (255, 255, 255))
        self.vel_txt = self.font.render(str(self.velocity.magnitude()), True, (255, 255, 255))
        self.world.screen.blit(self.vel_txt, (20, 20))

# ---------------------------------------------------------------------- #
# ## Hauptprogramm
world = GameWorld()
world.reset()

# Hauptschleife
while world.keep_going:
    # Framerate festsetzen
    world.clock.tick(FPS)

    world.events()
    world.update()
    world.draw()

pygame.quit()
sys.exit(0)