
import pygame
import os
import random

class Generation:
  def __init__(self) -> None:
    self.tree = pygame.image.load(os.path.join("src", "assets", "tree16x32.png"))
  
  def generate(self) -> list:
    data = []
    for i in range(32):
      randomX = random.randint(0, 512)
      randomY = random.randint(0, 512)
      data.append([self.tree, randomX, randomY])
    return data
      
      
  def draw(self, screen, data):
      for i in data:
        screen.blit(i[0], (i[1], i[2]))