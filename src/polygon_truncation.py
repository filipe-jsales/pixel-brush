from src.rasterization import Rasterization
from src.polyline import *

class PolygonTruncation(Rasterization):
    """
    @Author: Filipe Eduardo Junqueira Sales
    @Author: João Davi Costa Lima
    @Github: https://github.com/filipe-jsales
    @Date: 2023-05-24
    @Version: 0.0.1
    @LinkedIn: https://www.linkedin.com/in/filipe-sales/

    A class that performs polygon truncation using the Sutherland-Hodgman algorithm.

    This class inherits from the Rasterization class.

    Attributes:
        polygon_points (list): The vertices of the polygon as a list of points.
        xmin (int): The minimum x-coordinate of the clipping window.
        xmax (int): The maximum x-coordinate of the clipping window.
        ymin (int): The minimum y-coordinate of the clipping window.
        ymax (int): The maximum y-coordinate of the clipping window.

    Methods:
        __init__(self, polygon_points, xmin, xmax, ymin, ymax):
            Initializes a PolygonTruncation object.

        sutherland_hodgman_left(self, pts):
            Applies the Sutherland-Hodgman algorithm for the left edge of the clipping window.

        sutherland_hodgman_right(self, pts):
            Applies the Sutherland-Hodgman algorithm for the right edge of the clipping window.

        sutherland_hodgman_down(self, pts):
            Applies the Sutherland-Hodgman algorithm for the bottom edge of the clipping window.

        sutherland_hodgman_up(self, pts):
            Applies the Sutherland-Hodgman algorithm for the top edge of the clipping window.

    Example usage:
        # Create an instance of the PolygonTruncation class
        polygon_points = [(10, 20), (30, 40), (50, 60), (70, 80)]
        xmin = 0
        xmax = 100
        ymin = 0
        ymax = 100
        polygon_truncation = PolygonTruncation(polygon_points, xmin, xmax, ymin, ymax)

        # Get the output points after polygon truncation
        output_points = polygon_truncation.output_points
    """
    def __init__(self, polygon_points: list, xmin, xmax, ymin, ymax):
        super().__init__([polygon_points, xmin, xmax, ymin, ymax])
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        left = self.sutherland_hodgman_left(polygon_points)
        up = self.sutherland_hodgman_up(left)
        right = self.sutherland_hodgman_right(up)
        down = self.sutherland_hodgman_down(right)

        new_polygon_vertices = down

        polygon = Polyline(new_polygon_vertices, close=True)
        self.output_points = polygon.output_points

    def sutherland_hodgman_left(self, pts):
        """
        Applies the Sutherland-Hodgman algorithm for the left edge of the clipping window.

        Args:
            pts (list): The vertices of the polygon as a list of points.

        Returns:
            list: The vertices after applying the Sutherland-Hodgman algorithm for the left edge.
        """
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if x1 >= self.xmin:
                if x2 >= self.xmin:
                    # inside to inside
                    new_polygon.append(list(p2))
                else:
                    # inside to outside
                    new_polygon.append(
                        [self.xmin, round(y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1))])

            else:
                if x2 >= self.xmin:
                    # outside to inside
                    new_polygon.append(
                        [self.xmin, round(y1 + (y2 - y1) * (self.xmin - x1) / (x2 - x1))])
                    new_polygon.append(p2)
        return new_polygon

    def sutherland_hodgman_right(self, pts):
        """
        Applies the Sutherland-Hodgman algorithm for the right edge of the clipping window.

        Args:
            pts (list): The vertices of the polygon as a list of points.

        Returns:
            list: The vertices after applying the Sutherland-Hodgman algorithm for the right edge.
        """
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if x1 <= self.xmax:
                if x2 <= self.xmax:
                    # inside to inside
                    new_polygon.append(list(p2))
                else:
                    # inside to outside
                    new_polygon.append(
                        [self.xmax, round(y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1))])

            else:
                if x2 <= self.xmax:
                    # outside to inside
                    new_polygon.append(
                        [self.xmax, round(y1 + (y2 - y1) * (self.xmax - x1) / (x2 - x1))])
                    new_polygon.append(p2)

        return new_polygon

    def sutherland_hodgman_down(self, pts):
        """
        Applies the Sutherland-Hodgman algorithm for the bottom edge of the clipping window.

        Args:
            pts (list): The vertices of the polygon as a list of points.

        Returns:
            list: The vertices after applying the Sutherland-Hodgman algorithm for the bottom edge.
        """
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if y1 >= self.ymin:
                if y2 >= self.ymin:
                    # inside to inside
                    new_polygon.append(list(p2))
                else:
                    # inside to outside
                    new_polygon.append(
                        [round(x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1)), self.ymin])

            else:
                if y2 >= self.ymin:
                    # outside to inside
                    new_polygon.append(
                        [round(x1 + (x2 - x1) * (self.ymin - y1) / (y2 - y1)), self.ymin])
                    new_polygon.append(p2)

        return new_polygon

    def sutherland_hodgman_up(self, pts):
        """
        Applies the Sutherland-Hodgman algorithm for the top edge of the clipping window.

        Args:
            pts (list): The vertices of the polygon as a list of points.

        Returns:
            list: The vertices after applying the Sutherland-Hodgman algorithm for the top edge.
        """
        new_polygon = []

        for i in range(len(pts)):
            p1 = pts[i]
            p2 = pts[(i+1) % len(pts)]

            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            if y1 <= self.ymax:
                if y2 <= self.ymax:
                    # inside to inside
                    new_polygon.append(list(p2))
                else:
                    # inside to outside
                    new_polygon.append(
                        [round(x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1)), self.ymax])

            else:
                if y2 <= self.ymax:
                    # outside to inside
                    new_polygon.append(
                        [round(x1 + (x2 - x1) * (self.ymax - y1) / (y2 - y1)), self.ymax])
                    new_polygon.append(p2)

        return new_polygon
