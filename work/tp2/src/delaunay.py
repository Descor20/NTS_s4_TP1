import numpy
from scipy.spatial import Delaunay



def center(room):
    return [room.corner_x + room.size_x//2, room.corner_y + room.size_y//2] 
    
def make_centers(list_rooms):
    return [(room.corner_x + room.size_x//2, room.corner_y + room.size_y//2) for room in list_rooms]
    
def delaunay(list_rooms):
    list_centers = make_centers(list_rooms)
    centers = numpy.array(list_centers)
    triangles = Delaunay(centers)
    list_vertices = []
    for triangle in triangles.simplices:
        tri = numpy.sort(triangle)
        v1 = tri[0],tri[1]
        v2 = tri[1],tri[2]
        v3 = tri[0],tri[2]
        if v1 not in list_vertices:
            list_vertices.append(v1)
        if v2 not in list_vertices:
            list_vertices.append(v2)
        if v3 not in list_vertices:
            list_vertices.append(v3)

    return list_vertices, list_centers

