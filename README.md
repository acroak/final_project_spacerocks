# Asteroid Python Clone
## CS5001 Final project

## Installation
This project uses Python 3.8.0
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pygame
```

## How to Lauch
navigate to the __main__.py file and initialize

## How to Play
Using the arrow keys or wasd navigate around the screen and destroy asteroids using (spacebar) to shoot.
Left Arrow	← / a -- Rotate the ship anticlockwise
Up Arrow	↑ / w -- Accelerate ship in direction its pointing
Right Arrow	→ / d -- Rotates the ship clockwise
Down Arrow	↓ / s -- Hit the brakes and slow down
(spacebar) -- Shoot bullets (no holding you need to tap!)

## Credits
### Assets
Start Menu Background:https://wallpaperaccess.com/full/2773642.jpg
Game Background: https://bacteri.itch.io/background-space  
Ship Sprite: https://opengameart.org/content/animated-spaceships
Asteroid Sprite: https://opengameart.org/content/brown-asteroid 
Background Audio:https://opengameart.org/content/outer-space-loop  
Shooting Audio: https://pixabay.com/sound-effects/search/v-ktor/
Asteroid Explosion Audio: https://opengameart.org/content/explosion-0
Ship Explosion Audio: https://freesound.org/people/JapanYoshiTheGamer/sounds/361258/

### Reference
https://www.pygame.org/docs/
The Vectors took some head scratching to eventually understand
https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
http://cs1110.cs.cornell.edu/docs/geom_vector2.html  
https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/  
https://realpython.com/asteroids-game-python/  
https://www.pygame.org/project/713 

### Things to add on
Implimenting a life bar/ number of lives before game over
Pointing system 
Spaceship inivincibility on respawn at center coordinate
Adding sprite animations to Spaceship move() and collision events
Ability to choose a difficulty level (getting 10 asteroids to spawn @ the start vs 6) or continously increasing the number of asteroids spawned based on a timer.
A better restart menu
Ability to use "esc" button to leave game
Ability to use "enter" button to start the game
