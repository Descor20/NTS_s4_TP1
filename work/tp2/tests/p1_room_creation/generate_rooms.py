import pytest
from src.p1_room_creation import generate_rooms



def test_gr1():
    l = generate_rooms(10, 5, 10, 15, 30)
    n = len(l)
    n == 10
    for i in range(n):
        r = l[i]
        assert 5 <= r.size_x <= 10
        assert 5 <= r.size_y <= 10 
        assert 0 <= r.corner_x
        assert r.corner_x + r.size_x < 15
        assert r.corner_y + r.size_y < 30
    assert all(l[i] != l[i+1] for i in range(n - 1))
    

 
