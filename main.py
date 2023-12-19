
import pygame
import sys
from pygame.locals import *

from generation import Generation

class Ecosystem:
  def __init__(self) -> None:
    
    SIZE = (640, 360) # 16:9 scaled
    
    pygame.init()
    self.screen = pygame.display.set_mode(SIZE, SCALED | FULLSCREEN, vsync=0)
    self.clock = pygame.time.Clock()
    
    self.current_gametick = 0
    self.gen = Generation()
    
  def run(self) -> None:
    
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      
      self.screen.fill("#472d3c")

      self.gen.run(self.screen)
      
      pygame.display.update()