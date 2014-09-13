#!/bin/python
from color_printer import print_colors
from random import randrange
from time import sleep
import math

def increment_color(hsv_color):
  velocity = 0.01
  hsv_color[0] += velocity
  hsv_color[0] = hsv_color[0]%1


hsv_colors = []
frame = 0

for i in range(64):
  hsv_colors.append([((4*i-1)%256)/256.0, 1, 1])

def modify_sinusoidally(hsv_color):
  velocity = math.sin(math.radians(frame*5))/100.0
  hsv_color[0] += velocity
  hsv_color[0] = hsv_color[0]%1

while True:
  frame += 1
  map(modify_sinusoidally, hsv_colors)
#  map(increment_color, hsv_colors)

  print_colors(hsv_colors)
  sleep(.01)
