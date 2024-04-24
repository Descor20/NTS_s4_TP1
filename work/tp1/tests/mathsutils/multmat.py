import pytest
from src.mathsutils import multmat


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon
    
def approx_v(X, Y, epsilon):
    return all(approx(X[i], Y[i], epsilon) for i in range(len(X)))
    
def approx_m(X, Y, epsilon):
    return all(approx_v(X[i], Y[i], epsilon) for i in range(len(X)))
        


def test_mm1():
    R = multmat([[0, 2], [1, 0]], [[2], [3]])
    assert R == [[6], [2]]
    
def test_mm2():
    R = multmat([[0, 2, 4], [1, 0, 5]], [[2, 1], [0, 3], [2, 1]])
    assert R == [[8, 10], [12, 6]]
    
def test_mm3():
    R = multmat([[0.3, -2.1, 4], [1, 0, -5.4]], [[-2.1, 3.5, 1]])
    assert len(R) == 2 and len(R[0]) == 3
    assert approx_m(R, [[-0.63, 1.05, 0.3], [-2.1, 3.5, 1]], 0.0001)
    
 
