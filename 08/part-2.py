import math
from typing import List
import numpy as np

lines = open("08/input", "r").read().splitlines()
trees: np.ndarray = np.array([[int(char) for char in line] for line in lines])


def get_trees_to_top_edge(x: int, y: int, trees: np.ndarray) -> List[int]:
    return trees[:y, x][::-1]


def get_trees_to_bottom_edge(x: int, y: int, trees: np.ndarray) -> List[int]:
    return trees[y + 1 :, x]


def get_trees_to_left_edge(x: int, y: int, trees: np.ndarray) -> List[int]:
    return trees[y, :x][::-1]


def get_trees_to_right_edge(x: int, y: int, trees: np.ndarray) -> List[int]:
    return trees[y, x + 1 :]


def calc_score_for_trees(tree_under_consideration: int, trees: List[int]) -> int:
    score = 0
    for tree in trees:
        if tree >= tree_under_consideration:
            score += 1
            break
        else:
            score += 1
    return score


def calculate_score_for_position(x: int, y: int, trees: np.ndarray) -> int:
    get_trees_functions = [
        get_trees_to_top_edge,
        get_trees_to_bottom_edge,
        get_trees_to_left_edge,
        get_trees_to_right_edge,
    ]
    scores = []
    for func in get_trees_functions:
        scores.append(calc_score_for_trees(trees[y, x], func(x, y, trees)))

    return math.prod(scores)


best_score = 0
for y, row in enumerate(trees):
    for x, cell in enumerate(row):
        best_score = max(best_score, calculate_score_for_position(x, y, trees))

print(best_score)
