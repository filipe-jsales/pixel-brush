from src.rasterization import Rasterization


class Bresenham(Rasterization):

    """
    @Author: Filipe Eduardo Junqueira Sales
    @Author: JD
    @Github: https://github.com/filipe-jsales
    @Date: 2022-04-01
    @Version: 0.0.1
    @LinkedIn: https://www.linkedin.com/in/filipe-sales/

    An implementation of the Bresenham's line algorithm, which is used to draw a line between two points on a 2D grid.

    Args:
        start_point (tuple): The starting point of the line, given as a tuple of (x, y) coordinates.
        end_point (tuple): The ending point of the line, given as a tuple of (x, y) coordinates.

    Attributes:
        x_start (int): The x-coordinate of the starting point.
        y_start (int): The y-coordinate of the starting point.
        x_end (int): The x-coordinate of the ending point.
        y_end (int): The y-coordinate of the ending point.
        points (list): A list of all the points on the line (including the start and end points).
        x_axis_changed (bool): True if the line was reflected about the x-axis, False otherwise.
        y_axis_changed (bool): True if the line was reflected about the y-axis, False otherwise.
        xy_axes_changed (bool): True if the line was reflected about both the x-axis and y-axis, False otherwise.
        output_points (list): The list of all the points on the line (same as `points`).
    """

    def __init__(self, start_point, end_point):
        super().__init__([start_point, end_point])

        self.x_start = start_point[0]
        self.y_start = start_point[1]

        self.x_end = end_point[0]
        self.y_end = end_point[1]

        self.points = []

        self.x_axis_changed = False
        self.y_axis_changed = False
        self.xy_axes_changed = False

        if start_point == end_point:
            self.output_points = [[self.x_start, self.y_start]]
            return

        self.check_octant()

        x = self.x_start
        y = self.y_start

        delta_x = self.x_end - self.x_start
        delta_y = self.y_end - self.y_start

        slope = delta_y / delta_x
        error = slope - (1/2)

        self.points.append([x, y])

        while x < self.x_end:
            if error >= 0:
                y += 1
                error -= 1
            x += 1
            error += slope
            self.points.append([x, y])

        self.reflection(self.points)

        self.output_points = self.points

    def check_octant(self):

        """
        Helper method to check which octant the line is in and apply any necessary transformations to the start and end points.
        """

        delta_x = self.x_end - self.x_start
        delta_y = self.y_end - self.y_start

        if delta_x != 0:
            slope = delta_y / delta_x
        else:
            slope = 2

        if slope > 1 or slope < -1:
            [self.x_start, self.y_start] = [self.y_start, self.x_start]
            [self.x_end, self.y_end] = [self.y_end, self.x_end]
            self.xy_axes_changed = True

        if self.x_start > self.x_end:
            self.x_start = -self.x_start
            self.x_end = -self.x_end
            self.x_axis_changed = True

        if self.y_start > self.y_end:
            self.y_start = -self.y_start
            self.y_end = -self.y_end
            self.y_axis_changed = True

    def reflection(self, pts: list):
        if self.y_axis_changed:
            for pt in self.points:
                pt[1] = -pt[1]

        if self.x_axis_changed:
            for pt in self.points:
                pt[0] = -pt[0]

        if self.xy_axes_changed:
            for pt in self.points:
                [pt[0], pt[1]] = [pt[1], pt[0]]
