import pygame
import circleshape

from constants import PLAYER_TURN_SPEED
from constants import LINE_WIDTH

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # drew asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # random movement
    def update(self, dt):
        speed_vector = self.velocity * dt
        self.position += speed_vector
