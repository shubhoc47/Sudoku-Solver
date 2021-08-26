#
# main.py
# Sudoku-solver
#
# Created by SHUBHO on 26/8/21.
#


def printGrid():
    print()
    global grid
    for x in range(9):
        for y in range(9):
            print(grid[x][y], end=" ")
        print()


def checker(k, rw, cl):
    for x in range(9):
        if grid[rw][x] == k:
            return False
    for x in range(9):
        if grid[x][cl] == k:
            return False
    p, q = ((rw // 3) * 3), ((cl // 3) * 3)

    for x in range(p, p + 3):
        for y in range(q, q + 3):
            if grid[x][y] == k:
                return False
    return True


def solver():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(1, 10):
                    if checker(k, i, j):
                        grid[i][j] = k
                        solver()
                        grid[i][j] = 0
                return
    printGrid()


rows, cols = (9, 9)
grid = []

for i in range(rows):
    col = input()
    col = col.split()
    col = list(map(int, col))
    grid.append(col)
solver()
