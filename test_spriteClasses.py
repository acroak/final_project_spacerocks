'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
spriteClasses TESTING file
May 
'''
import unittest, pygame, spriteClasses, helperfunctions
from pygame.math import Vector2

class TestGamePieces(unittest.TestCase):
    # constructor tests
    def test_init(self):
        testImage = helperfunctions.load_image("testSprite")
        gamePiece1 = spriteClasses.GamePieces((300,400), testImage, 1)

        self.assertEqual(gamePiece1.positionTuple, (300,400))
        self.assertEqual(gamePiece1.radius, 150)
        self.assertEqual(gamePiece1.speed, [1,1])

        testImage = helperfunctions.load_image("spaceship")
        gamePiece2 = spriteClasses.GamePieces((250,625), testImage, 3)
        self.assertEqual(gamePiece2.positionTuple, (250,625))
        self.assertEqual(gamePiece2.radius, 16)
        self.assertEqual(gamePiece2.speed, [3,3])


    def test_draw(self):
        position = (300,400) - Vector2(150)
        self.assertEqual(position, [150,250])
        position = (600,270) - Vector2(150)
        self.assertEqual(position, [450,120])
        position = (0,0) - Vector2(150)
        self.assertEqual(position, [-150,-150])

    def test_move(self):
        screen = pygame.display.set_mode((800,600))
        testImage = helperfunctions.load_image("testSprite")
        gamePiece1 = spriteClasses.GamePieces((300,400), testImage, 1) 
        gamePiece1.positionTuple = helperfunctions.wrap_position(gamePiece1.positionTuple + gamePiece1.speed, screen)
        assert gamePiece1.positionTuple == [301, 401], gamePiece1.positionTuple + "  traveled position does not equal"
        for _ in range(5):
            gamePiece1.positionTuple = helperfunctions.wrap_position(gamePiece1.positionTuple + gamePiece1.speed, screen)

        assert gamePiece1.positionTuple == [306, 406], gamePiece1.positionTuple + "  long traveled position does not equal"

    def test_collides_with(self):
        testImage = helperfunctions.load_image("testSprite")
        gamePiece1 = spriteClasses.GamePieces((300,400), testImage, 1) 
        gamePiece2 = spriteClasses.GamePieces((250,350), testImage, 2) 

        distance = gamePiece1.positionTuple.distance_to(gamePiece2.positionTuple)
        collision_status = distance < gamePiece1.radius + gamePiece2.radius
        assert collision_status == True, "collision error"

        gamePiece1 = spriteClasses.GamePieces((20,20), testImage, 1) 
        gamePiece2 = spriteClasses.GamePieces((350,350), testImage, 2)
        distance = gamePiece1.positionTuple.distance_to(gamePiece2.positionTuple)
        collision_status = distance < gamePiece1.radius + gamePiece2.radius
        assert collision_status == False, "collision error"

class TestSpaceship(unittest.TestCase):
    
    def test_rotate(self):
        # clockwise
        UP = Vector2(0,-1)
        direction = Vector2(UP)
        sign = 1 
        angle = 3 * sign
        assert direction == [0, -1], "rotation item did not appear at expected position"
        direction.rotate_ip(angle)
        assert direction == [0.052336, -0.99863], "rotation item did not rotate clockwise"
        direction.rotate_ip(angle)
        assert direction == [0.104528, -0.994522], "rotation item did not rotate clockwise"
        # anticlockwise
        direction = Vector2(UP)
        sign = -1
        angle = 3 * sign
        assert direction == [0, -1], "rotation item did not appear at expected position"
        direction.rotate_ip(angle)
        assert direction == [-0.052336, -0.99863], "rotation item did not rotate anticlockwise"
        direction.rotate_ip(angle)
        assert direction == [-0.104528, -0.994522], "rotation item did not rotate clockwise"

    def test_speed(self):
        ship = spriteClasses.Spaceship((400,300),None)
        ship.deceleration = -0.25
        ship.direction = Vector2(0, -1)
        assert ship.speed == [0,0], "speed did not initialize at 0"
        # acceleration()
        for _ in range(3):
            ship.speed += ship.direction * 0.05
        assert ship.speed == [0, -0.15], "ship speed in not increasing as expected"

        #  brake()
        if ship.speed[0] >= 0 and ship.speed[1] >= 0:
            ship.speed = [ship.speed[0], ship.speed[1] + ship.deceleration]
        elif ship.speed[0] >= 0 and ship.speed[1] <= 0:
            ship.speed = [ship.speed[0], ship.speed[1] + ship.acceleration]
        elif ship.speed[0] <= 0 and ship.speed[1] <= 0:
            ship.speed = [ship.speed[0], ship.speed[1] + ship.acceleration]
        else:
            ship.speed = [ship.speed[0], ship.speed[1] + ship.deceleration]
        assert ship.speed == [0.0, -0.10000000000000002], "Ship is not braking at given amount"

    def test_shoot(self):
        bullets = []
        bullet_speed = 3
        ship = spriteClasses.Spaceship((400,300), bullets.append)
        ship.speed = [1,1]
        bullet_velocity = ship.direction * bullet_speed + ship.speed
        assert bullet_velocity == [1, -2], "issue generating bullet during shoot method in Spaceship"
        bullet = spriteClasses.Bullet(ship.positionTuple, bullet_velocity)
        assert bullet.positionTuple == [400, 300], "test_shoot() error generating bullet spawn point"

class TestAsteroid(unittest.TestCase):
    def test_init(self):
        test_asteroid = spriteClasses.Asteroid([100,100], None)
        assert test_asteroid.size == 3, "Asteroids not initializing with default size 3"
        assert test_asteroid.positionTuple == [100,100], "Asteroid not initializing with given coord."
    
    def test_split(self):
        asteroids_list = []
        test_asteroid = spriteClasses.Asteroid([100,100], None)
        if test_asteroid.size > 1:
            for _ in range(2):
                asteroid = spriteClasses.Asteroid(
                    test_asteroid.positionTuple, asteroids_list, test_asteroid.size - 1
                )
        for asteroid in asteroids_list:
            assert asteroid.size == 2, "Asteroid split error"

class TestBullet(unittest.TestCase):
    def test_init(self):
        test_bullet = spriteClasses.Bullet([200,200], 3)
        assert test_bullet.positionTuple == [200,200], "Bullet not initializing at given coord"
        assert test_bullet.speed == [3,3], "Bullet not initializing at given speed/velocity"

    def test_move(self):
        test_bullet = spriteClasses.Bullet([200,200], 3)
        test_bullet.positionTuple = test_bullet.positionTuple + test_bullet.speed
        assert test_bullet.positionTuple == [203,203], "Bullet not moving at given speed"
        for _ in range(10):
            test_bullet.positionTuple = test_bullet.positionTuple + test_bullet.speed
        assert test_bullet.positionTuple == [233,233], "Bullet not moving at large given speed"










        
        



def main():
    # pygame needs an initialization to test
    pygame.init()
    pygame.display.set_mode((800,600))
    unittest.main()

main()