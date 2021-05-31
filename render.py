import pygame
from player import Playerg

class Render:
    def __init__(self, screen: pygame.Surface, player: Playerg):
        self.screen = screen
        self.player = player
        self.delta_x = 580
        self.delta_y = 330
        self.cell = 50

    def map(self):
        with open(f"levels/{self.player.lvl}/map.txt") as map_file:
            map_lines = map_file.readlines()
            for i, line in enumerate(map_lines):
                for j, block in enumerate(line):
                    if block == '1':
                        pygame.draw.rect(self.screen, (0, 255, 0), (j * self.cell - self.player.x, i * self.cell - self.player.y, self.cell, self.cell), 2)
                    elif block == '0':
                        pygame.draw.rect(self.screen, (255, 255, 255), (j * self.cell - self.player.x, i * self.cell - self.player.y, self.cell, self.cell))

    def render_player(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (580, 330, 40, 60))


