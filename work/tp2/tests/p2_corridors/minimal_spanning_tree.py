import pytest
from src.p2_corridors import minimal_spanning_tree
from src.room import Room


def distance_squared(center1, center2):
    return int((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2)

def test_mst1():
    list_centers = [(2, 10), (10, 14), (10, 8), (16, 4), (16, 8), (6, 4), (4, 6)]
    list_edges = [(0, 1), (0, 3), (0, 6), (1, 2), (2, 4), (2, 6), (3, 4), (3, 5), (4, 5), (5, 6)]
    r = minimal_spanning_tree(list_centers, list_edges)
    s = sum(distance_squared(list_centers[list_edges[i][0]], list_centers[list_edges[i][1]]) for i in range(len(r)))
    # MST has 6 edges and sum of squares of weights of its edges is 156
    assert len(r) == 6
    assert s == 156
