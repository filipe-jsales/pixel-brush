from src.rasterization import Rasterization
import sys


class CriticalPoint:
    def __init__(self, index, dir, x_intersection, inv_slope):
        self.index = index
        self.dir = dir
        self.x_intersection = x_intersection
        self.inv_slope = inv_slope

    def __lt__(self, outro):
        return self.x_intersection < outro.x_intersection


class Scanline(Rasterization):
    def __init__(self, polygon):
        super().__init__(polygon)

        ymax = -sys.maxsize
        ymin = sys.maxsize

        critical_points = []

        for i in range(len(polygon)):
            if polygon[i][1] < ymin:
                ymin = polygon[i][1]
            if polygon[i][1] > ymax:
                ymax = polygon[i][1]

            auxiliar_point = polygon[(i+1)%len(polygon)]

            if polygon[i][1] < auxiliar_point[1]:
                c = CriticalPoint(i, dir=1, x_intersection=polygon[i][0],
                                 inv_slope=(auxiliar_point[0] - polygon[i][0])/(auxiliar_point[1] - polygon[i][1]))
                critical_points.append(c)

            auxiliar_point = polygon[(i-1)]

            if polygon[i][1] < auxiliar_point[1]:
                c = CriticalPoint(i, dir=-1, x_intersection=polygon[i][0],
                                 inv_slope=(auxiliar_point[0] - polygon[i][0]) / (auxiliar_point[1] - polygon[i][1]))
                critical_points.append(c)

        actives = []

        for y in range(ymin, ymax+1):
            for point in actives:
                point.x_intersection += point.inv_slope

            for pt in critical_points:
                if polygon[pt.index][1] == y:
                    actives.append(pt)

            for i in range(len(actives)-1, -1, -1):
                c = actives[i]
                p_max = polygon[(c.index + c.dir + len(polygon))%len(polygon)]
                if p_max[1] == y:
                    actives.pop(i)

            actives.sort()

            for i in range(0, len(actives), 2):
                xmin = round(actives[i].x_intersection)
                xmax = round(actives[i+1].x_intersection)
                for x in range(xmin, xmax):
                    self.output_points.append([x,y])


