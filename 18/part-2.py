cubes = {tuple(map(int, l.split(","))) for l in open("18/input")}
neighbours = lambda x, y, z: {
    (x + 1, y, z),
    (x - 1, y, z),
    (x, y + 1, z),
    (x, y - 1, z),
    (x, y, z + 1),
    (x, y, z - 1),
}

seen = set()
todo = [(-1, -1, -1)]

while todo:
    here = todo.pop()
    todo += [
        s for s in (neighbours(*here) - cubes - seen) if all(-1 <= c <= 25 for c in s)
    ]
    seen |= {here}

print(sum((n in seen) for c in cubes for n in neighbours(*c)))
