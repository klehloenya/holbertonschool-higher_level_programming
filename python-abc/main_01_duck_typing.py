#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

# Create instances of Circle and Rectangle
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

# Pass the objects to shape_info function
shape_info(circle)
shape_info(rectangle)
