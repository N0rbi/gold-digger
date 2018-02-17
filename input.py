import pygame

QUIT_GAME = 10000
MOVE_LEFT = 10001
MOVE_RIGHT = 10002
MOVE_UP = 10003
MOVE_DOWN = 10004


class InputHandler:

    def __init__(self, tank):
        self.__tank = tank
        self.__keydown_buffer = []

    def get_commands(self, events):
        commands = []
        for event in events:
            if event.type == pygame.QUIT:
                commands.append(QUIT_GAME)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.__keydown_buffer.append(MOVE_LEFT)
                if event.key == pygame.K_d:
                    self.__keydown_buffer.append(MOVE_RIGHT)
                if event.key == pygame.K_w:
                    self.__keydown_buffer.append(MOVE_UP)
                if event.key == pygame.K_s:
                    self.__keydown_buffer.append(MOVE_DOWN)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.__keydown_buffer.remove(MOVE_LEFT)
                if event.key == pygame.K_d:
                    self.__keydown_buffer.remove(MOVE_RIGHT)
                if event.key == pygame.K_w:
                    self.__keydown_buffer.remove(MOVE_UP)
                if event.key == pygame.K_s:
                    self.__keydown_buffer.remove(MOVE_DOWN)

        self.__tank.commands.extend(self.__keydown_buffer)
        return commands
