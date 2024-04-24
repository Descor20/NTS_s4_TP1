import pytest
from src.p2_corridors import filter_rooms
from src.room import Room



def test_fr1():
    r1 = Room(12, 6, 1, 4)
    r2 = Room(4, 4, 14, 1)
    r3 = Room(5, 4, 9, 9)
    lr = [r1, r2, r3]
    lc = [Room(1, 7, 3, 3), Room(1, 7, 14, 4)]
    l = filter_rooms(lr, lc)
    assert l == [r1, r2] or l == [r2, r1]

    
"""   
def test_fr2():
    r1 = Room(12, 6, 1, 4)
    r2 = Room(3, 3, 7, 1)
    r3 = Room(10, 9, 7, 1)
    l = choose_main_rooms([r1, r2, r3], 5, 8)
    assert len(l) == 1
    assert l[0].size_x == 10
    assert l[0].size_y == 9
    assert l[0].corner_x == 7
    assert l[0].corner_y == 1
"""    
    

 
