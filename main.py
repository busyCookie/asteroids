import pygame

from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT


def main():
    exit = False
    dt = 0
    main_timer = pygame.time.Clock()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while exit != True:
        #pre loop
        log_state()


        #draw
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                return

        screen.fill("black")
        pygame.display.flip()

        #loop end
        tick = main_timer.tick(60)
        dt = tick / 1000
        #print(f"{dt}")


if __name__ == "__main__":
    main()
