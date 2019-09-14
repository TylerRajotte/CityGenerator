from engine import *
import threading


def startengineloop(engine):
    engine.mainloop()


def mesh(engine):
    #engine.addmesh("TestMesh.mesh", (300, 300, 400, 400))
    engine.addmesh("ghost.mesh", (100, 100, 300, 300))


if __name__ == "__main__":
    main = Engine(500, 400)

    loopthread = threading.Thread(target=startengineloop, args=(main,))
    meshthread = threading.Thread(target=mesh, args=(main,))

    loopthread.start()
    meshthread.start()
