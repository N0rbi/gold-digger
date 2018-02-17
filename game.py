import pygame
import time
import input
from gameObject.dynamicGameObject import DynamicGameObject


class Game:
    __devBlue = (50, 110, 255)

    def __init__(self, width, height, tank):
        pygame.init()
        self.__size = self.__width, self.__height = width, height
        self.__pgScreen = pygame.display.set_mode(self.__size)
        self.__running = True
        self.gameObjects = []
        self.__tank = tank
        self.__input_handler = input.InputHandler(self.__tank)

    # Renders content to the screen
    def _render(self):
        [o.render(self.__pgScreen) for o in self.gameObjects]

    # Game loop
    def tick(self):
        lasttime = time.time()

        while self.__running:
            events = pygame.event.get()

            commands = self.__input_handler.get_commands(events)
            if input.QUIT_GAME in commands:
                break

            for go in self.gameObjects:
                if isinstance(go, DynamicGameObject):
                    go.tick(time.time()-lasttime)

            lasttime = time.time()
            self.__pgScreen.fill(self.__devBlue)
            self._render()
            pygame.display.flip()
