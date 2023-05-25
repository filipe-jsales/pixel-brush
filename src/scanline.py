from src.rasterization import Rasterization
import sys


class CriticalPoint:
    """
    A class representing a critical point used in the Scanline algorithm.

    The CriticalPoint class stores information about a critical point, including its index, direction, x-coordinate
    of intersection, and inverse slope.

    Attributes:
        index (int): The index of the critical point.
        dir (int): The direction of the critical point.
        x_intersection (float): The x-coordinate of the intersection.
        inv_slope (float): The inverse slope of the critical point.
    """

    def __init__(self, index, dir, x_intersection, inv_slope):
        """
        Initializes a CriticalPoint object with the given parameters.

        Args:
            index (int): The index of the critical point.
            dir (int): The direction of the critical point.
            x_intersection (float): The x-coordinate of the intersection.
            inv_slope (float): The inverse slope of the critical point.
        """
        self.index = index
        self.dir = dir
        self.x_intersection = x_intersection
        self.inv_slope = inv_slope

    def __lt__(self, outro):
        """
        Compares two CriticalPoint objects based on their x_intersection values.

        Args:
            outro (CriticalPoint): The other CriticalPoint object to compare.

        Returns:
            bool: True if the x_intersection of this point is less than the x_intersection of the other point, False otherwise.
        """
        return self.x_intersection < outro.x_intersection


class Scanline(Rasterization):
    """
    A class representing the Scanline algorithm for polygon filling.

    The Scanline class extends the Rasterization class and provides an implementation of the Scanline algorithm for filling
    polygons. It fills the polygon by scanning each horizontal line within its bounding box and determining the intersections
    with the polygon edges.

    Attributes:
        polygon (list): The list of vertices representing the polygon to be filled.
    """

    def __init__(self, polygon):
        """
        Initializes a Scanline object with the given polygon.

        Args:
            polygon (list): The list of vertices representing the polygon to be filled.
        """
        super().__init__(polygon)

        ymax = -sys.maxsize
        ymin = sys.maxsize

        critical_points = []

        for i in range(len(polygon)):
            if polygon[i][1] < ymin:
                ymin = polygon[i][1]
            if polygon[i][1] > ymax:
                ymax = polygon[i][1]

            auxiliar_point = polygon[(i + 1) % len(polygon)]

            if polygon[i][1] < auxiliar_point[1]:
                c = CriticalPoint(i, dir=1, x_intersection=polygon[i][0],
                                  inv_slope=(auxiliar_point[0] - polygon[i][0]) / (auxiliar_point[1] - polygon[i][1]))
                critical_points.append(c)

            auxiliar_point = polygon[(i - 1)]

            if polygon[i][1] < auxiliar_point[1]:
                c = CriticalPoint(i, dir=-1, x_intersection=polygon[i][0],
                                  inv_slope=(auxiliar_point[0] - polygon[i][0]) / (auxiliar_point[1] - polygon[i][1]))
                critical_points.append(c)

        actives = []

        for y in range(ymin, ymax + 1):
            for point in actives:
                point.x_intersection += point.inv_slope

            for pt in critical_points:
                if polygon[pt.index][1] == y:
                    actives.append(pt)

            for i in range(len(actives) - 1, -1, -1):
                c = actives[i]
                p_max = polygon[(c.index + c.dir + len(polygon)) % len(polygon)]
                if p_max[1] == y:
                    actives.pop(i)

            actives.sort()

            for i in range(0, len(actives), 2):
                xmin = round(actives[i].x_intersection)
                xmax = round(actives[i + 1].x_intersection)
                for x in range(xmin, xmax):
                    self.output_points.append([x, y])
    """
    The Scanline algorithm for polygon filling.

    The Scanline algorithm fills a polygon by scanning each horizontal line within its bounding box. It determines the
    intersections between the scanline and the polygon edges and adds the resulting points to the output_points list.
    """
