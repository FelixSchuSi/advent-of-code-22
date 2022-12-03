# rucksacks = open("03/example-input", "r").read().splitlines()
rucksacks = open("03/input", "r").read().splitlines()


def get_priority_of_rucksacks(rucksack: str) -> int:
    left, right = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    characters_in_both_halfs = set(left).intersection(set(right))
    priority = 0
    for character in characters_in_both_halfs:
        if character.islower():
            prio = ord(character) - 96
            priority += prio
        else:
            prio = ord(character) - 38
            priority += prio
    return priority


print(sum([get_priority_of_rucksacks(rucksack) for rucksack in rucksacks]))
