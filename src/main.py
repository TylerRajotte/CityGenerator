from engine import *
from scipy.spatial import Voronoi
import numpy as np
import threading
import random


def startengineloop(engine):
    engine.mainloop()


def enginemanagment(engine):
    # engine.addmesh("TestMesh.mesh", (300, 300, 400, 400))
    # engine.addmesh("TestMesh.mesh", (0, 0, 100, 100))
    # engine.addmesh("ghost.mesh", (100, 100, 300, 300))
    # engine.addpoint(100, 100, (255, 255, 255), 5)
    resolution = 100
    windowx = 1000
    windowy = 600
    points = []
    for x in range(resolution):
        points.append((random.randrange(0, windowx), random.randrange(0, windowy)))

    vor = Voronoi(points)
    linedata = vor.vertices
    for x in range(len(linedata)):
        if x != len(linedata) - 1:
            print(linedata[x])
            engine.addline(linedata[x][0], linedata[x][1], linedata[x + 1][0], linedata[x + 1][1], (255, 0, 0), 2)

    for x in points:
        engine.addpoint(x[0], x[1], (0, 0, 255), 0)


if __name__ == "__main__":
    main = Engine(1000, 600)

    loopthread = threading.Thread(target=startengineloop, args=(main,))
    enginemanagementthread = threading.Thread(target=enginemanagment, args=(main,))

    loopthread.start()
    enginemanagementthread.start()
