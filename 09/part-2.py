from typing import List, Tuple
import numpy as np

lines = open("09/input", "r").read().splitlines()
VISITED_FIELDS = set()


def parse_input(lines):
    result = []
    for line in lines:
        direction, distance = line.split(" ")
        result.append((direction, int(distance)))
    return result


def get_field_dimensions(instructions: List[Tuple[str, int]]) -> Tuple[int, int]:
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    current_x = 0
    current_y = 0
    for direction, distance in instructions:
        if direction == "R":
            current_x += distance
        elif direction == "L":
            current_x -= distance
        elif direction == "U":
            current_y += distance
        elif direction == "D":
            current_y -= distance
        max_x = max(max_x, current_x)
        max_y = max(max_y, current_y)
        min_x = min(min_x, current_x)
        min_y = min(min_y, current_y)
    height = max_y - min_y + 1
    width = max_x - min_x + 1
    start_x = abs(min_x)
    start_y = abs(min_y)
    return width, height, start_x, start_y


def apply_single_step(direction: str, positions):
    head_pos, knots, start_pos = positions

    for i, knot in enumerate(knots):
        prev_knot = knots[i - 1] if i > 0 else head_pos

        if abs(knot[0] - prev_knot[0]) >= 1 and abs(knot[1] - prev_knot[1]) >= 1:
            if direction == "U" and not knot[1] == (prev_knot[1] + 1):
                knot[0] = prev_knot[0]
            elif direction == "D" and not knot[1] == (prev_knot[1] - 1):
                knot[0] = prev_knot[0]
            elif direction == "R" and not knot[0] == (prev_knot[0] + 1):
                knot[1] = prev_knot[1]
            elif direction == "L" and not knot[0] == (prev_knot[0] - 1):
                knot[1] = prev_knot[1]

    if direction == "R":
        head_pos[0] += 1
    elif direction == "L":
        head_pos[0] -= 1
    elif direction == "U":
        head_pos[1] += 1
    elif direction == "D":
        head_pos[1] -= 1

    for i in range(2):
        if abs(head_pos[i] - tail_pos[i]) > 1:
            if head_pos[i] > tail_pos[i]:
                tail_pos[i] += 1
            else:
                tail_pos[i] -= 1

    print(f"#### step {direction} ####")
    visualize_field(positions)
    VISITED_FIELDS.add((tail_pos[0], tail_pos[1]))
    return (head_pos, tail_pos, start_pos)


def apply_instruction(instruction: Tuple[str, int], positions):
    direction, distance = instruction
    head_pos, tail_pos, start_pos = positions
    print(f"#### instruction {direction} {distance} ####")
    for _ in range(distance):
        head_pos, tail_pos, start_pos = apply_single_step(direction, positions)
    return (head_pos, tail_pos, start_pos)


def visualize_field(positions) -> None:
    head_pos, tail_pos, start_pos = positions
    field: np.ndarray = np.full((height, width), ".")
    field[start_pos[1], start_pos[0]] = "s"
    field[tail_pos[1], tail_pos[0]] = "T"
    field[head_pos[1], head_pos[0]] = "H"
    print(np.flip(field, axis=0))


instructions = parse_input(lines)
width, height, start_x, start_y = get_field_dimensions(instructions)
positions = ([start_x, start_y], [start_x, start_y], [start_x, start_y])
for instruction in instructions:
    positions = apply_instruction(instruction, positions)

print(len(VISITED_FIELDS))
