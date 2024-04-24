import pytest
from src.p2_corridors import choose_main_rooms
from src.room import Room



def test_cmr1():
    r1 = Room(12, 6, 1, 4)
    r2 = Room(3, 3, 7, 1)
    r3 = Room(9, 9, 7, 1)
    l = choose_main_rooms([r1, r2, r3], 8, 5)
    assert len(l) == 2

    
    
def test_cmr2():
    r1 = Room(12, 6, 1, 4)
    r2 = Room(3, 3, 7, 1)
    r3 = Room(10, 9, 7, 1)
    l = choose_main_rooms([r1, r2, r3], 5, 8)
    assert len(l) == 1
    assert l[0].size_x == 10
    assert l[0].size_y == 9
    assert l[0].corner_x == 7
    assert l[0].corner_y == 1
    
    

 
