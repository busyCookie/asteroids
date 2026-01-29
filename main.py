import sys
import pygame
import pygame.freetype

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
    lives = 3
    score = 0
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

    field = AsteroidField()

    pygame.freetype.init()

    font = pygame.freetype.Font("./NotoSansMono-VariableFont_wdth,wght.ttf", 24, 0, 0, True)
    font_symbol = pygame.freetype.Font("./NotoSansSymbols2-Regular.ttf", 24, 0, 0, True)
    #font_symbol = pygame.freetype.SysFont("C059", 24)

    #font = pygame.freetype.SysFont("segoeuisymbol", 24)

    while exit != True:
        #pre loop
        log_state()

        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                print(f"Score: {score}")
                print(f"lives: {" ♥" * lives}")
                print(f"game closing")
                return

        # update
        updatable.update(dt)
        i_time -= dt

        for asteroid in asteroids:
            if player.collide_with(asteroid) and i_time <= 0:
                if lives <= 0:
                    log_event("player_hit")
                    print(f"Gamer over!")
                    print(f"Score: {score}")
                    print(f"lives: {" ♥" * lives}")

                    sys.exit()
                else:
                    lives -= 1
                    i_time = 1
                    player.reset(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_hit")
                    score += 1
                    shot.kill()
                    asteroid.split()

        # draw
        screen.fill("black")

        #score_ui = font.render(f"score: {score}", 1, "white")
        #lives_line = "\xA5" * lives
        #lives_ui =  font.render(lives_line, 1, "red")

        for item in drawable:
            item.draw(screen)

        #screen.blit(score_ui, (10,10) )
        #screen.blit(lives_ui, (10,34) )

        font.render_to(screen, (10,10), f"score: {score}", "yellow")
        font.render_to(screen, (10,36), f"lives:", "red")
        font_symbol.render_to(screen, (100,36), " ♥" * lives, "red")

        pygame.display.flip()

        #loop end
        tick = main_timer.tick(60)
        dt = tick / 1000
        #print(f"{dt}")


if __name__ == "__main__":
    main()
