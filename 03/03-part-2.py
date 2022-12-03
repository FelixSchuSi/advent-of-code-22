from typing import List


# rucksacks = open("03/example-input", "r").read().splitlines()
rucksacks = open("03/input", "r").read().splitlines()
groups = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]


def get_priority_of_group(rucksack_group: List[str]) -> int:
    first, second, third = rucksack_group
    id_characters = set(first).intersection(set(second)).intersection(set(third))

    priority = 0
    for character in id_characters:
        if character.islower():
            prio = ord(character) - 96
            priority += prio
        else:
            prio = ord(character) - 38
            priority += prio
    return priority


print(sum([get_priority_of_group(rucksack_group) for rucksack_group in groups]))
