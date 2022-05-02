'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
Helper Function TESTING file
May 2021
'''
import unittest, os, random
from pygame.math import Vector2

class test_helperFunctions(unittest.TestCase):
    def test_load_image(self):
        imageNames = ["asteroid.png", "background.png", "bullet2.png", "menu_background.png", "spaceship.png", "testSprite.png"]
        for image in imageNames:
            imageExists = None
            if os.path.exists('assets/images/' + image):
                # print ("Image File exists")
                imageExists = True
            else:
                # print ("Image File does not exist")
                imageExists = False
            assert imageExists == True, (image + " image does not exist")
    
    def test_load_audio(self):
        audioNames = ["explosion.wav", "laser.mp3", "outer_space.mp3", "ship_explosion.wav"]
        for audio in audioNames:
            audioExists = None
            if os.path.exists('assets/audio/' + audio):
                # print ("Audio File exists")
                audioExists = True
            else:
                # print ("Audio File does not exist")
                audioExists = False
            assert audioExists == True, (audio + " audio does not exist")
    
    def test_wrap_position(self):
        # width and height of screen are constant
        w, h = (800, 600)
        # top right
        x, y = (0, 600)
        assert Vector2(x % w, y % h) == [0,0]
        # bottom right -ish
        x, y = (400, 600)
        assert Vector2(x % w, y % h) == [400,0], "Wrap Position tuple error"
        # center screen
        x, y = (400, 300)
        assert Vector2(x % w, y % h) == [400, 300], "Wrap Position tuple error"
    
    def test_get_random_position(self):
        # width and height of screen are constant
        w, h = (800, 600)

        random_coord = Vector2(
            random.randrange(w),
            random.randrange(h)
        )
        assert random_coord[0] >= 0, "Error with random coodrinate, width less than zero"
        assert random_coord[0] <= 800, "Error with random coordinate, width is greater than 800"
        assert random_coord[1] >= 0, "Error with random coodrinate, height less than zero"
        assert random_coord[1] <= 800, "Error with random coordinate, height is greater than 600"
    
    def get_random_velocity(self):
        speed = random.randint(1, 3)
        angle = random.randrange(0, 360) 
        assert speed >= 1, "Speed error, less than 1"
        assert speed <= 3, "Speed error, greater than 3"
        assert angle >= 0, "Angle error, less than 0"
        assert angle <= 360, "Angle error, greater than 360"
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()