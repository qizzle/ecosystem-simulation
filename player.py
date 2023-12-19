
import pygame

class Player:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.tilesheet = pygame.image.load("./assets/colored_packed.png").convert()

    def move(self, x, y) -> None:
        if (self.x + x >= 0) and (self.x + x + 1 <= 40) :
            if self.y + y >= 0:
                self.x = self.x + x
                self.y = self.y + y

    def draw(self, screen):
        screen.blit(self.tilesheet, (self.x * 16, self.y * 16), (25 * 16, 0, 16, 16))

