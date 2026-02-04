import math
import pygame
import circleshape
from shot import Shot
from constants import PLAYER_RADIUS
from constants import PLAYER_SPEED
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_START_LIVES
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from constants import PLAYER_I_TIME
from constants import LINE_WIDTH
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT


#class for player object
class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 180
        self.shot_cooldown = 0
        self.lives = PLAYER_START_LIVES
        self.i_time = PLAYER_I_TIME

    def get_lives(self):
        return self.lives

    def get_istate(self):
        if self.i_time > 0:
            return True
        return False

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
        color = "cyan"
        if self.i_time > 0 and math.fmod(math.trunc(self.i_time * 5), 2) == 0:
            color = "red"

        pygame.draw.polygon(screen, color, self.triangle(), LINE_WIDTH)

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

    def process_hit(self, x, y):
        if self.i_time > 0:
            return self
        else:
            self.lives -= 1
            if self.lives >= 0:
                new_player = Player( x, y)
                new_player.lives = self.lives
                self.kill()
                return new_player
            else:
                raise PlayerState("player is dead")


    def reset(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 180
        self.shot_cooldown = 0

        #print(f"x: {x}, y: {y}; pos: {self.position}")

    def update(self, dt):
        self.shot_cooldown -= dt
        self.i_time -= dt

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

        if self.position.x > SCREEN_WIDTH:
            self.position = pygame.Vector2(self.position.x - SCREEN_WIDTH, self.position.y)
        if self.position.x < 0:
            self.position = pygame.Vector2(self.position.x + SCREEN_WIDTH, self.position.y)
        if self.position.y > SCREEN_HEIGHT:
            self.position = pygame.Vector2(self.position.x, self.position.y - SCREEN_HEIGHT)
        if self.position.y < 0:
            self.position = pygame.Vector2(self.position.x, self.position.y + SCREEN_HEIGHT)
