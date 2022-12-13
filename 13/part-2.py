from functools import cmp_to_key


parsed_input = [
    [eval(line) for line in pair.split("\n")]
    for pair in open("13/input", "r").read().split("\n\n")
]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return right - left
    elif isinstance(left, list) and isinstance(right, list):
        for l_item, r_item in zip(left, right):
            result = compare(l_item, r_item)
            if result != 0:
                return result
        return len(right) - len(left)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    assert False


two, six = [[2]], [[6]]
parsed_input.append([two, six])
parsed_input = [item for sublist in parsed_input for item in sublist]
parsed_input.sort(key=cmp_to_key(compare), reverse=True)
print((parsed_input.index(two) + 1) * (parsed_input.index(six) + 1))
