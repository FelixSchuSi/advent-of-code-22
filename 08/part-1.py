import numpy as np

lines = open("08/input", "r").read().splitlines()
lines = np.array([[int(char) for char in line] for line in lines])


def are_trees_visible_from_position(position: str, trees):
    result = np.zeros(trees.shape, dtype=int)
    if position == "top":
        for y, row in enumerate(trees):
            for x, cell in enumerate(row):
                if y == 0:
                    result[y, x] = 1
                    continue
                if trees[y, x] > max(trees[:y, x]):
                    result[y, x] = 1
    if position == "bottom":
        for y, row in enumerate(trees):
            for x, col in enumerate(row):
                if y >= len(trees) - 1:
                    result[y, x] = 1
                    continue
                if trees[y, x] > max(trees[y + 1 :, x]):
                    result[y, x] = 1
    if position == "left":
        for y, row in enumerate(trees):
            for x, cell in enumerate(row):
                if x == 0:
                    result[y, x] = 1
                    continue
                if trees[y, x] > max(trees[y, :x]):
                    result[y, x] = 1
    if position == "right":
        for y, row in enumerate(trees):
            for x, col in enumerate(row):
                if x >= len(trees[0]) - 1:
                    result[y, x] = 1
                    continue
                if trees[y, x] > max(trees[y, x + 1 :]):
                    result[y, x] = 1
    return result


result = (
    are_trees_visible_from_position("top", lines)
    | are_trees_visible_from_position("bottom", lines)
    | are_trees_visible_from_position("right", lines)
    | are_trees_visible_from_position("left", lines)
)

print(np.sum(result))
