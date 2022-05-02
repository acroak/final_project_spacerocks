'''
Andrea Croak
CS5001: Fundamentals of Computer Science
Final Project: Asteroid Clone
game file
handle the inner workings for game play like game initialization and loop, user input, collision mechanics,and win/lose conditions
May 2021
'''
import pygame, sys, time
from pygame import mixer
from pygame.math import Vector2
from helperfunctions import load_image, load_audio, get_random_position
from spriteClasses import Spaceship, Asteroid


class AsteroidGame:
    ''' 
    Class: AsteroidGame
    Attributes: none
    Methods: draw_text(), main_menu(),game_loop(), user_input(), get_sprite_objects(), game_play(), draw()
    '''
    # make sure the asteroids don't generated too close to the spaceship on launch
    min_asteroid_distance = 250

    def __init__(self):
        '''
        Constructor
        Parameters:
            self - the current object
        Initialize pygame, set title for window, set window size
        '''
        # initialize game window
        pygame.init()
        pygame.display.set_caption("Asteroids")
        
        # Background music
        mixer.init()
        bgMusicPath = load_audio("outer_space", "mp3")
        mixer.music.load(bgMusicPath)
        bgMusic = mixer.Sound(bgMusicPath)
        mixer.Channel(0).play(bgMusic)
        # loop music
        mixer.music.play(-1)

        #set surface/screen size
        self.screen = pygame.display.set_mode((800,600))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        # set bg images
        self.menu_background = load_image("menu_background", False)
        self.background = load_image("background", False)

        # fonts
        self.font = pygame.font.SysFont("comicsans", 20)
        self.fontlarge = pygame.font.SysFont("comicsans", 35)

        # track bullet instances
        self.bullets = []
        # load spaceship
        self.ship = Spaceship((400, 300), self.bullets.append)
        # track asteroids
        self.asteroids = []
        # generate 6 asteroids and ensure that the min generation distance from the spaceship is met for each instance
        for asteroid in range(6):
            position = get_random_position(self.screen)
            while position.distance_to(self.ship.positionTuple) < self.min_asteroid_distance:
                position = get_random_position(self.screen)
            self.asteroids.append(Asteroid(position, self.asteroids.append))

        # control the FPS so game runs similairly on different machines
        self.clock = pygame.time.Clock()

        # start conditions for menu and game
        self.menu_loop = True
        self.start_game = False
    
    def draw_text(self, text, font, color, surface, x, y):
        """
        blit the copy to the pygame surface
        Return: none
        Inputs: * self - the current object
                * text- copy to display
                * font - font family and size to use
                * color - font color
                * surface - pygame surface on which to superimpose images etc.
                * x, y - positional coordinates for where to place copy
        """
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft=(x,y)
        self.screen.blit(textobj, textrect)

    def main_menu(self):
        """
        create the main menu / start game conditions
        Return: none
        Inputs: * self - the current object
        """
        # start menu bg
        self.screen.blit(self.menu_background, (0,0))
        # menu copy
        title = self.fontlarge.render('ASTEROIDS' , True , (255,255,255))
        self.screen.blit(title, (350,200))
        self.draw_text('How To Play', self.font, (255,255,255), self.screen, 10, 440)
        self.draw_text('Traverse space using WASD or the arrow keys.', self.font, (255,255,255), self.screen, 10, 460)
        self.draw_text('w / up to accelerate forward', self.font, (255,255,255), self.screen, 10, 480)
        self.draw_text('a / left to roate left ', self.font, (255,255,255), self.screen, 10, 500)
        self.draw_text('d / right to rotate right', self.font, (255,255,255), self.screen, 10, 520)
        self.draw_text('s / down to brake', self.font, (255,255,255), self.screen, 10, 540)
        # start button
        pygame.draw.rect(self.screen,(22,35,44),[350,260,140,40], self.width == 0, 25)
        # pass copy to button

        text = self.fontlarge.render('START' , True , (255,255,255))
        self.screen.blit(text, (380,270))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            # start game, close menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_game = True
                self.menu_loop = False
            
        
        # updates the frames of the game
        pygame.display.update()
        self.clock.tick(60)
   
    def game_loop(self):
        """
        launches start menu and closes it once done with it. Then lauches the game
        Return: none
        Inputs: * self - the current object
        """
        #launches start menu
        while self.menu_loop == True:
            self.main_menu()

        # Checks for user input, runs game logic, and draws a frame
        while self.start_game == True:
            self.user_input()
            self.game_play()
            self.draw()
        
    def user_input(self):
        """
        handle user input from keyboard
        Return: none
        Inputs: * self - the current object
        """
        # handle items to be controlled with a single click.instance
        for keypress in pygame.event.get():
            # check to see if user closes pygame window
            if keypress.type == pygame.QUIT:
                quit()
            # handle attack
            elif keypress.type == pygame.KEYDOWN:
                # handle shooting
                if keypress.key == pygame.K_SPACE and self.ship:
                    self.ship.shoot()

        # handle held button input
        is_key_pressed = pygame.key.get_pressed()

        # if a spaceship exists allow it to respond to input
        if self.ship:
            # handle rotation
            if is_key_pressed[pygame.K_RIGHT] or is_key_pressed[pygame.K_d]:
                self.ship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT] or is_key_pressed[pygame.K_a]:
                self.ship.rotate(clockwise=False)

            # handle forwards acceleration
            if is_key_pressed[pygame.K_UP] or is_key_pressed[pygame.K_w]:
                self.ship.accelerate()

            # handle braking
            if is_key_pressed[pygame.K_DOWN] or is_key_pressed[pygame.K_s]:
                self.ship.brake()
                
    def get_sprite_objects(self):
        """
        make a list of all the current objects on the screen
        Return: none
        Inputs: * self - the current object
        """
        # make a list of lists for bullets and asteroids
        game_objects = [*self.asteroids, *self.bullets]

        if self.ship:
            game_objects.append(self.ship)

        return game_objects

    def game_play(self):
        """
        move objects across the screen, detect collisions and handle the win/lose conditions
        Return: none
        Inputs: * self - the current object
        """
        # wrap all moving objects to the screen dimensions
        for game_object in self.get_sprite_objects():
            game_object.move(self.screen)

        # delete bullets once they exit the surface dimensions
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.positionTuple):
                self.bullets.remove(bullet)
        
         # handle bullet collision (asteroid vs. bullet)
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    return

        # handles collision (asteroid vs. ship)
        if self.ship:
            for asteroid in self.asteroids:
                # lose condition
                if asteroid.collides_with(self.ship):
                    self.ship = None
                    mixer.Channel(4).play(mixer.Sound(load_audio("ship_explosion", "wav")))
                    header = self.fontlarge.render('GAMEOVER' , True , (255,255,255))
                    subheader = self.fontlarge.render("Press 'R' to replay" , True , (255,255,255))
                    self.screen.blit(header, Vector2((350,280)))
                    self.screen.blit(subheader, Vector2((315,325)))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    self.menu_loop = True
                    self.start_game = False
                    pygame.display.update()
                    self.asteroids = []
                    return 
        # Win condition
        if len(self.asteroids) == 0:
            header = self.fontlarge.render('WINNER!!' , True , (255,255,255))
            subheader = self.fontlarge.render("Press 'R' to replay" , True , (255,255,255))
            self.screen.blit(header, Vector2((350,280)))
            self.screen.blit(subheader, Vector2((315,325)))
            pygame.display.update()
            pygame.time.wait(3000)
            self.menu_loop = True
            self.start_game = False
            pygame.display.update()
            return
                    
    def draw(self):
        """
        update all sprites on the screena s they move around and interact
        Return: none
        Inputs: * self - the current object
        """
        self.screen.blit(self.background, (0,0))

        for game_object in self.get_sprite_objects():
            game_object.draw(self.screen)
        # renders all assets at the same time onto the surface
        pygame.display.flip()
        self.clock.tick(60)

    