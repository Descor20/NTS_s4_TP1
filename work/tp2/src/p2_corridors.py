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
    list_edgesc = order(list_edges, list_centers)
    ##print("  -> liste des edges not reformat : " + str(list_edges))
    ##print("  -> liste des edges reformat : " + str(list_edgesc))
    for edges in list_edgesc :
        if (edges[0] > len(list_centers) -1 or edges[1] > len(list_centers) -1) :
            return [-1]
        acc = can_access2([], edges[0],  edges[1], l)
        if (not acc) :
            l.append(edges)
    return l



def make_corridors(list_centers, list_corridors):
    """
    list_centers: list of couples int * int
    list_corridors: list of couples int * int
    return a list of Rooms
    """
    l = []
    for edge in list_corridors :
        (x,y) = (list_centers[edge[0]][0],list_centers[edge[1]][1])
        sx = list_centers[edge[1]][0] - x
        sy = list_centers[edge[0]][1] - y

        r1 = Room(sx,1,x,y)
        r2 = Room(1,sy,x,y)

        if (r1.size_x < 0) :
            r1.corner_x += r1.size_x
            r1.size_x *= -1
        if (r2.size_y < 0) :
            r2.corner_y += r2.size_y
            r2.size_y *= -1

        if r1.size_x != 0 :
            l.append(r1)
        if r2.size_y != 0 :
            l.append(r2)
    return l
    

def filter_rooms(list_rooms, list_corridors):
    """
    list_rooms: list of rooms
    list_corridors: list of rooms of size n*1 or 1*n
    return a list of the rooms that intersect at least one corridor
    """
    l = []
    for room in list_rooms :
        for corridor in list_corridors :
            if not (room in l) :
                if (collision_detection(room, corridor)) :
                    l.append(room)
    return l



## ================================ Annexe ==============================

def order (list_edges, list_centers) :
    def distance_sqr(center1, center2):
        return int((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2)
    L = []
    lorder = []
    for edge in list_edges :
        dist = distance_sqr(list_centers[edge[0]], list_centers[edge[1]])
        found = False
        for ed in lorder :
            if ed[0] == dist :
                found = True
                ed.append(edge)
        if (not found) :
            lorder.append([dist, edge])
    while (len(lorder) != 0) :
        min = 0
        valmin = lorder[0][0]
        for j in range(len(lorder)) :
            if (lorder[j][0] < valmin) :
                valmin = lorder[j][0]
                min = j
        l = lorder.pop(min)
        for i in range(len(l)) :
            if (i != 0) :
                L.append(l[i])
    return L



def can_access2 (M, room_a, room_b, list_edges) :
    acc = False
    M.append(room_a)
    if (room_a == room_b) :
        return True
    else :
        for edge in list_edges :
            if (edge[0] == room_a and edge[1] not in M) :
                acc = acc or can_access2 (M, edge[1], room_b, list_edges)
            elif (edge[1] == room_a and edge[0] not in M) :
                acc = acc or can_access2(M, edge[0], room_b, list_edges)
    return acc

## ================================== Tests ============================
## Tests on the Minimal Spreading Tree
"""

list_centers = [(2, 10), (10, 14), (10, 8), (16, 4), (16, 8), (6, 4), (4, 6)]
list_edges = [(0, 1), (0, 3), (0, 6), (1, 2), (2, 4), (2, 6), (3, 4), (3, 5), (4, 5), (5, 6)]

l = minimal_spanning_tree(list_centers, list_edges)
print(" Liste des centres : " + str(list_centers))
print(" Taille liste des centres : " + str(len(list_centers)))
print(" Liste des edges : " + str(list_edges))
print(" Taille liste des edges : " + str(len(list_edges)))
print("----------------------------")
print(" Resultat : " + str(l))
print(" Taille liste resultat : " + str(len(l)))

def distance_squared(center1, center2):
    return int((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2)

s = sum(distance_squared(list_centers[l[i][0]], list_centers[l[i][1]]) for i in range(len(l)))

print("sum x = " + str(s))

print("=============================================================")
"""

## Tests on creating corridor
"""
corridors = make_corridors(list_centers, l)
print(" Corridors = [")
for corridor in corridors :
    print("        x = " + str(corridor.corner_x))
    print("        y = " + str(corridor.corner_y))
    print("        sx = " + str(corridor.size_x))
    print("        sy = " + str(corridor.size_y))
    print("-------------")
print("              ]")
print("=============================================================")
"""