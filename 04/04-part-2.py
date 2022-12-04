# lines = open("04/example-input", "r").read().splitlines()
lines = open("04/input", "r").read().splitlines()


def parse_line(line):
    left, right = line.split(",")
    left_start_end, right_start_end = left.split("-"), right.split("-")
    left_range, right_range = [
        set(range(int(start), int(end) + 1))
        for start, end in [left_start_end, right_start_end]
    ]
    return len(left_range.intersection(right_range)) > 0


print(sum([parse_line(line) for line in lines]))
