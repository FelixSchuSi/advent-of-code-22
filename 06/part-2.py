line = open("06/input", "r").read()


def find_start_of_message_marker(line: str) -> int:
    for i in range(13, len(line)):
        if len(set(line[i - 14 : i])) == 14:
            return i


print(find_start_of_message_marker(line))
