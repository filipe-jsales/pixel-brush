from tkinter import *


class Screen:
    """
    @Author: Filipe Eduardo Junqueira Sales
    @Author: João Davi Costa Lima
    @Github: https://github.com/filipe-jsales
    @Date: 2023-05-24
    @Version: 0.0.1
    @LinkedIn: https://www.linkedin.com/in/filipe-sales/
    
    A class representing the screen for drawing and visualization.

    The Screen class provides functionality for creating and managing a graphical screen using the tkinter library.
    It allows drawing pixels, lines, and rectangles, as well as converting between screen coordinates and matrix coordinates.

    Attributes:
        screenSize (int): The size of the screen in pixels.
        Matrix (list): The matrix representing the screen.
        matrixSize (int): The size of the matrix used for coordinate conversion.
        pixelSize (int): The size of each pixel on the screen.
        master (Tk): The Tkinter root object.
        screen (Canvas): The Tkinter canvas object representing the screen.
    """

    def __init__(self, screenSize):
        """
        Initializes a Screen object with the given screen size.

        Args:
            screenSize (int): The size of the screen in pixels.
        """
        self.screenSize = screenSize
        self.Matrix = []
        self.matrixSize = 50
        self.pixelSize = int(self.screenSize / self.matrixSize)

        for i in range(self.matrixSize):
            line = []
            for j in range(self.matrixSize):
                line.append(0)
            self.Matrix.append(line)

        self.master = Tk()
        self.screen = Canvas(self.master, width=self.screenSize, height=self.screenSize)
        self.screen.pack()

        self.CreateTemplate()

    def CreateTemplate(self):
        """
        Creates the template for the screen, including grid lines and a central axis line.
        """
        aux = int(self.screenSize / 2) + (self.pixelSize / 2)

        for x in range(0, self.screenSize, self.pixelSize):  # horizontal lines
            self.screen.create_line(x, 0, x, self.screenSize, fill='#DCDCDC')

        for y in range(0, self.screenSize, self.pixelSize):  # vertical lines
            self.screen.create_line(0, y, self.screenSize, y, fill='#DCDCDC')

        self.screen.create_line(0, aux - self.pixelSize, self.screenSize, aux - self.pixelSize, fill="#f00")  # line central - horizontal
        self.screen.create_line(aux, 0, aux, self.screenSize, fill="#f00")  # line central - vertical

    def ConvertCoordinates(self, x, y):
        """
        Converts coordinates from matrix coordinates to screen coordinates.

        Args:
            x (int): The x-coordinate in matrix coordinates.
            y (int): The y-coordinate in matrix coordinates.

        Returns:
            tuple: The converted screen coordinates (x, y).
        """
        real_x = int((self.pixelSize * x) + (self.screenSize / 2))
        real_y = int((self.screenSize / 2) - (self.pixelSize * y))

        return real_x, real_y

    def ConvertMatrixCoordinates(self, x, y):
        """
        Converts coordinates from screen coordinates to matrix coordinates.

        Args:
            x (int): The x-coordinate in screen coordinates.
            y (int): The y-coordinate in screen coordinates.

        Returns:
            tuple: The converted matrix coordinates (line, column).
        """
        column = int(x + (self.matrixSize / 2))
        line = int((self.matrixSize / 2) - y) - 1

        return line, column

    def DrawPixel(self, x, y, color):
        """
        Draws a pixel on the screen at the specified coordinates.

        Args:
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.
            color (str): The color of the pixel.
        """
        x1, y1 = self.ConvertCoordinates(x, y)
        self.screen.create_rectangle(x1, y1, x1 + self.pixelSize, y1 - self.pixelSize, fill=color)

        l, c = self.ConvertMatrixCoordinates(x, y)
        self.Matrix[l][c] = color

    def Draw(self, object: list, color):
        """
        Draws an object on the screen.

        Args:
            object (list): A list of points representing the object.
            color (str): The color of the object.
        """
        for p in object:
            self.DrawPixel(p[0], p[1], color)

    def printMatrix(self):
        """
        Prints the matrix representation of the screen.
        """
        for line in self.Matrix:
            print(line)

    def checkMatrix(self, x, y):
        """
        Retrieves the color value from the matrix at the specified coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            str: The color value from the matrix.
        """
        l, c = self.ConvertMatrixCoordinates(x, y)
        return self.Matrix[l][c]

    def outlineWindow(self, xmin, xmax, ymin, ymax):
        """
        Outlines a window on the screen.

        Args:
            xmin (int): The minimum x-coordinate of the window.
            xmax (int): The maximum x-coordinate of the window.
            ymin (int): The minimum y-coordinate of the window.
            ymax (int): The maximum y-coordinate of the window.
        """
        xmin, ymin = self.ConvertCoordinates(xmin, ymin)
        xmax, ymax = self.ConvertCoordinates(xmax+1, ymax+1)
        self.screen.create_rectangle(xmin, ymin, xmax, ymax, outline='green')
