import pygame


class Line:
    def __init__(self, xpos1, ypos1, xpos2, ypos2, color, width):
        self.xpos1 = xpos1
        self.ypos1 = ypos1
        self.xpos2 = xpos2
        self.ypos2 = ypos2
        self.color = color
        self.width = width

    def readout(self, surface):
        pygame.draw.line(surface, self.color, (self.xpos1, self.ypos1), (self.xpos2, self.ypos2), self.width)
