
def findNewDimensions(list_rooms):
    xMax = -1000000
    yMax = -1000000
    xMin = 1000000
    yMin = 1000000
    for room in list_rooms:
        xMin = min(xMin, room.corner_x)
        yMin = min(yMin, room.corner_y)
        xMax = max(xMax, room.corner_x + room.size_x + 1)
        yMax = max(yMax, room.corner_y + room.size_y + 1)
    return xMax, yMax, xMin, yMin


def generateGrid(xMax, yMax, xMin, yMin, list_rooms, list_corridors):
    grid = [(["#"] * (yMax - yMin - 1)) for i in range(xMax - xMin - 1)]
    for room in list_corridors:
        for i in range(room.size_x):
            for j in range(room.size_y):
                grid[i + room.corner_x - xMin][j + room.corner_y - yMin] = "."
    for room in list_rooms:
        for i in range(1, room.size_x-1):
            for j in range(1,room.size_y - 1):
                grid[i + room.corner_x - xMin][j + room.corner_y - yMin] = " "
    return grid

            

def prettyPrint(grid):
    for line in grid:
        for c in line:
            print(c,end="")
        print()




