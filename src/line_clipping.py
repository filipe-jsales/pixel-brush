from src.rasterization import Rasterization
from src.bresenham import *

class LineClipping(Rasterization):
    """
    A class that performs line clipping using the Cohen-Sutherland algorithm.

    This class inherits from the Rasterization class.

    Attributes:
        p1 (tuple): The starting point of the line as a tuple (x1, y1).
        p2 (tuple): The ending point of the line as a tuple (x2, y2).
        xmin (int): The minimum x-coordinate of the clipping window.
        xmax (int): The maximum x-coordinate of the clipping window.
        ymin (int): The minimum y-coordinate of the clipping window.
        ymax (int): The maximum y-coordinate of the clipping window.

        up (int): Binary code representing the "up" region in the clipping window.
        down (int): Binary code representing the "down" region in the clipping window.
        right (int): Binary code representing the "right" region in the clipping window.
        left (int): Binary code representing the "left" region in the clipping window.

    Methods:
        __init__(self, p1, p2, xmin, xmax, ymin, ymax):
            Initializes a LineClipping object.

        cohem_sutherland(self, p1, p2):
            Performs the Cohen-Sutherland line clipping algorithm.

        binary(self, point):
            Converts a point into a binary code based on its position relative to the clipping window.

        sign(self, num):
            Determines the sign (positive or negative) of a number.

    Example usage:
        # Create an instance of the LineClipping class
        p1 = (10, 20)
        p2 = (50, 60)
        xmin = 0
        xmax = 100
        ymin = 0
        ymax = 100
        line_clipping = LineClipping(p1, p2, xmin, xmax, ymin, ymax)

        # Get the output points after line clipping
        output_points = line_clipping.output_points
    """
    def __init__(self, p1, p2, xmin, xmax, ymin, ymax):
        super().__init__([p1, p2])
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        self.up = int('1000', 2)
        self.down = int('0100', 2)
        self.right = int('0010', 2)
        self.left = int('0001', 2)

        self.cohem_sutherland(list(p1), list(p2))

    def cohem_sutherland(self, p1, p2):
        """
        Performs the Cohen-Sutherland line clipping algorithm.

        Args:
            p1 (list): The starting point of the line as a list [x1, y1].
            p2 (list): The ending point of the line as a list [x2, y2].
        """
        c1 = self.binary(p1)
        c2 = self.binary(p2)

        while True:
            if c1 | c2 == 0:

                line = Bresenham(p1, p2)
                self.output_points = line.output_points
                break
            elif c1 & c2 != 0:
                break
            else:

                if c1 != 0:
                    out = c1
                else:
                    out = c2

                x1, y1 = p1[0], p1[1]
                x2, y2 = p2[0], p2[1]

                if out & self.up:

                    x = round(x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1))
                    y = self.ymax

                elif out & self.down:

                    x = round(x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1))
                    y = self.ymin

                elif out & self.right:

                    y = round(y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1))
                    x = self.xmax

                elif out & self.left:

                    y = round(y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1))
                    x = self.xmin

                if out == c1:
                    p1[0] = x
                    p1[1] = y
                    c1 = self.binary(p1)

                else:
                    p2[0] = x
                    p2[1] = y
                    c2 = self.binary(p2)

    def binary(self, point):
        """
        Converts a point into a binary code based on its position relative to the clipping window.

        Args:
            point (list): The point as a list [x, y].

        Returns:
            int: The binary code representing the position of the point.
        """
        x = point[0]
        y = point[1]

        bit1 = self.sign(self.ymax - y)
        bit2 = self.sign(y - self.ymin)
        bit3 = self.sign(self.xmax - x)
        bit4 = self.sign(x - self.xmin)

        return int(str(bit1) + str(bit2) + str(bit3) + str(bit4), 2)

    def sign(self, num):
        """
        Determines the sign (positive or negative) of a number.

        Args:
            num (float): The number to determine the sign of.

        Returns:
            int: 1 if the number is negative, 0 otherwise.
        """
        if num < 0:
            return 1
        else:
            return 0
