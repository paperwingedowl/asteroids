import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta = 0
    refresh_rate = 120

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while True:

        for u in updatable:
            u.update(delta)

        for a in asteroids:
            if a.collide(player):
                print("Game over!")
                exit()

        screen.fill("black")
        
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        clock.tick(refresh_rate)
        delta = clock.tick(refresh_rate) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # checks to see if you closed the window, then exits
                return


if __name__ == "__main__":
    main()