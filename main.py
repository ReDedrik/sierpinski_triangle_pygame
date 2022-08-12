import pygame
import sys
import math
import random as rd
import time

pygame.init()

###
### creating canvas and establishing variables
###
i = 0
previous_point = -1
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
        pt1 = Endpoint(center_of_screen[0] - length / 2, center_of_screen[1] + (math.sqrt(3) / 2) * (1/2) * length)
        pt2 = Endpoint(center_of_screen[0] + length / 2, center_of_screen[1] + (math.sqrt(3) / 2) * (1/2) * length)
        pt3 = Endpoint(center_of_screen[0], center_of_screen[1] - (math.sqrt(3) / 2) * (1/2) * length)
        for i in Endpoint.instances:
            i.Dot()
            Endpoint.Line(i, Endpoint.instances[(Endpoint.instances.index(i) + 1) % 3])
    
    @staticmethod
    def square(length):
        center_of_screen = (width / 2, height / 2)
        s_pt1 = Endpoint(center_of_screen[0] - length / 2, center_of_screen[1] + length / 2)
        s_pt2 = Endpoint(center_of_screen[0] + length / 2, center_of_screen[1] + length / 2)
        s_pt3 = Endpoint(center_of_screen[0] + length / 2, center_of_screen[1] - length / 2)
        s_pt4 = Endpoint(center_of_screen[0] - length / 2, center_of_screen[1] - length / 2)
        for i in Endpoint.instances:
            i.Dot()
        Endpoint.Line(s_pt1, s_pt2, s_pt4)
        Endpoint.Line(s_pt3, s_pt2, s_pt4)

    def pentagon(length):
        center_of_screen = (width / 2, height / 2)
        h = (length / 2) / math.cos(54 * math.pi / 180)
        p_pt1 = Endpoint(center_of_screen[0] - h * math.cos(54 * math.pi / 180), center_of_screen[1] - h * math.sin(-54 * math.pi / 180))
        p_pt2 = Endpoint(center_of_screen[0] + h * math.cos(-54 * math.pi / 180), center_of_screen[1] - h * math.sin(-54 * math.pi / 180))
        p_pt5 = Endpoint(center_of_screen[0] - h * math.cos(18 * math.pi / 180), center_of_screen[1] - h * math.sin(18 * math.pi / 180))
        p_pt4 = Endpoint(center_of_screen[0], center_of_screen[1] - h)
        p_pt3 = Endpoint(center_of_screen[0] + h * math.cos(-18 * math.pi / 180), center_of_screen[1] - h * math.sin(18 * math.pi / 180))
        Endpoint.Line(p_pt1, p_pt2, p_pt5)
        Endpoint.Line(p_pt3, p_pt2, p_pt4)
        Endpoint.Line(p_pt4, p_pt5)
        for i in Endpoint.instances:
            i.Dot()
        
###
### function to pick first random point
###
def first_point(list_of_pts):
    if len(list_of_pts) >= 4:
        return (rd.randrange(int(list_of_pts[0].coords[0]), int(list_of_pts[1].coords[0])), rd.randrange(int(list_of_pts[3].coords[1]), int(list_of_pts[0].coords[1])))
    else:
        pt1 = list_of_pts[0].coords
        pt2 = list_of_pts[1].coords
        pt3 = list_of_pts[2].coords
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

def pick_random_vertex(vertex):
    num_list = []
    for i in range(len(Endpoint.instances)):
        num_list.append(i)
    if len(Endpoint.instances) == 4:
        num_list.remove(vertex)
        previous_point = rd.choice(num_list)
        return previous_point
    if len(Endpoint.instances) == 3:
        return rd.randint(0, len(Endpoint.instances) - 1)
    elif len(Endpoint.instances) == 5:
        if vertex == 0:
            num_list.remove(1)
            num_list.remove(4)
        elif vertex == 1:
            num_list.remove(2)
            num_list.remove(0)
        elif vertex == 2:
            num_list.remove(1)
            num_list.remove(3)
        elif vertex == 3:
            num_list.remove(2)
            num_list.remove(4)
        elif vertex == 4:
            num_list.remove(0)
            num_list.remove(3)

        return rd.choice(num_list)


Endpoint.pentagon(350)
#Endpoint.square(700)
#Endpoint.equilateral_triangle(600)
pygame.display.update()

fp = first_point(Endpoint.instances)
dot(fp)
next_point = fp
pygame.display.update()
###
### game loop (update)
###
vertex = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if i <= 7:
        time.sleep(0.3)
    if i <= dots:
        vertex = pick_random_vertex(vertex)
        next_point = draw_new_point(next_point, Endpoint.instances[vertex].coords)
        dot(next_point)
    i += 1
    pygame.display.update()

