from src.rasterization import Rasterization
from src.bresenham import Bresenham

'''
para construir uma curva são calculados points (que fazem parte da curva)
a partir dos pts de controle. Em seguida, os points calculados são
conectados com o algoritmo de Bresenham.

a variavel n define quantos points serão calculados
'''


class Curves(Rasterization):
    def __init__(self, n, control_pts: list):
        super().__init__([control_pts])

        self.points = []
        increment = 1 / n
        t = 0.0

        for d in range(n+1):
            self.points.append(self.casteljau(t, control_pts))
            t += increment

        self.join_points()

    def casteljau(self, t, control_points):
        pts = []
        for p in control_points:
            pts.append(list(p))

        for i in range(1, len(pts)):
            for j in range(len(pts)-i):
                pts[j][0] = (1 - t) * pts[j][0] + t * pts[j+1][0]
                pts[j][1] = (1 - t) * pts[j][1] + t * pts[j + 1][1]

        return [int(pts[0][0]), int(pts[0][1])]

    def join_points(self):
        for x in range(len(self.points) - 1):
            line = Bresenham(self.points[x], self.points[x + 1])

            for pt in line.output_points:
                self.output_points.append(pt)
