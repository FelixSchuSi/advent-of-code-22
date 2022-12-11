from typing import List, Tuple

lines = open("10/input", "r").read().splitlines()
cycle_count = 0
register_x = 1
signals = []


def parse_insruction(line: str):
    if line == "noop":
        return "noop", 0
    else:
        command, value = line.split(" ")
        return command, int(value)


def execute_instruction(instruction: Tuple[str, int]):
    global cycle_count
    global register_x
    global signals
    command, value = instruction
    cycle_count += 1
    if cycle_count == 20 or (cycle_count > 20 and (cycle_count - 20) % 40 == 0):
        signals.append((cycle_count, register_x))
    if command == "noop":
        pass
    else:
        cycle_count += 1
        if cycle_count == 20 or (cycle_count > 20 and (cycle_count - 20) % 40 == 0):
            signals.append((cycle_count, register_x))
        register_x += value


def calculate_result(signals: List[Tuple[int, int]]):
    result = 0
    for cycle, signal in signals:
        result += cycle * signal
    return result


[execute_instruction(parse_insruction(line)) for line in lines]
print(calculate_result(signals))
