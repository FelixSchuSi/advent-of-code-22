from math import prod
from typing import List

input = open("11/input", "r").read()
monkeys = [line.split("\n") for line in input.split("\n\n")]


def parse_monkey(monkey: List[str]):
    name = monkey[0]
    items = [
        int(num) for num in monkey[1].split("  Starting items: ")[1:][0].split(", ")
    ]
    operant = monkey[2].split("new = old ")[1][0]
    second_factor = monkey[2].split(" ")[-1]
    operation = eval(f"lambda old: old {operant} {second_factor}")
    test_number = int(monkey[3].split(" ")[-1])
    test_operation = eval(f"lambda x: x % {test_number} == 0")
    if_true_throw_to_monkey = int(monkey[4].split(" ")[-1])
    if_false_throw_to_monkey = int(monkey[5].split(" ")[-1])
    return {
        "name": name,
        "items": items,
        "operation": operation,
        "test_operation": test_operation,
        "divide_by": test_number,
        "if_true_throw_to_monkey": if_true_throw_to_monkey,
        "if_false_throw_to_monkey": if_false_throw_to_monkey,
        "items_inspected": 0,
    }


def simulate_round(parsed_monkeys, round_idx, divisible_by_product):
    print(f"Round {round_idx + 1}:")
    for monkey in parsed_monkeys:
        for item_to_inspect in monkey["items"]:
            monkey["items_inspected"] += 1
            new_item_to_inspect = (
                monkey["operation"](item_to_inspect) % divisible_by_product
            )
            test_result = monkey["test_operation"](new_item_to_inspect)
            target_monkey = None
            if test_result:
                target_monkey = monkey["if_true_throw_to_monkey"]
            else:
                target_monkey = monkey["if_false_throw_to_monkey"]

            parsed_monkeys[target_monkey]["items"].append(new_item_to_inspect)
            # print(
            #     f"Round {round_idx + 1}: {monkey['name']} {item_to_inspect} -> {new_item_to_inspect} -> {target_monkey}"
            # )
        monkey["items"] = []

    # for monkey in parsed_monkeys:
    #     print(f"{monkey['name']} has {monkey['items']}")
    return parsed_monkeys


parsed_monkeys = [parse_monkey(monkey) for monkey in monkeys]
divisible_by_product = prod([monkey["divide_by"] for monkey in parsed_monkeys])
for round_idx in range(10000):
    parsed_monkeys = simulate_round(parsed_monkeys, round_idx, divisible_by_product)

# for monkey in parsed_monkeys:
#     print(monkey["name"], monkey["items_inspected"], monkey["items"])

monkey_one, monkey_two = [
    monkey
    for monkey in sorted(
        parsed_monkeys, key=lambda x: x["items_inspected"], reverse=True
    )
][0:2]
print(monkey_one["items_inspected"] * monkey_two["items_inspected"])
