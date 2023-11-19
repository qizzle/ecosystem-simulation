import pygame
import sys
from pygame.locals import *

import src.input as inputManager

class Ecosystem:
  def __init__(self) -> None:
    # Einstellungen
    self.CANVAS = 32
    self.TEXTURESIZE = 16
    self.FPS = 24.0
    #
    pygame.init()
    self.DISPLAY = (self.CANVAS * self.TEXTURESIZE, self.CANVAS * self.TEXTURESIZE)
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode(self.DISPLAY, FULLSCREEN | SCALED)
    self.deltaTime = 1 / self.FPS # deltaTime ist die Zeit, die seit dem letzten Frame vergangen ist.
    self.running = True
    
    self.input = inputManager.Input()
  
  def quit(self) -> None:
    self.running = False
    pygame.quit()
    sys.exit()
  
  def update(self, deltaTime) -> None:
    
    self.input.register(pygame.key.get_pressed())
    
    for event in pygame.event.get():
      if event.type == QUIT:
        self.quit()
          
  
  def draw(self, screen) -> None:
    screen.fill((110, 100, 80))
    
    pygame.display.flip()
  
  def run(self) -> None:
    while self.running:
      self.update(self.deltaTime)
      self.draw(self.screen)
      
      self.deltaTime = self.clock.tick(self.FPS)
      