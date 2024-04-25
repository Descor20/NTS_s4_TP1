from room import *
from p1_room_creation import collision_detection



def choose_main_rooms(list_rooms, size_xmin, size_ymin):
    """
    list_rooms: list of Rooms
    size_xmin: int
    size_xmin: int
    return: a list of rooms (from list_rooms) which dimensions are greater than size_xmin x size_ymin
    """
    l = []
    for room in list_rooms :
        if (size_xmin < room.size_x and size_ymin < room.size_y) :
            l.append(room)
    # Dummy result, for initial display
    return l



def minimal_spanning_tree(list_centers, list_edges):
    """
    list_centers: list of couples int * int
    list_edges: list of couples int*int
    return: a list of couples int*int (included in list_edges) that form a minimal spanning tree
    """
    l = []
    print(len(list_centers))
    for centeri in range (len(list_centers)) :
        for centerj in range (len(list_centers)) :
            direct_e = False
            ed = (0,0)
            for edge in list_edges :
                if (edge[0] == centeri and edge[1] == centerj) :
                    ed = edge
                    direct_e = True
            if (direct_e) :
                (acc, edge) = can_access([], centeri, centerj, l)
                if (not acc) :
                    l.append(ed)
    return l



def make_corridors(list_centers, list_corridors):
    """
    list_centers: list of couples int * int
    list_corridors: list of couples int * int
    return a list of Rooms
    """
    return []
    

def filter_rooms(list_rooms, list_corridors):
    """
    list_rooms: list of rooms
    list_corridors: list of rooms of size n*1 or 1*n
    return a list of the rooms that intersect at least one corridor
    """
    # Dummy result, for initial display
    return list_rooms



## ================================ Annexe ==============================

def can_access (M, room_a, room_b, list_edges) :
    acc = False
    if (room_a == room_b) :
        return (True,(0,0))
    for edge in list_edges :
        if (edge[0] == room_a) :
            if (edge[1] == room_b) :
                return True
            elif (edge in M) :
                M.append(edge)
                acc = can_access(M, room_a, room_b)
        if (acc) :
            return (acc,edge)
    return (acc,(0,0))

