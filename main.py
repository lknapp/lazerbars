#!/bin/python

from color_printer import print_colors
from random import randrange
from time import sleep
from colorsys import hsv_to_rgb
from rgb_converter import rgb256

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
    r = int(r) - 1
    g = int(g) - 1
    b = int(b) - 1
    rgb_256_colors.append([r, g, b])
  return rgb_256_colors


#hsv_red_array = [[0, 1, 1]]
#rgb_256_red_array = to_rgb_256(hsv_red_array)
#rgb_256_color_code = rgb256(rgb_256_red_array[0])
#
#rgb_256_color = rgb256([255, 0, 0])
#print(hsv_red_array)
#print(rgb_256_red_array)
#print(rgb_256_color_code)
#print(rgb_256_color)

hsv_colors = []

for i in range(64):
  hsv_colors.append([((4*i-1)%256)/256.0, 1, 1])

print_colors(to_rgb_256(hsv_colors))


while True:
  map(increment_color, hsv_colors)

  print_colors(to_rgb_256(hsv_colors))
  sleep(.01)
