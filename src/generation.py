
import pygame
import os
import random

import src.main

class Generation:
  def __init__(self) -> None:
    self.tree = pygame.image.load(os.path.join("src", "assets", "tree16x32.png"))
    self.x, self.y = src.main.Ecosystem().DISPLAY
  
  def generate(self):
    data = []
    for i in range(32):
      randomX = random.randint(0, self.x)
      randomY = random.randint(0, self.y)
      data.append({"object": self.tree, "x": self.randomX, "y": self.randomY})
    return data
      
      
  def draw(self, screen, data):
      for i in data:
        screen.blit(i["object"], (i["x"], i["y"]))