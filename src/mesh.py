import pygame


class Mesh:
    def __init__(self, data, pixelrange, color, completemesh, width):
        """Data structure [[pointx, pointy], [pointx, pointy]...]
        Pixerange structure [minx, miny, maxx, maxy]"""
        # Takes in cords and outputs them to pixel values then uses those to make pygame lines
        self.inputdata = data
        self.pixelrange = pixelrange
        self.color = color
        self.completemesh = completemesh
        self.width = width

        self.flipyvalues()
        self.pixeldata = []
        self.__rendertopixel()

    def __rendertopixel(self):
        # Takes in cord data and outputs pixel values
        maxandmin = self.__findmaxandmin()
        for x in self.inputdata:
            xvalue = x[0]
            yvalue = x[1]

            # Elimanate negative numbers if they are there
            if maxandmin[0] < 0:
                xvalue = x[0] + (maxandmin[0] * -1)

            if maxandmin[1] < 0:
                yvalue = x[1] + (maxandmin[1] * -1)

            # Check if zero and scale values to between 0 and 1
            if maxandmin[2] + (maxandmin[0] * -1) == 0:
                xvalue = 0
            else:
                xvalue = xvalue / (maxandmin[2] + (maxandmin[0] * -1))

            if maxandmin[3] + (maxandmin[1] * -1) == 0:
                yvalue = 0
            else:
                yvalue = yvalue / (maxandmin[3] + (maxandmin[1] * -1))

            # Scale up to proper area and shift to proper place
            areax = self.pixelrange[2] - self.pixelrange[0]
            areay = self.pixelrange[3] - self.pixelrange[1]
            xvalue = (areax * xvalue) + self.pixelrange[0]
            yvalue = (areay * yvalue) + self.pixelrange[1]

            # Append Data so it can be drawn later
            self.pixeldata.append((xvalue, yvalue))

    def __findmaxandmin(self):
        # Gets data in a way to make use of max and min functions then uses those functions
        # It then returns all of the maxs and mins in a tuple
        allofx = []
        allofy = []
        for x in self.inputdata:
            allofx.append(x[0])
            allofy.append(x[1])

        final = (min(allofx), min(allofy), max(allofx), max(allofy))
        return final

    def flipyvalues(self):
        for x in range(len(self.inputdata)):
            self.inputdata[x] = (self.inputdata[x][0], self.inputdata[x][1] * -1)

    def readoutmesh(self, plane):
        # Pygame render code that can be called repeatedly
        pygame.draw.lines(plane, self.color, self.completemesh, self.pixeldata, self.width)