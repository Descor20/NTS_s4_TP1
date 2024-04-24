import pytest
from src.mathsutils import r2d


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon
    
def approx_v(X, Y, epsilon):
    return all(approx(X[i], Y[i], epsilon) for i in range(len(X)))
    
def approx_m(M1, M2, epsilon):
    return all(approx_v(M1[i], M2[i], epsilon) for i in range(len(M1)))
        


def test_r2d1():
    R = r2d(0)
    assert len(R) == 2 and len(R[0]) == 2
    assert approx_m(R, [[1, 0], [0, 1]], 0.0001)
    

def test_r2d2():
    R = r2d(90)
    assert len(R) == 2 and len(R[0]) == 2
    assert approx_m(R, [[0, -1], [1, 0]], 0.0001)

def test_r2d3():
    R = r2d(27)
    assert len(R) == 2 and len(R[0]) == 2
    assert approx_m(R, [[0.8910065, -0.4539905], [0.4539905, 0.8910065]], 0.0001)

 
