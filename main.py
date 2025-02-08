import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    pygame.init()
    Gameclock = pygame.time.Clock()
    dt = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid = AsteroidField()

    Player.containers = (updatable, drawable)
    player_1 = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player_1.collide(asteroid):
                print("Game Over!")
                return
            for bullet in shots:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()
        
        screen.fill(000)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = (Gameclock.tick(60))/1000



if __name__ == "__main__":
    main()