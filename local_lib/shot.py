import pygame
import local_lib.circleshape as circleshape
from local_lib.constants import SHOT_RADIUS
from local_lib.constants import SHOT_TTL
from local_lib.constants import LINE_WIDTH
from local_lib.constants import SCREEN_WIDTH
from local_lib.constants import SCREEN_HEIGHT

#class for projectile object
class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.ttl = SHOT_TTL

    # drew asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "magenta", self.position, self.radius, LINE_WIDTH)

    # random movement
    def update(self, dt):
        if self.ttl <= 0:
            self.kill()
            return

        self.ttl -= 1 * dt
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
