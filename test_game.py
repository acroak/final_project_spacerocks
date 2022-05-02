'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
Game TESTING file
May 2021
'''
import unittest, os, game, spriteClasses, helperfunctions

class test_AsteroidGame:
    def test_init(self):
        test_game = game.AsteroidGame()
        assert test_game.screen == [800,600], "Game Surface not initializing at default size"
        assert test_game.width == 800, "Game Surface issue with width size"
        assert test_game.height == 600, "Game Surface issue with height size"
        assert test_game.bullets == [], "Game is initializing with bullet instances, should be empty list"
        assert test_game.ship.positionTuple == [400,300], "Default Spaceship spawn point is incorrect"
        assert test_game.asteroids == [], "Game is initializing with asteroid instances, should be empty list"
        for asteroid in range(6):
            position = helperfunctions.get_random_position(test_game.screen)
            while position.distance_to(test_game.ship.positionTuple) < 250:
                position = helperfunctions.get_random_position(test_game.screen)
            test_game.asteroids.append(spriteClasses.Asteroid(position, test_game.asteroids.append))
        assert len(test_game.asteroids) == 6, str(len(test_game.asteroids)) + " asteroids were generated, should be 6"
        assert test_game.menu_loop == True, "Game is not initializing the menu first"
        assert test_game.start_game == False, "Game is immediately exicuting the game loop.... should first be the menu"

        # draw_text(), main_menu(), game_loop(), user_input() feel like visual/manual QA tests


def main():
    unittest.main()

if __name__ == "__main__":
    main()