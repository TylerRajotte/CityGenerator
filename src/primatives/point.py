import pygame


class Point:
    def __init__(self, xpos, ypos, color, size):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.size = size

    def readout(self, surface):
        pygame.draw.circle(surface, self.color, (self.xpos, self.ypos), self.size)
