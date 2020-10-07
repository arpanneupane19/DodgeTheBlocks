DodgeTheBlocks

## Built With:

Python 3.7.9
Pygame - 2D graphics library



## Features:

Navigation menu.
1. Collision between player block and enemy block.
2. Collision between player block and wall.
3. Recording the score.
4. Option to select background music or turn it off.



## File Structure:

1. DodgeTheBlocks.py - Contains the main game.
2. sfx_hit.wav - Contains the sound of the player colliding with other objects.
3. song1.wav and song2.wav - Contain the background music.


Installing PyGame:

1. Windows -
```bash 
pip install pygame
```
2. macOS - 
```bash
pip3 install pygame
```

3.Ubuntu/Debian - 
```bash
sudo apt-get python3-pygame
```



## Playing the game:

The goal in the game is for you to dodge the red block that falls from the top of the screen.
The more times you dodge it, the faster the block gets but your speed also increases whenever your
score increases.
If you want to pause the game, you can press "p" and it will pause. To continue press "c" and to
exit press "q". 
If you crash or collide with the enemy block or the wall, your score resets, your speed resets and the enemy
block's speed resets. 
If you want to see the keybinds, whenever you launch the game, there is a button for help which will show you
the mechanics of the game.

