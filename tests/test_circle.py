import math

import pytest
import source.shapes as shapes

class TestCircle:

    def setup_method(self,method):
        print(f"setting up for method: {method}")
        self.circle = shapes.Circle(10)
        pass

    def test_one(self):
        assert True

    def test_two(self):
        assert True

    def   test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius

    def teardown_method(self, method):
        print(f"teardown_method for method:{method}")
        del self.circle
        pass