from src.rasterization import Rasterization

class Circle(Rasterization):
    """
    @Author: Filipe Eduardo Junqueira Sales
    @Author: João Davi Costa Lima
    @Github: https://github.com/filipe-jsales
    @Date: 2023-05-24
    @Version: 0.0.1
    @LinkedIn: https://www.linkedin.com/in/filipe-sales/
    A class that represents a circle and performs rasterization to draw the circle.

    This class inherits from the Rasterization class.

    Attributes:
        input_points (dict): A dictionary containing the input points for the circle.
            It should have the following keys:
                - "center": The center point of the circle as a tuple (x, y).
                - "radius": The radius of the circle.

        center (tuple): The center point of the circle as a tuple (x, y).
        radius (int): The radius of the circle.
        output_points (list): A list to store the output points after rasterization.

    Methods:
        __init__(self, input_points):
            Initializes a Circle object.

        middle_point(self):
            Performs the midpoint algorithm to rasterize the circle.

        e_prox(self, x, y, e):
            Calculates the updated error value for the next point in the rasterization algorithm.

        e_fin(self, x, y, e):
            Calculates the updated error value when the current point is inside the circle.

        draw_octants(self, x, y):
            Draws the points in all eight octants of the circle.

    Example usage:
        # Create an instance of the Circle class
        input_points = {"center": (0, 0), "radius": 5}
        circle = Circle(input_points)

        # Perform the rasterization
        circle.middle_point()

        # Get the output points
        output_points = circle.output_points
    """
    def __init__(self, input_points):
        super().__init__(input_points)

        self.center = self.input_points["center"]
        self.radius = round(self.input_points["radius"])

        self.middle_point()

    def middle_point(self):
        # initial parameters and first traces in octant
        x = 0
        y = self.radius
        e = -self.radius
        self.draw_octants(x, y)

        # draw in the second octant to others octants
        while x <= y:
            # adjust the x error and increment to the right
            e = self.e_prox(x, y, e)
            x += 1

            # if it is inside the circle, decrement y, else keep y
            if e >= 0:
                e = self.e_fin(x, y, e)
                y -= 1

            self.draw_octants(x, y)

    def e_prox(self, x, y, e):
        """
        Calculates the updated error value for the next point in the rasterization algorithm.

        Args:
            x (int): The x-coordinate of the current point.
            y (int): The y-coordinate of the current point.
            e (int): The current error value.

        Returns:
            int: The updated error value.
        """
        return e + 2*x + 1

    def e_fin(self, x, y, e):
        """
        Calculates the updated error value when the current point is inside the circle.

        Args:
            x (int): The x-coordinate of the current point.
            y (int): The y-coordinate of the current point.
            e (int): The current error value.

        Returns:
            int: The updated error value.
        """
        return e - 2*y + 2

    def draw_octants(self, x, y):
        """
        Draws the points in all eight octants of the circle.

        Args:
            x (int): The x-coordinate of the current point.
            y (int): The y-coordinate of the current point.
        """
        self.output_points.append([x + self.center[0], y + self.center[1]])
        self.output_points.append([y + self.center[0], x + self.center[1]])
        self.output_points.append([y + self.center[0], -x + self.center[1]])
        self.output_points.append([x + self.center[0], -y + self.center[1]])
        self.output_points.append([-x + self.center[0], -y + self.center[1]])
        self.output_points.append([-y + self.center[0], -x + self.center[1]])
        self.output_points.append([-y + self.center[0], x + self.center[1]])
        self.output_points.append([-x + self.center[0], y + self.center[1]])
