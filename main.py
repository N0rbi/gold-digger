from game import Game
import pygame
from gameObject.interface.text_display import TextDisplay
from gameObject.environment.blocks.blockFactory import BlockFactory
from gameObject.tank.tank import Tank

# Main handles file loading (possible network managing), and the configuration of the game (images, sounds)

def ground():
    bf = BlockFactory(400, 400, 64)
    blocks = []
    for i in range(-10, 10):
        for j in range(3):
            blocks.append(bf.get_block(i, j))
    return blocks


tank = Tank(400, 100, 1.)
game = Game(800, 600, tank)
#hp_display = TextDisplay(50, 500, font_size=20, text="HP:"+tank.get_hp())

game.gameObjects.extend(ground())
game.gameObjects.extend([tank])
#game.gameObjects.extend([hp_display])

game.tick()
