from src.rasterization import Rasterization
from src.bresenham import Bresenham


class Polyline(Rasterization):
    """
    A class representing a Polyline, which is a series of connected line segments.

    This class inherits from the Rasterization class and provides methods to generate the set of points that approximate
    the Polyline using the Bresenham's line algorithm.

    Attributes:
        points (list): The list of points defining the Polyline.
        close (bool): Indicates whether the Polyline is closed (forms a closed shape) or open (ends without connecting
            back to the starting point).
    """

    def __init__(self, points: list, close=False):
        """
        Initializes a Polyline object with the given points.

        Args:
            points (list): The list of points defining the Polyline.
            close (bool, optional): Indicates whether the Polyline is closed. Defaults to False.
        """
        super().__init__(points)

        if close:
            points.append(points[0])

        for x in range(len(points)-1):
            line = Bresenham(points[x], points[x+1])

            for pt in line.output_points:
                self.output_points.append(pt)
