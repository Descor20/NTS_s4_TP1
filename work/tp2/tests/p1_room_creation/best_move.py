import pytest
from src.p1_room_creation import best_move
from src.room import Room



def test_bm1():
    # best move is to move room r1 5 units top
    r1 = Room(11, 3, 1, 4)
    r2 = Room(4, 8, 7, 1)
    s = best_move(r1, r2) 
    assert r1.corner_x == 1
    assert r1.corner_y == 9
    assert s == 0

    
    
def test_bm2():
    # best move is to move room r2 7 units top
    r1 = Room(20, 10, 5, 15)
    r2 = Room(11, 6, 7, 18)
    s = best_move(r1, r2) 
    assert r2.corner_x == 7
    assert r2.corner_y == 25
    assert s == 1
    
    

 
