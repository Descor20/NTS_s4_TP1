import pytest
from src.p1_room_creation import collision_detection
from src.room import Room



def test_cd1():
    r1 = Room(11, 3, 1, 4)
    r2 = Room(4, 8, 7, 1)
    assert collision_detection(r2, r1) 
    assert collision_detection(r1, r2)

def test_cd2():
    r1 = Room(4, 2, 2, 1)
    r2 = Room(11, 3, 1, 4)
    assert not collision_detection(r1, r2)
    assert not collision_detection(r2, r1)
    
def test_cd3():
    r1 = Room(20, 10, 5, 15)
    r2 = Room(10, 4, 7, 18)
    assert collision_detection(r1, r2)
    assert collision_detection(r2, r1)
    
    
    

 
