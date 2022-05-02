'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
helper functions file
May 2021
'''
import random
import pygame
from pygame.math import Vector2
from pathlib import Path


def load_image(name, with_alpha = True):
    """
    Returns the correct filepath for image assests and converts to pygame image format
    Inputs: * name: file name
            * with_alpha: default to true for PNG transparentcy handling
    """
    filename = Path(__file__).parent / Path("assets/images/" + name + ".png")
    sprite = pygame.image.load(filename.resolve())

    if with_alpha:
        # convert transparency on .pngs to alpha mode in pygame
        return sprite.convert_alpha()
    # for images not requiring alpha you can use the regualr convert method to change file types into pygame image files
    return sprite.convert()

def load_audio(name, file_type):
    """
    Returns the created file path for audio assets
    Inputs: * name: name of audio file
            * file_type: type of audio file format (mp3, wav, etc)
    """
    filename = Path(__file__).parent / Path("assets/audio/" + name + "." + file_type)
    print(filename)
    return filename

# wrap screen objects so they dont continue out into the void
def wrap_position(position, surface):
    """
    Returns the calculated sister vector poin on the opposit side of the surface
    Inputs: * position: current (x,y) position of object
            * surface: the dimesions of pygames surface/window
    """
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

# generate random x,y tuple for asteroids
def get_random_position(surface):
    """
    Returns random (x,y) position
    Inputs: * surface: the dimensions of pygames surface/window
    """
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height())
    )

# generate random velocity and vector or asteroids
def get_random_velocity(min_speed, max_speed):
    """
    Returns a random velocity and angle of rotation for asteroids
    Inputs: * min and max speed: osme asteroids will be slow and some fast
    """
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)

