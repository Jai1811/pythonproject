from dbm import error

import pytest
import time
import source.my_functions as my_functions


def test_add():
    assert my_functions.add(1, 2) == 3

def test_add_string():
    assert my_functions.add("a", "b") == "ab"

def test_divide():
    with pytest.raises(ValueError):
         my_functions.divide(1, 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10, 2)
    assert result == 5.0

@pytest.mark.skip(reason="broken")
def test_add_skip():
    time.sleep(5)
    result = my_functions.add(10, 2)
    assert result == 14

@pytest.mark.xfail(reason="broken")
def test_add_xfail():
    time.sleep(5)
    result = my_functions.add(10, 2)
    assert result == 0



