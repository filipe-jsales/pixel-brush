class Rasterization:
    """
    @Author: Filipe Eduardo Junqueira Sales
    @Author: João Davi Costa Lima
    @Github: https://github.com/filipe-jsales
    @Date: 2023-05-24
    @Version: 0.0.1
    @LinkedIn: https://www.linkedin.com/in/filipe-sales/
    
    A class representing a Rasterization, which converts input points into a rasterized representation.

    The Rasterization class provides a base class for performing rasterization operations on a set of input points.
    It defines the input points and output points attributes.

    Attributes:
        input_points (list): The list of points of the input figure.
        output_points (list): The list of points that compose the rasterization.
    """

    def __init__(self, input_points):
        """
        Initializes a Rasterization object with the given input points.

        Args:
            input_points (list): The list of points of the input figure.
        """
        self.input_points = input_points
        self.output_points = []
