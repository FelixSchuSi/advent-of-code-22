from typing import List, Tuple

lines = open("10/input", "r").read().splitlines()
cycle_count = 0
register_x = 1
signals = []
output = ""


def parse_insruction(line: str):
    if line == "noop":
        return "noop", 0
    else:
        command, value = line.split(" ")
        return command, int(value)


def tick():
    global cycle_count
    global register_x
    global signals
    global output

    cycle_count += 1
    if abs(cycle_count % 40 - (register_x + 1)) <= 1:
        output += "#"
    else:
        output += " "
    if cycle_count % 40 == 0:
        output += "\n"

    if cycle_count == 20 or (cycle_count > 20 and (cycle_count - 20) % 40 == 0):
        signals.append((cycle_count, register_x))


def execute_instruction(instruction: Tuple[str, int]):
    global cycle_count
    global register_x

    command, value = instruction
    tick()

    if command == "noop":
        pass
    else:
        tick()
        register_x += value


[execute_instruction(parse_insruction(line)) for line in lines]
print(output)
