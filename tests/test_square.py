import pytest
import source.shapes as shapes

@pytest.mark.parametrize("side_lenght, expected_area, random", [(5,25,6),(4,16,7),(8,64,8)])
def mul_square_areas(side_lenght, expected_area, random):
    assert shapes.Square(side_lenght).area() == expected_area
