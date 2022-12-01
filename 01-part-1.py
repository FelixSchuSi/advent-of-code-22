lines = "".join(open("01-input", "r").readlines())
# lines = "".join(open("01-example-input", "r").readlines())
inventories = lines.split("\n\n")
inventories = [[int(calory_count) for calory_count in inventory.split("\n")] for inventory in inventories]
calorie_sums = [sum(inventory) for inventory in inventories]
print(max(calorie_sums))
