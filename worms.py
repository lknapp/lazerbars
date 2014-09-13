#!/bin/python
from color_printer import print_colors
from random import randrange
from time import sleep
import math

ENV_SIZE = 64

class Worm:
  def __init__(self, pos):
    self.pos = pos
    if randrange(2) == 1:
      self.vel = -1
    else:
      self.vel = 1
  def move(self):
    self.pos += self.vel
    if self.pos >= ENV_SIZE - 1:
      self.pos = 0
    if self.pos < 0:
      self.pos = ENV_SIZE - 1
  
class Env:
  def __init__(self, worms):
    self.occupied_cells = [0]*ENV_SIZE
    self.worms = worms
    for worm in self.worms:
      self.occupied_cells[worm.pos] = 1

  def update(self):
    for worm in self.worms:
      worm.move()
    self.occupied_cells = [0]*ENV_SIZE
    for worm in self.worms:
      self.occupied_cells[worm.pos] = 1

    
def make_color_array(occupied_cells):
  colors = []
  for cell in occupied_cells:
    if cell == 1:
      colors.append([255, 0, 255])
    else:
      colors.append([0, 0, 0])
  return colors


worms = [Worm(3), Worm(7), Worm(15), Worm(23)]
env = Env(worms)

while True:
  env.update()

  print_colors(make_color_array(env.occupied_cells))
  sleep(.1)
