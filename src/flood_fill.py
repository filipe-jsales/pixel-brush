from src.rasterization import Rasterization
from src.screen import Screen

class FloodFill(Rasterization):
    """
    A class representing a Recursive Filling algorithm for filling an area with a color.

    The FloodFill class extends the Rasterization class and provides a recursive algorithm for filling an area
    with a specified color. It utilizes the Screen class for drawing and checking pixels.

    Attributes:
        point (tuple): The starting point for the filling operation.
        color (str): The color to fill the area with.
        edge_color (str): The color of the area's edge.
        screen (Screen): The screen object to perform the filling operation on.
    """

    def __init__(self, point, color, edge_color, screen: Screen):
        """
        Initializes a FloodFill object with the given parameters.

        Args:
            point (tuple): The starting point for the filling operation.
            color (str): The color to fill the area with.
            edge_color (str): The color of the area's edge.
            screen (Screen): The screen object to perform the filling operation on.
        """
        super().__init__([point, color, screen])
        self.screen = screen
        self.color = color
        self.edge_color = edge_color
        self.recursion(point)

    def recursion(self, point):
        """
        Recursively fills the area with the specified color.

        The recursion method fills the area with the specified color using a recursive algorithm. It starts from the
        given point and recursively fills adjacent pixels with the color until the area is completely filled.

        Args:
            point (tuple): The current point to process.
        """
        x, y = point
        current_color = self.screen.checkMatrix(x, y)

        if current_color != self.color and current_color != self.edge_color:
            self.screen.DrawPixel(x, y, self.color)

            neighbors = [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1)
            ]

            for neighbor in neighbors:
                self.recursion(neighbor)
