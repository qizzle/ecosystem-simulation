
import src.main
from pygame.locals import *

class Input:
  def __init__(self) -> None:
    pass
  
  def register(self, keys) -> None:
    if keys[K_ESCAPE]:
      src.main.Ecosystem().quit()