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
    try:
        asteroids = AsteroidGame()
        asteroids.game_loop() 
    except ValueError as valErr:
        print(valErr, "Something Math'd wrong")

    except TypeError as typeErr:
        print(typeErr, "oops, please contact your adminstrator")

    except KeyboardInterrupt as interupt:
        print("\n", "The user has force quit the program")

    except OSError as osErr:
        print(osErr, "Something has gone wrong, please check external USB devices and connections")
        

          


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