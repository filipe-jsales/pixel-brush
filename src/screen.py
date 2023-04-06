from tkinter import *

class Screen:
    def __init__(self, screenSize):
        ## initial parameters
        self.screenSize = screenSize
        self.Matrix = []
        self.matrixSize = 50
        self.pixelSize = int(self.screenSize / self.matrixSize)

        for i in range(self.matrixSize):
            line = []
            for j in range(self.matrixSize):
                line.append(0)
            self.Matrix.append(line)

        ## criar o canvas utilizando o tkinter
        self.master = Tk()
        self.screen = Canvas(self.master, width=self.screenSize, height=self.screenSize)
        self.screen.pack()

        self.CreateTemplate()

    ## função que cria a grade
    def CreateTemplate(self):
        aux = int(self.screenSize / 2) + (self.pixelSize / 2)

        for x in range(0, self.screenSize, self.pixelSize):  # horizontal lines
            self.screen.create_line(x, 0, x, self.screenSize, fill='#DCDCDC')

        for y in range(0, self.screenSize, self.pixelSize):  # vertical lines
            self.screen.create_line(0, y, self.screenSize, y, fill='#DCDCDC')

        self.screen.create_line(0, aux - self.pixelSize, self.screenSize, aux - self.pixelSize,
                         fill="#f00")  # line central - horizontal
        self.screen.create_line(aux, 0, aux, self.screenSize, fill="#f00")  # line central - vertical


    # convert to real coordinates 
    def ConvertCoordinates(self, x, y):
        real_x = int((self.pixelSize * x) + (self.screenSize / 2))
        real_y = int((self.screenSize / 2) - (self.pixelSize * y))

        return real_x, real_y

    def ConvertMatrixCoordinates(self, x, y):
        column = int(x + (self.matrixSize / 2))
        line = int((self.matrixSize / 2) - y) - 1

        return line, column

    # draw a pixel in the screen
    def DrawPixel(self, x, y, color):
        x1, y1 = self.ConvertCoordinates(x, y)
        self.screen.create_rectangle(x1, y1, x1 + self.pixelSize, y1 - self.pixelSize, fill=color)

        l, c = self.ConvertMatrixCoordinates(x, y)
        self.Matrix[l][c] = color

    def Draw(self, object: list, color):
        for p in object:
            self.DrawPixel(p[0], p[1], color)

    def printMatrix(self):
        for line in self.Matrix:
            print(line)

    def checkMatrix(self, x, y):
        l, c = self.ConvertMatrixCoordinates(x, y)
        return self.Matrix[l][c]

    def outlineWindow(self, xmin, xmax, ymin, ymax):

        xmin, ymin = self.ConvertCoordinates(xmin, ymin)
        xmax, ymax = self.ConvertCoordinates(xmax+1, ymax+1)
        self.screen.create_rectangle(xmin, ymin, xmax, ymax, outline='green')