
import src.main
import src.generation
import pygame
from pygame.locals import *

class Input:
  def __init__(self) -> None:
    pass
  
  def register(self, keys) -> None:
    if keys[K_ESCAPE]:
      src.main.Ecosystem().quit()
    if keys[K_F11]:
      pygame.display.toggle_fullscreen()