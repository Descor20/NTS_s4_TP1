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
    l = []
    for i in range (number_rooms):
        x = rng.randInt(sizemin, sizemax)
        y = rng.randInt(sizemin, sizemax)
        cornx = rng.randInt(0, dimension_x - x)
        corny = rng.randInt(0, dimension_y - y)
        #print(" -x " + str(x) + "\n -y " + str(y) + "\n -dx " + str(cornx) + "\n -dy " + str(corny))
        l.append(Room(x, y, cornx, corny))
    return l



def collision_detection(room_a, room_b):
    """
    room_a: Room
    room_b: Room
    return: boolean
    """
    a = room_a
    b = room_b
    ncollision = True
    print(" -min(size_x) " + str(min(a.corner_x, b.corner_x)) + "\n -max(x)" + str(max(a.corner_x, b.corner_x)))
    if (min(a.corner_x + a.size_x, b.corner_x + b.size_x) >= max(a.corner_x, b.corner_x)) and (min(a.corner_y + a.size_y, b.corner_y + b.size_y) >= max(a.corner_y, b.corner_y)) :
        ncollision = False
    return not ncollision
    

def best_move(room_a, room_b):
    """
    room_a: Room
    room_b: Room that overlaps with room_a
    Moves one of both rooms according to the rules in the subject 
    return : 0 if room_a has been moved, 1 else
    """
    a = room_a
    b = room_b
    can = False
    d_r = 0
    a_b = 0
    cost = 0
    tmp = 0
    while (a.corner_x + cost < b.corner_x + b.size_x) :
        cost += 1
    while (a.corner_y + tmp < b.corner_y + b.size_y) :
        tmp += 1
    if (tmp < cost and tmp > 0) :
        cost = tmp
        d_r = 1
    tmp = 0
    while (b.corner_x + tmp < a.corner_x + a.size_x) :
        tmp += 1
    if (tmp < cost and tmp > 0) :
        cost = tmp
        d_r = 0
        a_b = 1
    tmp = 0
    while (b.corner_y + tmp < a.corner_y + a.size_y) :
        tmp += 1
    if (tmp < cost and tmp > 0) :
        cost = tmp
        d_r = 1
        a_b = 1
    ##print(" -a_b " + str(a_b) + "\n -d_r " + str(d_r) + "\n -cost " + str(cost))
    
    if (a_b == 0) :
        if (d_r == 0) :
            room_a.corner_x += cost
        else :
            room_a.corner_y += cost
    else :
        if (d_r == 0) :
            room_b.corner_x += cost
        else :
            room_b.corner_y += cost
    
    return a_b
    



def separation_steering_behavior(list_rooms):
    """
    list_rooms: list of Rooms
    moves rooms until none overlap, does not return anything
    """
    
    while
