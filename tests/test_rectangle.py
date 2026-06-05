import pytest
import source.shapes as shapes

def test_area(my_rectangle):
    assert my_rectangle.area() == 200
def test_parameter(my_rectangle):
    assert my_rectangle.perimeter() == 400

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle
