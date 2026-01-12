import sys
import pygame
#import player

from logger import log_state
from logger import log_event
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    exit = False
    dt = 0
    main_timer = pygame.time.Clock()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    field = AsteroidField()

    while exit != True:
        #pre loop
        log_state()

        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                return

        # update
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collide_with(asteroid):
                log_event("player_hit")
                print(f"Gamer over!")
                sys.exit()

            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()

        # draw
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        #loop end
        tick = main_timer.tick(60)
        dt = tick / 1000
        #print(f"{dt}")


if __name__ == "__main__":
    main()
