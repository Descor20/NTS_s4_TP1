import pytest
from src.mathsutils import multmatvector


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon
    
def approx_v(X, Y, epsilon):
    return all(approx(X[i], Y[i], epsilon) for i in range(len(X)))
        


def test_mmv1():
    R = multmatvector([[0, 2], [1, 0]], [2, 3])
    assert R == [6, 2]
    
def test_mmv2():
    R = multmatvector([[0, 2, 4], [1, 0, 5]], [2, 3, 1])
    assert R == [10, 7]
    
def test_mmv3():
    R = multmatvector([[0.3, -2.1, 4], [1, 0, -5.4]], [-2.1, 3.5, 1])
    assert len(R) == 2
    assert approx_v(R, [-3.98, -7.5], 0.0001)
    
 
