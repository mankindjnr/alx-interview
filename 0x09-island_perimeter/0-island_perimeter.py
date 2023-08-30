#!/usr/bin/python3
"""perimeter of an island"""


def island_perimeter(grid):
    """find the perimeter"""
    perimeter = 0
    row_len = len(grid[0])
    grid_len = len(grid)

    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k] != 0:
                # check back
                if k != 0:
                    if grid[i][k - 1] == 0:
                        perimeter += 1
                # check front
                if k < row_len - 1:
                    if grid[i][k + 1] == 0:
                        perimeter += 1
                # check up/is [i] != 0
                if i != 0:
                    if grid[i - 1][k] == 0:
                        perimeter += 1
                # check down/if 1 == len
                if i < grid_len - 1:
                    if grid[i + 1][k] == 0:
                        perimeter += 1

    return perimeter
