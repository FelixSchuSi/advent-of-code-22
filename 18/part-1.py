import numpy as np
import math


lines = open("18/input", "r").read().splitlines()


def parse_line(line):
    return [int(value) for value in line.split(",")]


def get_min_max(lines):
    min_x = min_y = min_z = math.inf
    max_x = max_y = max_z = -math.inf
    for x, y, z in lines:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)
    return min_x, min_y, min_z, max_x, max_y, max_z


def create_grid(parsed_input, dimensions):
    min_x, min_y, min_z, max_x, max_y, max_z = dimensions

    result = np.zeros((max_x - min_x + 1, max_y - min_y + 1, max_z - min_z + 1))
    for x, y, z in parsed_input:
        result[x - min_x, y - min_y, z - min_z] = 1
    return result


def get_neighbour_count(grid, x, y, z):
    neighbour_count = 0
    if x + 1 < grid.shape[0] and grid[x + 1, y, z] == 1:
        neighbour_count += 1
    if y + 1 < grid.shape[1] and grid[x, y + 1, z] == 1:
        neighbour_count += 1
    if z + 1 < grid.shape[2] and grid[x, y, z + 1] == 1:
        neighbour_count += 1
    if x - 1 >= 0 and grid[x - 1, y, z] == 1:
        neighbour_count += 1
    if y - 1 >= 0 and grid[x, y - 1, z] == 1:
        neighbour_count += 1
    if z - 1 >= 0 and grid[x, y, z - 1] == 1:
        neighbour_count += 1
    return neighbour_count


def count_sides(grid):
    possible_sides = (grid == 1).sum() * 6
    sides = possible_sides
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for z in range(grid.shape[2]):
                if grid[x, y, z] == 0:
                    continue

                sides -= get_neighbour_count(grid, x, y, z)
    return sides


parsed_input = [parse_line(line) for line in lines]
dimensions = get_min_max(parsed_input)
grid = create_grid(parsed_input, dimensions)
print(count_sides(grid))
