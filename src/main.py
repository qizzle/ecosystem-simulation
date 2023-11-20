import pygame
import sys
from pygame.locals import *

import src.input as inputManager
import src.generation as generation

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
    self.screen = pygame.display.set_mode(self.DISPLAY, SCALED)
    self.deltaTime = 1 / self.FPS # deltaTime ist die Zeit, die seit dem letzten Frame vergangen ist.
    self.defaultColor = (206, 225, 189)
    self.running = True
    
    self.input = inputManager.Input()
    self.generation = generation.Generation()
    self.generationData = self.generation.generate()
  
  def quit(self) -> None:
    self.running = False
    pygame.quit()
    sys.exit()
  
  def update(self, deltaTime) -> None:
    
    keys = pygame.key.get_pressed()
    
    self.input.register(keys)
    
    if keys[K_r]:
      self.generationData = self.generation.generate()
    
    for event in pygame.event.get():
      if event.type == QUIT:
        self.quit()
          
  
  def draw(self, screen) -> None:
    screen.fill(self.defaultColor)
    
    self.generation.draw(screen, self.generationData)
    
    pygame.display.flip()
  
  def run(self) -> None:
    while self.running:
      self.update(self.deltaTime)
      self.draw(self.screen)
      
      self.deltaTime = self.clock.tick(self.FPS)
      