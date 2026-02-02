import pygame
import circleshape
from constants import SHOT_RADIUS
from constants import LINE_WIDTH
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

#class for projectile object
class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # drew asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "magenta", self.position, self.radius, LINE_WIDTH)

    # random movement
    def update(self, dt):
        speed_vector = self.velocity * dt
        self.position += speed_vector

        if self.position.x > SCREEN_WIDTH:
            self.position = pygame.Vector2(self.position.x - SCREEN_WIDTH, self.position.y)
        if self.position.x < 0:
            self.position = pygame.Vector2(self.position.x + SCREEN_WIDTH, self.position.y)
        if self.position.y > SCREEN_HEIGHT:
            self.position = pygame.Vector2(self.position.x, self.position.y - SCREEN_HEIGHT)
        if self.position.y < 0:
            self.position = pygame.Vector2(self.position.x, self.position.y + SCREEN_HEIGHT)
