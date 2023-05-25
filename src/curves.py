from src.rasterization import Rasterization
from src.bresenham import Bresenham

class Curves(Rasterization):
    """
    @Author: Filipe Eduardo Junqueira Sales
    @Author: JD
    @Github: https://github.com/filipe-jsales
    @Date: 2022-04-01
    @Version: 0.0.1
    @LinkedIn: https://www.linkedin.com/in/filipe-sales/
    
    A class that represents curves and performs rasterization using the Bresenham algorithm to draw the curves.

    This class inherits from the Rasterization class.

    Attributes:
        n (int): The number of points to interpolate on the curve.
        control_pts (list): A list of control points defining the curve.

        points (list): A list to store the interpolated points on the curve.
        output_points (list): A list to store the output points after rasterization.

    Methods:
        __init__(self, n, control_pts):
            Initializes a Curves object.

        casteljau(self, t, control_points):
            Performs the Casteljau's algorithm to interpolate a point on the curve at parameter t.

        join_points(self):
            Connects the interpolated points on the curve using the Bresenham algorithm.

    Example usage:
        # Create an instance of the Curves class
        control_points = [(0, 0), (2, 5), (5, 3)]
        curves = Curves(10, control_points)

        # Get the output points after rasterization
        output_points = curves.output_points
    """
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
        """
        Performs the Casteljau's algorithm to interpolate a point on the curve at parameter t.

        Args:
            t (float): The parameter value at which to interpolate the point on the curve.
            control_points (list): A list of control points defining the curve.

        Returns:
            list: The interpolated point on the curve as a list [x, y].
        """
        pts = []
        for p in control_points:
            pts.append(list(p))

        for i in range(1, len(pts)):
            for j in range(len(pts)-i):
                pts[j][0] = (1 - t) * pts[j][0] + t * pts[j+1][0]
                pts[j][1] = (1 - t) * pts[j][1] + t * pts[j + 1][1]

        return [int(pts[0][0]), int(pts[0][1])]

    def join_points(self):
        """
        Connects the interpolated points on the curve using the Bresenham algorithm.
        """
        for x in range(len(self.points) - 1):
            line = Bresenham(self.points[x], self.points[x + 1])

            for pt in line.output_points:
                self.output_points.append(pt)
