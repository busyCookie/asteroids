import sys
import pygame
import pygame.freetype

from local_lib.logger import log_state
from local_lib.logger import log_event
from local_lib.constants import SCREEN_WIDTH
from local_lib.constants import SCREEN_HEIGHT
from local_lib.constants import PLAYER_SURVIVAL_TIMER
from local_lib.player import Player
from local_lib.shot import Shot
from local_lib.asteroid import Asteroid
from local_lib.asteroidfield import AsteroidField

def main():
    exit = False
    score = 0
    survival_time = 0
    score_time_trigger = PLAYER_SURVIVAL_TIMER
    i_time = 0
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
    lives_string = " ♥" * player.get_lives()

    field = AsteroidField()

    pygame.freetype.init()

    font = pygame.freetype.Font("./fonts/NotoSansMono-VariableFont_wdth,wght.ttf", 24, 0, 0, True)
    font_symbol = pygame.freetype.Font("./fonts/NotoSansSymbols2-Regular.ttf", 24, 0, 0, True)

    while exit != True:
        #pre loop
        log_state()

        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                print(f"Score: {score}")
                print(f"lives: {lives_string}")
                print(f"game closing")
                return

        # update
        updatable.update(dt)
        i_time -= dt

        for asteroid in asteroids:
            if player.collide_with(asteroid):
                asteroid.split()
                log_event("player_hit")
                try:
                    player = player.process_hit(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                except:
                    log_event("player_killed")
                    print(f"Gamer over!")
                    print(f"Score: {score}")
                    sys.exit()
                else:
                    lives_string = " ♥" * player.get_lives()

            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_hit")
                    score += 1
                    shot.kill()
                    asteroid.split()

        # time_score
        survival_time += dt
        if survival_time >= score_time_trigger:
            score += 1
            score_time_trigger += score_time_trigger

        # draw
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        font.render_to(screen, (10,10), f"score: {score}", "yellow")
        font.render_to(screen, (10,36), f"lives:", "red")
        font_symbol.render_to(screen, (100,36), lives_string, "red")

        pygame.display.flip()

        #loop end
        tick = main_timer.tick(60)
        dt = tick / 1000
        #print(f"{dt}")


if __name__ == "__main__":
    main()
