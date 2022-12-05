from typing import List


stacks_str, rearrangement_instructions = open("05/input", "r").read().split("\n\n")


def clean_stack_line(stack_line):
    return (
        stack_line.replace("    ", ".")
        .replace(" ", "")
        .replace("[", "")
        .replace("]", "")
    )


def prepare_stacks(stacks_str: str) -> List[List[str]]:
    stacks_lines = stacks_str.split("\n")
    stacks = [[] for _ in range(len(stacks_lines[-1].split("   ")))]
    stacks_lines.pop()  # remove line with indexes
    cleaned_stacks_lines = reversed(
        [clean_stack_line(stack_line) for stack_line in stacks_lines]
    )

    for line in cleaned_stacks_lines:
        for i, char in enumerate(line):
            if char == ".":
                continue
            stacks[i].append(char)
    return stacks


def parse_rearrangement_instructions(
    rearrangement_instructions: str,
) -> List[List[int]]:
    result = []
    for line in rearrangement_instructions.split("\n"):
        instruction = []
        for elem in line.replace("move ", "").split(" from "):
            for e in elem.split(" to "):
                instruction.append(int(e))
        result.append(instruction)
    return result


def apply_rearrangement_instruction(
    stacks: List[List[str]], instruction: List[int]
) -> List[List[str]]:
    amount, source, destination = list(instruction)
    items = []
    for _ in range(amount):
        items.append(stacks[source - 1].pop())
    for item in reversed(items):
        stacks[destination - 1].append(item)
    return stacks


def read_solution_from_stacks(stacks: List[List[str]]) -> str:
    return "".join([stack[-1] for stack in stacks])


stacks = prepare_stacks(stacks_str)

for instruction in parse_rearrangement_instructions(rearrangement_instructions):
    stacks = apply_rearrangement_instruction(stacks, instruction)


print(stacks)
print(read_solution_from_stacks(stacks))
