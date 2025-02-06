import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    pygame.init()
    Gameclock = pygame.time.Clock()
    dt = 0
    player_1 = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player_1.update(dt)
        screen.fill(000)
        player_1.draw(screen)
        pygame.display.flip()
        dt = (Gameclock.tick(60))/1000



if __name__ == "__main__":
    main()