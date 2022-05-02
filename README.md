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
Using the arrow keys or wasd navigate around the screen and destroy asteroids using (spacebar) to shoot. <br/>
Left Arrow	← / a -- Rotate the ship anticlockwise <br/>
Up Arrow	↑ / w -- Accelerate ship in direction its pointing <br/>
Right Arrow	→ / d -- Rotates the ship clockwise <br/>
Down Arrow	↓ / s -- Hit the brakes and slow down <br/>
(spacebar) -- Shoot bullets (no holding you need to tap!) <br/>

## Credits
### Assets
Start Menu Background:https://wallpaperaccess.com/full/2773642.jpg<br/>
Game Background: https://bacteri.itch.io/background-space<br/>
Ship Sprite: https://opengameart.org/content/animated-spaceships<br/>
Asteroid Sprite: https://opengameart.org/content/brown-asteroid<br/>
Background Audio:https://opengameart.org/content/outer-space-loop<br/>
Shooting Audio: https://pixabay.com/sound-effects/search/v-ktor/<br/>
Asteroid Explosion Audio: https://opengameart.org/content/explosion-0<br/>
Ship Explosion Audio: https://freesound.org/people/JapanYoshiTheGamer/sounds/361258/<br/>

### Reference
https://www.pygame.org/docs/<br/>
The Vectors took some head scratching to eventually understand<br/><br/>
https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2<br/>
http://cs1110.cs.cornell.edu/docs/geom_vector2.html<br/><br/>  
https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/<br/>  
https://realpython.com/asteroids-game-python/<br/>  
https://www.pygame.org/project/713<br/> 

### Things to add on
Implimenting a life bar/ number of lives before game over<br/>
Pointing system<br/>
Spaceship inivincibility on respawn at center coordinate<br/>
Adding sprite animations to Spaceship move() and collision events<br/>
Ability to choose a difficulty level (getting 10 asteroids to spawn @ the start vs 6) or continously increasing the number of asteroids spawned based on a timer.<br/>
A better restart menu<br/>
Ability to use "esc" button to leave game<br/>
Ability to use "enter" button to start the game<br/>
Make asteroid Sprites rotate through space as they move<br/>
