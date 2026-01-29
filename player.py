import pygame
import circleshape
from shot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_START_LIVES
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from constants import LINE_WIDTH

#class for player object
class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 180
        self.shot_cooldown = 0
        self.lives = PLAYER_START_LIVES

    def get_lives(self):
        return self.lives

    # generate triange shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # draw player shape
    def draw(self, screen):
        pygame.draw.polygon(screen, "blue", self.triangle(), LINE_WIDTH)

    # controls
    def shoot(self):
      shot = Shot(self.position.x, self.position.y)
      shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        direction = pygame.Vector2(0,1)
        direction = direction.rotate(self.rotation)
        speed_vector = direction * PLAYER_SPEED * dt

        self.position += speed_vector

    def get_hit(self):
        self.lives -= 1

    def reset(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 180
        self.shot_cooldown = 0

        #print(f"x: {x}, y: {y}; pos: {self.position}")

    def update(self, dt):
        self.shot_cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown <= 0:
                self.shoot()
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
