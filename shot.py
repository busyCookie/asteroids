import pygame
import circleshape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH

#class for projectile object
class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # drew asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # random movement
    def update(self, dt):
        speed_vector = self.velocity * dt
        self.position += speed_vector
