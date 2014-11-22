import pygame
from pygame.locals import *
from gamelib import SimpleGame

class SquashGame(SimpleGame):
    pass

def init(self):
    super(SquashGame, self).game_init()

def main():
    game = SquashGame("Squash Game")
    game.run()

if __name__ == '__main__':
    main()
