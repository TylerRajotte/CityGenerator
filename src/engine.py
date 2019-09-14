import pygame
from mesh import Mesh
from filereader import FileReader


class Engine:
    def __init__(self, windowxsize, windowysize):
        pygame.init()
        self.screen = pygame.display.set_mode((windowxsize, windowysize))
        self.clock = pygame.time.Clock()
        self.loopFinished = False
        self.drawMeshList = []

    def mainloop(self):
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
        for x in self.drawMeshList:
            x.readoutmesh(self.screen)

    def addmesh(self, meshfilelocation, pixelrange):
        meshfile = FileReader(meshfilelocation, "read")
        meshdata = []
        color = [255, 255, 255]
        complete = False
        width = 1
        for x in meshfile.fileOutput:
            if "color" in x:
                color = list(map(int, x.split("=")[1].split(" ")))
            elif "linewidth" in x:
                width = int(x.split("=")[1])
            elif "complete" in x:
                complete = bool(x.split("=")[1])
            else:
                meshdata.append(list(map(int, x.split(" "))))

        self.drawMeshList.append(Mesh(meshdata, pixelrange, color, complete, width))
