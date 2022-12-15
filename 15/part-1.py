from itertools import chain
import numpy as np

lines = open("15/input", "r").read().splitlines()
lines = [
    [
        int(coord)
        for coord in line.replace("Sensor at x=", "")
        .replace(", y", "")
        .replace(": closest beacon is at x", "")
        .split("=")
    ]
    for line in lines
]


def create_map(coordinates, min_max):
    x_min, x_max, y_min, y_max = min_max
    output = np.full((y_max - y_min + 1, x_max - x_min + 1), ".")
    for sensor_x, sensor_y, beacon_x, beacon_y in coordinates:
        output[sensor_y - y_min, sensor_x - x_min] = "S"
        output[beacon_y - y_min, beacon_x - x_min] = "B"
    return output


def get_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_rect_coords(sensor, diff, min_max):
    x_min, x_max, y_min, y_max = min_max
    x, y = sensor
    dim_1_diff, dimm_2_diff = diff
    result = []

    result.append((x + dim_1_diff - x_min, y + dimm_2_diff - y_min))
    result.append((x + dim_1_diff - x_min, y - dimm_2_diff - y_min))
    result.append((x - dim_1_diff - x_min, y + dimm_2_diff - y_min))
    result.append((x - dim_1_diff - x_min, y - dimm_2_diff - y_min))
    result.append((x + dimm_2_diff - x_min, y + dim_1_diff - y_min))
    result.append((x + dimm_2_diff - x_min, y - dim_1_diff - y_min))
    result.append((x - dimm_2_diff - x_min, y + dim_1_diff - y_min))
    result.append((x - dimm_2_diff - x_min, y - dim_1_diff - y_min))

    result = (
        (x, y)
        for x, y in result
        if x >= 0 and y >= 0 and x < x_max - x_min + 1 and y < y_max - y_min + 1
    )
    return result


def draw_on_map(map, coordinates, min_max):
    for sensor_x, sensor_y, beacon_x, beacon_y in coordinates:
        distance = get_manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        for diff in range(1, distance + 1):
            dim_1_diff = diff
            dim_2_diff = 0
            while dim_1_diff >= 0:
                for x_coord, y_coord in get_rect_coords(
                    (sensor_x, sensor_y), (dim_1_diff, dim_2_diff), min_max
                ):
                    if map[y_coord, x_coord] == ".":
                        map[y_coord, x_coord] = "#"
                dim_1_diff -= 1
                dim_2_diff += 1
    return map


x_coords = list(chain([line[0] for line in lines], [line[2] for line in lines]))
y_coords = list(chain([line[1] for line in lines], [line[3] for line in lines]))
x_min, x_max, y_min, y_max = min(x_coords), max(x_coords), min(y_coords), max(y_coords)

# map = create_map(lines, (x_min, x_max, y_min, y_max))
# map = draw_on_map(map, lines, (x_min, x_max, y_min, y_max))
# for row in map:
#     print("".join(row))

print((map[10] == "#").sum())
