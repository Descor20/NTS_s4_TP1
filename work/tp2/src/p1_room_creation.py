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
    #print("\n\n -min(corner+s_x) " + str(min((a.corner_x + a.size_x), (b.corner_x + b.size_x))) + "\n -max(corner_x)" + str(max(a.corner_x, b.corner_x)))
    #print(" -min(corner+s_y) " + str(min((a.corner_y + a.size_y), (b.corner_y + b.size_y))) + "\n -max(corner_y)" + str(max(a.corner_y, b.corner_y)))
    if (min((a.corner_x + a.size_x), (b.corner_x + b.size_x)) > max(a.corner_x, b.corner_x)) and (min((a.corner_y + a.size_y), (b.corner_y + b.size_y)) > max(a.corner_y, b.corner_y)) :
        ncollision = False
    #print(" --> collision: " + str(not ncollision))
    return not ncollision
    

def best_move(room_a, room_b):
    """
    room_a: Room
    room_b: Room that overlaps with room_a
    Moves one of both rooms according to the rules in the subject 
    return : 0 if room_a has been moved, 1 else
    """
    #print(room_a.corner_x + room_a.corner_y)
    #print(room_b.corner_x + room_b.corner_y)
    #print(room_a.size_y)
    #print(room_b.size_x)
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
    #print(" -a_b " + str(a_b) + "\n -d_r " + str(d_r) + "\n -cost " + str(cost))
    
    #print("   -> cost: " + str(cost))
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
    #print(room_a.corner_x + room_a.corner_y)
    #print(room_b.corner_x + room_b.corner_y)
    return a_b
    



def separation_steering_behavior(list_rooms):
    """
    list_rooms: list of Rooms
    moves rooms until none overlap, does not return anything
    """
    (collision,a,b) = detect_col(list_rooms)
    while (collision) :
        #print(" - collision: " + str(collision) + "\n - a: " + str(a) + "\n - b: " + str(b))
        room = best_move(list_rooms[a], list_rooms[b])
        #print (" -> room: " + str(room))
        #ar = list_rooms[a]
        #print("  -> room a : " + str(ar.corner_x) + " | " + str(ar.corner_y) + "\n        " + str(ar.size_x) + " | " + str(ar.size_y))
        #br = list_rooms[b]
        #print("  -> room b : " + str(br.corner_x) + " | " + str(br.corner_y) + "\n        " + str(br.size_x) + " | " + str(br.size_y))
        (collision,a,b) = detect_col(list_rooms)
        #print("=======================================")

def detect_col (list_rooms) :
    """
    list_rooms: list of Rooms
    detect any collision in the list of rooms
    return the bool telling if collision and the index of the two rooms
    """
    for i in range (len(list_rooms)) :
        for j in range (len(list_rooms)) :
            #print(" -i: " + str(i) + " -j: " + str(j))
            if (i != j) :
                if collision_detection(list_rooms[i], list_rooms[j]) :
                    return (True,i,j)
    return (False,0,0)

