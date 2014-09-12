#!/bin/python

from color_printer import print_colors
from random import randrange
from time import sleep
from colorsys import hsv_to_rgb

hsv_colors = []

for i in range(64):
  hsv_colors.append([((4*i-1)%256)/256.0, 1, 1])

def increment_color(hsv_color):
  velocity = 0.01
  hsv_color[0] += velocity
  hsv_color[0] = hsv_color[0]%1

def to_rgb_256(hsv_color_array):
  rgb_256_colors = []
  for i in range(len(hsv_color_array)): 
    h = hsv_color_array[i][0]
    s = hsv_color_array[i][1]
    v = hsv_color_array[i][2]
    (r, g, b) = hsv_to_rgb(h, s, v)
    r *= 256
    g *= 256
    b *= 256
    rgb_256_colors.append([r, g, b])
  return rgb_256_colors

while True:
  print_colors(to_rgb_256(hsv_colors))
  map(increment_color, hsv_colors)
  sleep(.01)
