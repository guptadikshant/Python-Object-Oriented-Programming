import math


class Circle:

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2)
    
