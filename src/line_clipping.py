from src.rasterization import Rasterization
from src.bresenham import *


class LineClipping(Rasterization):
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
        x = point[0]
        y = point[1]

        bit1 = self.sign(self.ymax - y)
        bit2 = self.sign(y - self.ymin)
        bit3 = self.sign(self.xmax - x)
        bit4 = self.sign(x - self.xmin)

        return int(str(bit1) + str(bit2) + str(bit3) + str(bit4), 2)

    def sign(self, num):
        if num < 0:
            return 1
        else:
            return 0
