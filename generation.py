
import pygame
import random

class Generation:
    def __init__(self) -> None:
        self.tree1 = pygame.image.load("./assets/tree1.png").convert()
        
        self.map = self.gen()

    def gen(self) -> list:
        map = []
        for i in range(24):
            map.append([random.randint(0, 640), random.randint(0, 360)])

    def run(self,screen) -> None:
        screen.blit(self.tree1, (0, 0))