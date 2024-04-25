
from delaunay import *
from utils import *
from p1_room_creation import *
from p2_corridors import *
from room import Room




def create_maze(n, sizeX, sizeY, maxX, maxY, size_main_x, size_main_y):

    ### Create rooms, then re_move the over-lapping
    list_rooms = generate_rooms(n, sizeX, sizeY, maxX, maxY)
    separation_steering_behavior(list_rooms)
    main_rooms = choose_main_rooms(list_rooms, size_main_x, size_main_y)
    
    x_max, y_max, x_min, y_min = findNewDimensions(list_rooms)
    prettyPrint(generateGrid(x_max, y_max, x_min, y_min, list_rooms,[]))

    ### Create a minimum spanning tree (delaunay is given)
    list_vertices, list_centers = delaunay(main_rooms)
    minspantree = minimal_spanning_tree(list_centers, list_vertices)
    
    ### From the Tree, create the corridors
    list_corridors = make_corridors(list_centers, minspantree)
    list_rooms = filter_rooms(list_rooms, list_corridors)
    
    ### Display (provided)
    x_max, y_max, x_min, y_min = findNewDimensions(list_rooms)
    return generateGrid(x_max, y_max, x_min, y_min, list_rooms, list_corridors)
    
    
if __name__ == "__main__":
    prettyPrint(create_maze(50, 5, 15, 40, 40, 8, 8))
    



