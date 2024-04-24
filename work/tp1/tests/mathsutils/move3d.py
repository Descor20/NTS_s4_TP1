import pytest
from src.mathsutils import move3d


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon
    
def approx_v(X, Y, epsilon):
    return all(approx(X[i], Y[i], epsilon) for i in range(len(X)))
    


def test_move3d1():
    R = move3d(1, 1, 2, [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], 3)
    assert R == (1, 1, -1)


def test_move3d2():
    R = move3d(10, -5, 3, [[0.8910065, 0, 0.4539905], [0, 1, 0], [-0.4539905, 0, 0.8910065]], 5)
    assert len(R) == 3
    assert approx_v(R, (14.4550325, -5, 0.7300475), 0.0001)

def test_move3d3():
    R = move3d(10, 0, 7, [[0.8910065, -0.4539905, 0], [0.4539905, 0.8910065, 0], [0, 0, 1]], 0)
    assert R == (10, 0, 7)
 
