line = open("06/input", "r").read()


def find_start_of_pack_marker(line: str) -> int:
    for i in range(3, len(line)):
        if len(set(line[i - 4 : i])) == 4:
            return i


print(find_start_of_pack_marker(line))
