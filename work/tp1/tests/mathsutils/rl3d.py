import pytest
from src.mathsutils import rl3d


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon
    
def approx_v(X, Y, epsilon):
    return all(approx(X[i], Y[i], epsilon) for i in range(len(X)))
    
def approx_m(M1, M2, epsilon):
    return all(approx_v(M1[i], M2[i], epsilon) for i in range(len(M1)))
        


def test_rl3d1():
    R = rl3d(0)
    assert len(R) == 3 and len(R[0]) == 3
    assert approx_m(R, [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 0.0001)
    

def test_rl3d2():
    R = rl3d(90)
    assert len(R) == 3 and len(R[0]) == 3
    assert approx_m(R, [[1, 0, 0], [0, 0, -1], [0, 1, 0]], 0.0001)

def test_rl3d3():
    R = rl3d(27)
    assert len(R) == 3 and len(R[0]) == 3
    assert approx_m(R, [[1, 0, 0], [0, 0.8910065, -0.4539905], [0, 0.4539905, 0.8910065]], 0.0001)

 
