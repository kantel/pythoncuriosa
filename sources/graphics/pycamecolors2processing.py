import pygame
import sys

pygame.init()
FPS = 60
clock = pygame.time.Clock()

# colors
all_colors = list()
all_rgb = list()
for item in pygame.color.THECOLORS.items():
    all_colors.append(item)
    all_rgb.append(item[1])

print(all_colors)
# print(all_rgb)