
import pygame
import random

class Generation:
    def __init__(self) -> None:
        self.tilesheet = pygame.image.load("./assets/colored_packed.png").convert()
        self.tilesX = 40
        self.tilesY = 23

    def simple_tile_builder(self, map, x, y, tileX, tileY):
        return map.append([self.tilesheet, x, y, tileX, tileY])
    
    def interactive_tile_builder(self, map, x, y, tileX, tileY, scene):
        pass

    def gen(self) -> list:
        map = []
        for i in range(82):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 5, 0)
        for i in range(64):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 6, 0)
        for i in range(32):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 7, 0)
        for i in range(16):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 1, 0)
        # tree
        for i in range(36):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 0, 1)
        for i in range(24):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 1, 1)
        for i in range(16):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 2, 1)
        for i in range(12):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 3, 1)
        # house
        for i in range(3):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 0, 19)
        # stone
        for i in range(19):
            self.simple_tile_builder(map, random.randint(0, self.tilesX - 1), random.randint(0, self.tilesY - 1), 5, 2)

        return map

    def run(self,screen, map) -> None:
        for i in map:
          screen.blit(i[0], (i[1]*16, i[2]*16), area=(i[3]*16, i[4]*16, 16, 16))  