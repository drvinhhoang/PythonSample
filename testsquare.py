
from square import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def text_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("dog")