from rng import *
from delaunay import *
from room import Room

SEED  = 6729
rng = PseudoRNG(46613,17,SEED)

        


def generate_rooms(number_rooms, sizemin, sizemax, dimension_x, dimension_y):
    """
    number_rooms : int
    sizemin : int
    sizemax : int
    dimension_x : int
    dimension_y : int
    return : a list of rooms with edges of size between sizemin and sizemax,
        such that all corners of each room has coordinates between 
        [0, dimension_x] and [0, dimension_y]
    """
    # Dummy list, to be able to display
    return [Room(1,2,3,4), Room(5,6,7,8), Room(9,10,11,12), Room(4,5,6,7) ]



def collision_detection(room_a, room_b):
    """
    room_a: Room
    room_b: Room
    return: boolean
    """
    return False 
    

def best_move(room_a, room_b):
    """
    room_a: Room
    room_b: Room that overlaps with room_a
    Moves one of both rooms according to the rules in the subject 
    return : 0 if room_a has been moved, 1 else
    """
    return 0



def separation_steering_behavior(list_rooms):
    """
    list_rooms: list of Rooms
    moves rooms until none overlap, does not return anything
    """
    return None

