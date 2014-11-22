import pygame
from pygame.locals import *

class SimpleGame(object):
    
    def __init__(self,
                title,
                window_size=(640, 480),
                fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps
        self.is_terminated = False
        
    def terminate(self):
        self.is_terminated = True

    def __handle_events(self):
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                self.on_key_down(key)
            elif event.type == KEYUP:
                self.on_key_up(key)


    def on_key_up(self, key):
        print "up"

    def on_key_down(self, key):
        print "down"
    
    def run(self):
        self.init()
        while not self.is_terminated:
            self.__handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

    def init(self):
        self.__game_init()

    def update(self):
        pass

    def render(self):
        pass

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)

