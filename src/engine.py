import pygame
from mesh import *


class Window:
    def __init__(self, windowxsize, windowysize):
        pygame.init()
        self.screen = pygame.display.set_mode((windowxsize, windowysize))
        self.clock = pygame.time.Clock()
        self.loopFinished = False

        meshdata = [[2, 0], [1, 2], [0, 2], [-1, 2], [-2, 0], [-1, -2], [0, -2], [1, -2]]
        # pixelrange = [0, 0, windowxsize, windowysize]
        # meshdata = [[-1, 1], [1, -1]]
        pixelrange = [100, 100, 300, 300]

        self.newmesh = Mesh(meshdata, pixelrange, (255, 0, 0), True, 5)

        self.__mainloop()

    def __mainloop(self):
        while not self.loopFinished:
            self.__handleevents()
            self.__draw()
            pygame.display.flip()
            self.clock.tick(60)

    def __handleevents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loopFinished = True

    def __draw(self):
        self.screen.fill((0, 0, 0))
        self.newmesh.readoutmesh(self.screen)


