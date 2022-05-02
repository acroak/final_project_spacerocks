'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
__Main__ file, run the game from this file.
May 2021
'''
import pygame
from game import AsteroidGame

def main():
    asteroids = AsteroidGame()
    asteroids.game_loop() 

          


if __name__ == "__main__":
    main()
    done = False
    # to restart the program after a win or loss
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()     