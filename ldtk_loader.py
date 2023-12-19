
import json
import os
import pygame

class LDTKLoader:
    def __init__(self, scene_name) -> None:
        self.tilesheet = pygame.image.load("./assets/colored_packed.png").convert()
        self.scene_name = scene_name

    def load(self):
        print(os.path.dirname(self.scene_name))
        with open("./scenes/" + self.scene_name + ".json", "r") as f:
            JSON = json.load(f)
        self.map = JSON["levels"][0]["layerInstances"][0]["gridTiles"]

    def draw(self, screen, offsetX, offsetY):
        for i in self.map:
            screen.blit(self.tilesheet, (i["px"][0] + offsetX, i["px"][1] + offsetY), (i["src"][0], i["src"][1], 16, 16))