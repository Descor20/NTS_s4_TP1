import pytest
from src.mathsutils import degreetorad


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon


def test_dtr1():
    assert degreetorad(0) == 0
    
def test_dtr2():
    assert approx(degreetorad(90), 1.570796, 0.0001)
    
def test_dtr3():
    assert approx(degreetorad(180), 3.14159265, 0.0001)
    
def test_dtr4():
    assert approx(degreetorad(-45), -0.785398, 0.0001)
    
 
