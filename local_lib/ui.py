import pygame
import pygame.freetype

from local_lib.constants import FONT
from local_lib.constants import SYMBOL_FONT

class score_gauge(pygame.freetype.Font):
    def
    __init__(self, x, y, score):
        super().__init__(FONT, 24, 0, 0, True)
        self.gauge_string = f"Score: {score}"
        self.x = x
        self.y = y

    def update(self, score):
        self.gauge_string = f"Score: {score}"

    def draw(self):
        self.font.render_to(screen, (self.x,self.y), self.gauge_string, "red")

class lives_gauage(pygame.freetype.Font):
    def __init__(self, x, y, lives):
        super().__init__(SYMBOL_FONT, 24, 0, 0, True)
        self.gauge_string = f"lives: {" ♥" * lives}"
        self.x = x
        self.y = y

    def update(self, current_lives):
        self.gauge_string = f"lives: {" ♥" * current_lives}"

    def draw(self, screen):
        self.font.render_to(screen, (self.x,self.y), self.gauge_string, "red")
