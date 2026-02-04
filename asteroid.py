import pygame
import random
import circleshape
from logger import log_event
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")

            split_direction1 = self.velocity.rotate(random.randint(20, 50))
            split_direction2 = split_direction1.rotate(45)
            split_radius = self.radius - ASTEROID_MIN_RADIUS

            position1 = self.position + split_direction1.normalize() * split_radius
            position2 = self.position + split_direction2.normalize() * split_radius

            asteroid1 = Asteroid(position1.x, position1.y, split_radius)
            asteroid2 = Asteroid(position2.x, position2.y, split_radius)

            asteroid1.velocity = split_direction1 * 1.2
            asteroid2.velocity = split_direction2 * 1.2

    # drew asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "grey", self.position, self.radius, LINE_WIDTH)

    # random movement
    def update(self, dt):
        speed_vector = self.velocity * dt
        self.position += speed_vector

        diameter = self.radius * 2
        if self.position.x > SCREEN_WIDTH + diameter:
            self.kill
        if self.position.x < 0 - diameter:
            self.kill
        if self.position.y > SCREEN_HEIGHT + diameter:
            self.kill
        if self.position.y < 0 - diameter:
            self.kill

