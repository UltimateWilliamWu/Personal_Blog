# Written by *** for COMP9021
#
# Implements a function display_leftmost_topmost_boundary(*grid)
# whose argument grid is supposed to be a sequence of strings
# all of the same length, consisting of nothing but spaces and *s,
# that represent one or more "full polygons" that do not "touch"
# each other.
# The selected polygon's top boundary is as high as possible ,
# and amongst all polygons whose top boundary is as high as possible,
# the selected polygon's top boundary starts as much to the left
# as possible.
# Each line of the output has the same number of characters,
# that of each string passed as argument.


def display(*grid):
    for e in grid:
        print(*e)


def generate_grids(*grid):
    grids = []
    for line in grid:
        grids.append(list(line))
    return grids


def dfs(cur_point, grids, leftmost_topmost_polygon_points):
    row, col = cur_point
    if row not in range(len(grids)) or col not in range(len(grids[0])) or grids[row][col] != "*" or cur_point in leftmost_topmost_polygon_points:
        return None
    leftmost_topmost_polygon_points.append(cur_point)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direction in directions:
        dfs((row + direction[0], col + direction[1]), grids, leftmost_topmost_polygon_points)


def display_leftmost_topmost_boundary(*grid):
    grids = generate_grids(*grid)
    for line in grids:
        print(" ".join(line))

    start_point = None
    for row in range(len(grids)):
        for col in range(len(grids[0])):
            if grids[row][col] == "*":
                start_point = row, col
                break
        if start_point is not None:
            break
    print(start_point)

    leftmost_topmost_polygon_points = []
    dfs(start_point, grids, leftmost_topmost_polygon_points)
    for row in range(len(grids)):
        for col in range(len(grids[0])):
            if (row, col) not in leftmost_topmost_polygon_points:
                grids[row][col] = " "

    for line in grids:
        print(" ".join(line))

    empty = []
    for row in range(1, len(grids) - 1):
        for col in range(1, len(grids[0]) - 1):
            neighbors = grids[row - 1][col], grids[row + 1][col], grids[row][col - 1], grids[row][col + 1]
            if " " not in neighbors:
                empty.append((row, col))

    for row, col in empty:
        grids[row][col] = " "

    for line in grids:
        print(" ".join(line))

    # REPLACE PASS ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
