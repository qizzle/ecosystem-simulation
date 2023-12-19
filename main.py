
import pygame
import sys
import math
from pygame.locals import *

from generation import Generation
from player import Player
from ldtk_loader import LDTKLoader

class Ecosystem:
  def __init__(self) -> None:
    
    SIZE = (640, 360) # 16:9 scaled
    
    pygame.init()
    self.screen = pygame.display.set_mode(SIZE, SCALED | FULLSCREEN, vsync=0)
    self.clock = pygame.time.Clock()
    
    self.current_gametick = 0
    self.gen = Generation()
    self.map = self.gen.gen()

    self.player = Player()
    self.house_scene = LDTKLoader("house_scene")
    self.house_scene.load()
    
  def quit(self):
    pygame.quit()
    sys.exit()

  def run(self) -> None:
    
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.quit()
        if event.type == pygame.KEYDOWN:
          if event.key == K_DOWN:
            self.player.move(0, 1)
          if event.key == K_UP:
            self.player.move(0, -1)
          if event.key == K_LEFT:
            self.player.move(-1, 0)
          if event.key == K_RIGHT:
            self.player.move(1, 0)

      keys = pygame.key.get_pressed()

      if keys[K_ESCAPE]:
        self.quit()
      if keys[K_r]:
        self.map = self.gen.gen()
      

      self.screen.fill("#472d3c")

      self.gen.run(self.screen, self.map)
      
      self.house_scene.draw(self.screen, 320 - 16 * 16 / 2, 160 - 8 * 16 / 2)

      self.player.draw(self.screen)

      

      pygame.display.update()