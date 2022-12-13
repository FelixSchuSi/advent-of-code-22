parsed_input = [[eval(line) for line in pair.split("\n")] for pair in open("13/input", "r").read().split("\n\n")]


def compare(left, right):
    # print("compare ", left, right)
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

result_sum = 0
for i, (left, right) in enumerate(parsed_input):
    result = compare(left, right)
    if result > 0:
        result_sum += i+1
    print(f"{i+1} {result}")

print(result_sum)
