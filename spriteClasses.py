'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
spriteClasses file
contains generic sprite class, asteroid, spaceship and bullet classes
May 2021
'''

import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom as imageRotate
from pygame import mixer
from helperfunctions import load_image, load_audio, wrap_position, get_random_velocity

# vector constant
UP = Vector2(0,-1)

class GamePieces:
    ''' 
    Class: GamePieces
    generic class for all game objects (spaceship, asteroids, enemies)
    Attributes: positionTuple, image, speed
    Methods: draw(), move(), collides_with()
    '''
    def __init__(self, positionTuple, image, speed):
        '''
        Constructor - creates a new instance of GamePieces
        Parameters -
           self - the current object
           poisitionTuple - the (x,y) position of the object
           image - the sprite image associated with the instance
           speed - the velocity at which the sprite is travelling 
        '''
        # (x,y) point tuple to be converted into vector to help move items around and determine distance between objects
        self.positionTuple = Vector2(positionTuple)
        # sprite image to be drawn
        self.image = image
        # for circle based collision
        self.radius = image.get_width()/2
        # tuple with speed and direction
        self.speed = Vector2(speed)

    def draw(self, surface):
        """
        Draw sprites/assets to the pygame surface
        Return: none
        Inputs: * self - the current object
                * surface - pygame surface on which to superimpose images etc.
        """
        # Vectors help make the positional math easier by moving from a center based cooridinate to a top left (0,0) coordinate, which is pygames default.
        position = self.positionTuple - Vector2(self.radius)
        # get sprite image into the pygame window.
        surface.blit(self.image, position)

    def move(self, surface):
        """
        updates objects position by using the speed and direction from the speed tuple
        Return: none
        Inputs: * self - the current object
                * surface - pygame surface on which to move images etc across.
        """
        self.positionTuple = wrap_position(self.positionTuple + self.speed, surface)

    def collides_with(self, other):
        """
        finds the distance between the center of object A and object "other" to see if they overlap
        Return: none
        Inputs: * self - the current object
                * other - instance of another sprite to check distance against
        """
        distance = self.positionTuple.distance_to(other.positionTuple)
        print("distance",distance)
        print("ship radius", self.radius)
        print("asteroid radius", other.radius)
        return distance < (self.radius -10) + (other.radius -10)

class Spaceship(GamePieces):
    ''' 
    Class: Spaceship
    subclass that inherits from the gamepieces class and controls the players sprite
    Attributes: position, bullet_callback
    Methods: rotate(), draw(), accelerate(), brake(), shoot()
    '''
    # static global variables
    maneuverability = 3 #(0 - 3)
    acceleration = 0.05
    deceleration = -0.25
    bullet_speed = 3 #(0 - 3)
    def __init__(self, position, bullet_callback):
        '''
        Constructor - creates a new instance of Spaceship
        Parameters -
           self - the current object
           poisition - the (x,y) position of the object
           bullet_callback - callback function to coninuously produce bullets when (spacebar) is hit 
        '''
        self.bullet_callback = bullet_callback
        # spawn spaceship facing up/toward the north of the screen
        self.direction = Vector2(UP)
        super().__init__(position, load_image("spaceship"), Vector2(0))

    def rotate(self, clockwise = True):
        """
        rotates the spaceship sprite according to true/false generated from user input
        Return: none
        Inputs: * self - the current object
                * clockwise - id the sprite should rotate left (anticlockwise) or right (clockwise)
        """
        sign = 1 if clockwise else -1
        angle = self.maneuverability * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        """
        updates the sprite image to visually show the rotation of left/right
        Return: none
        Inputs: * self - the current object
                * surface - pygame surface on which to superimpose images etc.
        """
        angle = self.direction.angle_to(UP)
        rotated_surface = imageRotate(self.image, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.positionTuple - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        """
        increases the spaceship objects velocity
        Return: none
        Inputs: * self - the current object
        """
        self.speed += self.direction * self.acceleration
        
    def brake(self):
        """
        decreases the spaceship objects velocity
        Return: none
        Inputs: * self - the current object
        """
        # print('speed at time of brake', self.speed)
        if self.speed[0] >= 0 and self.speed[1] >= 0:
            self.speed = [self.speed[0], self.speed[1] + self.deceleration]
        elif self.speed[0] >= 0 and self.speed[1] <= 0:
            self.speed = [self.speed[0], self.speed[1] + self.acceleration]
        elif self.speed[0] <= 0 and self.speed[1] <= 0:
            self.speed = [self.speed[0], self.speed[1] + self.acceleration]
        else:
            self.speed = [self.speed[0], self.speed[1] + self.deceleration]
        # print('speed after brake', self.speed)

    def shoot(self):
        """
        creates a bullet instance and uses the bullet_callback to append to on going bullet list
        Return: none
        Inputs: * self - the current object
        """
        bullet_velocity = self.direction * self.bullet_speed + self.speed
        bullet = Bullet(self.positionTuple, bullet_velocity)
        self.bullet_callback(bullet)
        mixer.Channel(1).play(mixer.Sound(load_audio("laser", "mp3")))       

class Asteroid(GamePieces):
    ''' 
    Class: Asteroid
    subclass that inherits from the gamepieces class and controls the "enemy" sprites
    Attributes: asteroid_callback, size
    Methods: split()
    '''
    def __init__(self, position, asteroid_callback, size = 3):
        '''
        Constructor - creates a new instance of an asteroid
        Parameters -
           self - the current object
           poisition - the (x,y) position of the object, to be randomized
           asteroid_callback - callback function to coninuously produce asteroids at the intilaization of the game 
        '''
        self.asteroid_callback = asteroid_callback
        self.size = size
        # asteroid image size relations
        size_to_scale = {
            3: 1,
            2: 0.5,
            1: 0.25,
        }
        scale = size_to_scale[size]
        # control image size
        image = imageRotate(load_image("asteroid"), 0, scale)
        super().__init__(position, image, get_random_velocity(1,3))

    def split(self):
        """
        when an asteroid of scale 3 or 2 is hit by a bullet it divides itself in two down to the next smallest scale. 3 -> 2/2 -> 1,1/1,1
        Return: none
        Inputs: * self - the current object
        """
        mixer.Channel(2).play(mixer.Sound(load_audio("explosion", "wav"))) 
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid(
                    self.positionTuple, self.asteroid_callback, self.size - 1
                )
                self.asteroid_callback(asteroid)

class Bullet(GamePieces):
    ''' 
    Class: Bullet
    subclass that inherits from the gamepieces class and spaceship projectiles
    Attributes: position, velocity
    Methods: move()
    '''
    def __init__(self, position, velocity):
        '''
        Constructor - creates a new instance of an asteroid
        Parameters -
           self - the current object
           poisition - the (x,y) position of the object, to be randomized
           velocity - the speed and angle at which the bullet was fired from
        '''
        super().__init__(position, load_image("bullet2"), velocity)

    def move(self, surface):
        """
        edited version of GamePiece method in order to not allow bullets to wrap around the screen dimensions
        Return: none
        Inputs: * self - the current object
                * surface - pygame surface on which to superimpose images etc.
        """
        self.positionTuple = self.positionTuple + self.speed