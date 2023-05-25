from src.rasterization import Rasterization
from src.polyline import Polyline
from math import sin, cos, radians
import numpy as np


class Transformation(Rasterization):
    """
    A class representing transformations applied to a set of points.

    The Transformation class extends the Rasterization class and provides methods for translating, scaling, and rotating
    a set of input points. The transformed points are stored in the output_points attribute.

    Attributes:
        input_points (list): The input points to be transformed.
        output_points (list): The transformed points.
    """

    def __init__(self, input_points):
        """
        Initializes a Transformation object with the given input points.

        Args:
            input_points (list): The input points to be transformed.
        """
        super().__init__(input_points)
        self.output_points = input_points

    def translate(self, trans_x, trans_y):
        """
        Translates the input points by the specified translation values.

        Args:
            trans_x (float): The translation value for the x-coordinate.
            trans_y (float): The translation value for the y-coordinate.
        """
        self.output_points = []
        for point in self.input_points:
            point[0] += trans_x
            point[1] += trans_y
            self.output_points.append(point)

    def scale(self, esc_x, esc_y):
        """
        Scales the input points by the specified scaling factors.

        Args:
            esc_x (float): The scaling factor for the x-coordinate.
            esc_y (float): The scaling factor for the y-coordinate.
        """
        self.output_points = []
        for point in self.input_points:
            point[0] *= esc_x
            point[1] *= esc_y
            self.output_points.append(point)
        self.output_points.append(self.output_points[0])

        self.output_points = Polyline(self.output_points).output_points

    def rotate(self, pivot, angulo):
        """
        Rotates the input points around the specified pivot point by the given angle.

        Args:
            pivot (list): The pivot point (x, y) for rotation.
            angulo (float): The rotation angle in degrees.
        """
        self.output_points = []
        trans_x = 0 - pivot[0]
        trans_y = 0 - pivot[1]
        translation = Transformation(self.input_points)
        translation.translate(trans_x, trans_y)
        self.input_points = translation.output_points

        radian_angle = radians(angulo)

        rotation_matrix = [
            [cos(radian_angle), -sin(radian_angle)], [sin(radian_angle), cos(radian_angle)]]

        for point in self.input_points:
            self.output_points.append([round(x)
                                      for x in np.dot(rotation_matrix, point)])

        translation = Transformation(self.output_points)
        translation.translate(-trans_x, -trans_y)
        self.output_points = translation.output_points
