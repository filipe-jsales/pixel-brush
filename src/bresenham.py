from src.rasterization import Rasterization


class Bresenham(Rasterization):
    def __init__(self, point1, point2):
        super().__init__([point1, point2])

        self.x1 = point1[0]
        self.y1 = point1[1]

        self.x2 = point2[0]
        self.y2 = point2[1]

        self.points = []

        self.change_x = False
        self.change_y = False
        self.change_xy = False

        if point1 == point2:
            self.output_points = [[self.x1, self.y1]]
            return

        self.check_octant()

        x = self.x1
        y = self.y1

        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1

        m = delta_y/delta_x
        e = m - (1/2)

        self.points.append([x, y])

        while x < self.x2:
            if e >= 0:
                y += 1
                e -= 1
            x += 1
            e += m
            self.points.append([x, y])

        self.reflection(self.points)

        self.output_points = self.points

    def check_octant(self):

        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1

        if delta_x != 0:
            m = delta_y/delta_x
        else:
            m = 2

        if m > 1 or m < -1:
            [self.x1, self.y1] = [self.y1, self.x1]
            [self.x2, self.y2] = [self.y2, self.x2]
            self.change_xy = True

        if self.x1 > self.x2:
            self.x1 = -self.x1
            self.x2 = -self.x2
            self.change_x = True

        if self.y1 > self.y2:
            self.y1 = -self.y1
            self.y2 = -self.y2
            self.change_y = True

    def reflection(self, pts: list):
        if self.change_y:
            for pt in self.points:
                pt[1] = -pt[1]

        if self.change_x:
            for pt in self.points:
                pt[0] = -pt[0]

        if self.change_xy:
            for pt in self.points:
                [pt[0], pt[1]] = [pt[1], pt[0]]
