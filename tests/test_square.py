from pytest import approx

from example_install.calculator_functions import square_value

def test_square():

    assert square_value(2) == approx(4)

