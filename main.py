import pygame
from player import *
from circleshape import *
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0
    refresh_rate = 120

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks to see if you closed the window, then exits
                return
        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        clock.tick(refresh_rate)
        delta = clock.tick(refresh_rate) / 1000


if __name__ == "__main__":
    main()