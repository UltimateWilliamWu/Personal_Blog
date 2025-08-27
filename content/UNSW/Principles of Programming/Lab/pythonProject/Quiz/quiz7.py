# Written by *** for COMP9021
#
# Randomly fills an array of size 10x10 with True and False,
# displayed as black and white squares, respectively
# and outputs the minimal number of chess knights needed to jump
# from black square to black square and visit all black squares
# (they can jump back to locations previously visited).


from random import seed, randrange
import sys

dim = 10


def display_grid():
    squares = {False: '⬜', True: '⬛'}
    for row in grid:
        print('    ', ''.join(squares[e] for e in row))


try:
    for_seed, n = (int(i) for i in input('Enter two integers: ').split())
    if not n:
        n = 1
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
if n > 0:
    grid = [[randrange(n) > 0 for _ in range(dim)] for _ in range(dim)]
else:
    grid = [[randrange(-n) == 0 for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print()


def count_knight_components(board):
    def explore(r, c):
        if (r < 0 or r >= dim or c < 0 or c >= dim
                or not board[r][c] or (r, c) in visited):
            return
        visited.add((r, c))
        for dr, dc in knight_moves:
            explore(r + dr, c + dc)

    knight_moves = [
        (2, 1), (1, 2), (-2, 1), (-1, 2),
        (2, -1), (1, -2), (-2, -1), (-1, -2)
    ]
    visited = set()
    count = 0
    for i in range(dim):
        for j in range(dim):
            if board[i][j] and (i, j) not in visited:
                explore(i, j)
                count += 1
    return count


result = count_knight_components(grid)
if result == 0:
    print("No chess knight has explored this board.")
else:
    print(f"At least {result} chess knights have explored this board.")

# INSERT YOUR CODE HERE
