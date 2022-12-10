import numpy as np

lines = open("08/example-input", "r").read().splitlines()
lines = np.array([[int(char) for char in line] for line in lines])


def calc_position_score(trees, x_position: int, y_position: int):
    # print(trees)
    x_len = len(trees[0])
    y_len = len(trees)
    # print("shape: ", x_len, y_len)

    result_top = 0
    result_bottom = 0
    result_left = 0
    result_right = 0
    # top
    for y_diff in range(1, y_position + 1):
        # When source tre is one tree away from the edge the score is always 1
        if y_position <= 1:
            result_top = 1
            break
        elif (
            trees[y_position - y_diff, x_position]
            >= trees[y_position - y_diff + 1, x_position]
        ):
            result_top = result_top + 1
            if y_position - y_diff == 0:
                break
        # When we only look one tree away from source we increase the score by one
        elif y_diff == 1:
            result_top = result_top + 1
        else:
            break
    # bottom
    for y_diff in range(1, y_len - y_position + 1):
        # When source tre is one tree away from the edge the score is always 1
        if y_position >= y_len - 2:
            result_bottom = 1
            break
        # When the current tree is higher than the previous one, we add 1 to the score
        elif (
            trees[y_position + y_diff, x_position]
            >= trees[y_position + y_diff - 1, x_position]
        ):
            result_bottom = result_bottom + 1
            # When we get to the bottom edge of the forest, we break the loop
            if y_position + y_diff == y_len - 1:
                break
        # When we only look one tree away from source we increase the score by one
        elif y_diff == 1:
            result_bottom = result_bottom + 1
            # if trees[y_position + y_diff, x_position] > trees[y_position, x_position]:
            #     break
        else:
            break
    # left
    for x_diff in range(1, x_position + 1):
        # When source tree is one tree away from the edge the score is always 1
        print(
            "x_position - x_diff: ",
            x_position - x_diff,
            "value",
            trees[y_position, x_position - x_diff],
        )
        if x_position <= 1:
            result_left = 1
            break
        elif (
            trees[y_position, x_position - x_diff]
            > trees[y_position, x_position - x_diff + 1]
        ):
            result_left = result_left + 1
            if x_position - x_diff == 0:
                break
        # When we only look one tree away from source we increase the score by one
        elif x_diff == 1:
            result_left = result_left + 1
            if trees[y_position, x_position - x_diff] >= trees[y_position, x_position]:
                break
        else:
            break
    # right
    for x_diff in range(1, x_len - x_position + 1):
        # When source tre is one tree away from the edge the score is always 1
        if x_position >= x_len - 2:
            result_right = 1
            break
        # When the current tree is higher than the previous one, we add 1 to the score
        elif (
            trees[y_position, x_position + x_diff]
            >= trees[y_position, x_position + x_diff - 1]
        ):
            result_right = result_right + 1
            # When we get to the bottom edge of the forest, we break the loop
            if x_position + x_diff == x_len - 1:
                break
        # When we only look one tree away from source we increase the score by one
        elif x_diff == 1:
            result_right = result_right + 1
        else:
            break
    if result_top * result_bottom * result_left * result_right == 12:
        print(
            "score: ",
            result_top * result_bottom * result_left * result_right,
            "pos",
            x_position,
            y_position,
        )
        print("result_top", result_top)
        print("result_bottom", result_bottom)
        print("result_left", result_left)
        print("result_right", result_right)
    return result_top * result_bottom * result_left * result_right


best_score = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        score = calc_position_score(lines, x, y)
        best_score = max(score, best_score)
calc_position_score(lines, 3, 2)

print(best_score)
