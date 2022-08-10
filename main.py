import pygame
import sys

pygame.init()

height = 600
width = 600
screen = pygame.display.set_mode(height, width)
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
start_position = 50, 500


def draw_circle(x, y):
    pygame.draw.circle(screen, black, (x, y), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


