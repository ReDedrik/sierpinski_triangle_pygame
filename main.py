import pygame
import sys
from math import sqrt
import random as rd
import time

pygame.init()

###
### creating canvas and establishing variables
###
i = 0
dots = 30000
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

def dot(coords):
    pygame.draw.circle(screen, black, coords, 1)
###
### Endpoint class 
###

class Endpoint:
    instances = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
        Endpoint.instances.append(self)
    
    @staticmethod
    def random_vertex():
        num = rd.randint(1, len(Endpoint.instances) - 1)
        return Endpoint.instances[num]

    def Dot(self):
        pygame.draw.circle(screen, black, self.coords, 2)

    @staticmethod
    def Line(pt1, pt2, pt3 = None):
        pygame.draw.line(screen, black, pt1.coords, pt2.coords)
        if pt3 != None:
            pygame.draw.line(screen, black, pt1.coords, pt3.coords)
    
    @staticmethod
    def equilateral_triangle(length):
        center_of_screen = (width / 2, height / 2)
        pt1 = Endpoint(center_of_screen[0] - length / 2, center_of_screen[1] + (sqrt(3) / 2) * (1/2) * length)
        pt2 = Endpoint(center_of_screen[0] + length / 2, center_of_screen[1] + (sqrt(3) / 2) * (1/2) * length)
        pt3 = Endpoint(center_of_screen[0], center_of_screen[1] - (sqrt(3) / 2) * (1/2) * length)
        for i in Endpoint.instances:
            i.Dot()
            Endpoint.Line(i, Endpoint.instances[(Endpoint.instances.index(i) + 1) % 3])
    
    @staticmethod
    def square(length):
        center_of_screen = (width / 2, height / 2)
        s_pt1 = Endpoint(center_of_screen[0] - length / 2, center_of_screen[1] + length / 2)
        s_pt2 = Endpoint(center_of_screen[0] + length / 2, center_of_screen[1] + length / 2)
        s_pt3 = Endpoint(center_of_screen[0] - length / 2, center_of_screen[1] - length / 2)
        s_pt4 = Endpoint(center_of_screen[0] + length / 2, center_of_screen[1] - length / 2)
        for i in Endpoint.instances:
            i.Dot()
        Endpoint.Line(s_pt1, s_pt2, s_pt3)
        Endpoint.Line(s_pt4, s_pt2, s_pt3)
###
### function to pick first random point
###
def first_point(list_of_pts):
    if len(list_of_pts) == 4:
        return (rd.randint(list_of_pts[0].coords[0], list_of_pts[1].coords[0]), rd.randint(list_of_pts[3].coords[1], list_of_pts[0].coords[1]))
    else:
        pt1 = list_of_pts[0]
        pt2 = list_of_pts[1]
        pt3 = list_of_pts[2]
        x, y = sorted([rd.random(), rd.random()])
        s, t, u = x, y - x, 1 - y
        return (s * pt1[0] + t * pt2[0] + u * pt3[0],
                s * pt1[1] + t * pt2[1] + u * pt3[1])

###
### function to find the new midpoint
###
def draw_new_point(point1, point2):
    x_value = (point1[0] + point2[0]) / 2
    y_value = (point1[1] + point2[1]) / 2
    return (x_value, y_value)

Endpoint.square(400)
#Endpoint.equilateral_triangle(600)
pygame.display.update()

fp = first_point(Endpoint.instances)
dot(fp)
next_point = fp
pygame.display.update()
###
### game loop (update)
###
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if i <= 10:
        time.sleep(0.3)
    if i <= dots:
        vertex = Endpoint.random_vertex()
        next_point = draw_new_point(next_point, vertex.coords)
        dot(next_point)
    i += 1
    pygame.display.update()

