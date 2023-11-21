
import pygame
import sys
from pygame.locals import *

class Ecosystem:
  def __init__(self) -> None:
    
    SIZE = (640, 360) # 16:9 scaled
    
    pygame.init()
    self.screen = pygame.display.set_mode(SIZE, SCALED | FULLSCREEN, vsync=0)
    self.clock = pygame.time.Clock()
    
    self.current_gametick = 0
    
  def run(self) -> None:
    
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      
      self.screen.fill("#71ddee")
      
      pygame.display.update()