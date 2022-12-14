import numpy as np
import math


lines = open("14/input", "r").read().splitlines()
coordinates = [line.split(" -> ") for line in lines]
sand_source = (0, 500)
max_x = -math.inf
min_x = math.inf
max_y = -math.inf
min_y = 0

parsed_coordinates = [
    [[int(num) for num in coord.split(",")] for coord in line] for line in coordinates
]


def create_map(parsed_coordinates):
    global max_x, min_x, max_y, min_y, sand_source
    for line in parsed_coordinates:
        for x, y in line:
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            min_y = min(min_y, y)
    output = np.full((max_y - min_y + 1, max_x - min_x + 1), ".")
    sand_source = (sand_source[0], sand_source[1] - min_x)
    output[sand_source[0], sand_source[1]] = "+"
    for line in parsed_coordinates:
        for i, (x, y) in enumerate(line):
            if i == 0:
                continue
            prev_x, prev_y = line[i - 1]
            x_smaller, x_larger = sorted([x, prev_x])
            y_smaller, y_larger = sorted([y, prev_y])
            output[
                (y_smaller - min_y) : (y_larger - min_y + 1),
                (x_smaller - min_x) : (x_larger - min_x + 1),
            ] = "#"
    return output


def drop_one_sand(map):
    global sand_source
    stop = False
    sand_source_y, sand_source_x = sand_source
    #      (y, x)
    diff = (0, 0)

    def step(map, sand_source_y, sand_source_x, diff):
        try:
            # Try to go down
            if map[sand_source_y + diff[0] + 1, sand_source_x + diff[1]] == ".":
                diff = (diff[0] + 1, diff[1])
                return step(map, sand_source_y, sand_source_x, diff)
            # Try to go to bottom left
            if map[sand_source_y + diff[0] + 1, sand_source_x + diff[1] - 1] == ".":
                diff = (diff[0] + 1, diff[1] - 1)
                return step(map, sand_source_y, sand_source_x, diff)
            # Try to go to bottom right
            if map[sand_source_y + diff[0] + 1, sand_source_x + diff[1] + 1] == ".":
                diff = (diff[0] + 1, diff[1] + 1)
                return step(map, sand_source_y, sand_source_x, diff)

            return diff, False
        except IndexError:
            return diff, True

    diff, stop = step(map, sand_source_y, sand_source_x, diff)
    if not stop:
        map[sand_source_y + diff[0], sand_source_x + diff[1]] = "O"

    return map, stop


map = create_map(parsed_coordinates)

while True:
    map, stop = drop_one_sand(map)
    if stop:
        break


print((map == "O").sum())
