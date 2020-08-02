
import pprint

LAND_CELL = '1'
WATER_CELL = '0'
LAND_VISITED_CELL = '2'
WATER_VISITED_CELL = '3'

def print_landscape(grid):
    pprint.pprint(grid)

def bfs(grid, x, y):
    row, col = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    if 0 <= x < row and 0<= y < col and (grid[x][y] != LAND_VISITED_CELL and grid[x][y] != WATER_CELL):
        if grid[x][y] == LAND_CELL:
            grid[x][y] = LAND_VISITED_CELL

        for direction in directions:
            bfs(grid, x + direction[0], y + direction[1])

    else:
        return 0


def numIslands(grid):
    row, col = len(grid), len(grid[0])
    num_of_islands = 0
    for x in range(row):
        for y in range(col):
            if grid[x][y] == LAND_CELL:
                bfs(grid, x, y)
                #print_landscape(grid)
                #print("\n")
                num_of_islands = num_of_islands + 1
    return num_of_islands

if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","1"],
        ["1","1","0","0","1"],
        ["0","0","0","1","0"]
        ]
    result = numIslands(grid)
    print("Number of islands : {}".format(result))
