import pytest
from src.mathsutils import move2d


#because floats
def approx(x, y, epsilon):
    return abs(x - y) < epsilon
    
def approx_v(X, Y, epsilon):
    return all(approx(X[i], Y[i], epsilon) for i in range(len(X)))
    


def test_move2d1():
    R = move2d(1, 1, [[0, 1], [-1, 0]], 3)
    assert R == (1, -2)

def test_move2d2():
    R = move2d(10, 0, [[0.8910065, -0.4539905], [0.4539905, 0.8910065]], 5)
    assert len(R) == 2
    assert approx_v(R, (14.4550325, 2.2699525), 0.0001)

def test_move2d3():
    R = move2d(10, 0, [[0.8910065, -0.4539905], [0.4539905, 0.8910065]], 0)
    assert R == (10, 0)

 
