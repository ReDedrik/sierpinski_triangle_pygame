import pygame
import sys
from math import sqrt
import random as rd

pygame.init()

###
### creating canvas and establishing variables
###
i = 0
dots = 100000
dotsize = 1
height, width = 800, 800
size = (height, width)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
black = (0, 0, 0)
start_position = 50, 500
pygame.display.set_caption(f"Sierpinski Triangle, {dots} Dots")
screen.fill(white)

###
### Dot function to draw dots at specified location
###
def Dot(x, size = dotsize):
    pygame.draw.circle(screen, black, (x[0], x[1]), size)

###
### establishing the corners
###
y_offset = 75
corner1 = (75, height - y_offset)
corner2 = (corner1[0] + (width - y_offset * 2), corner1[1])
corner3 = ((corner1[0] + corner2[0]) / 2, height - y_offset - sqrt((corner2[0] - corner1[0])**2 - ((corner1[0] + corner2[0]) / 2)**2))

###
### function to pick first random point
###
def first_point(pt1, pt2, pt3):
    x, y = sorted([rd.random(), rd.random()])
    s, t, u = x, y - x, 1 - y
    return (s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1])


def random_vertex():
    num = rd.randint(1, 3)
    if num == 1:
        return corner1
    if num == 2:
        return corner2
    if num == 3:
        return corner3

def draw_new_point(point1, point2):
    x_value = (point1[0] + point2[0]) / 2
    y_value = (point1[1] + point2[1]) / 2
    return (x_value, y_value)


fp = first_point(corner1, corner2, corner3)
Dot(corner1, 3)
Dot(corner2, 3)
Dot(corner3, 3)
Dot(fp)
next_point = fp
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if i <= dots:
        vertex = random_vertex()
        next_point = draw_new_point(next_point, vertex)
        Dot(next_point)



    i += 1
    pygame.display.update()

