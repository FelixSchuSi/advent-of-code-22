a = [list(line) for line in open("12/input", "r").read().splitlines()]


def terrain():
    grid = dict()
    for R in range(len(a)):
        for C in range(len(a[0])):
            grid[(R, C)] = a[R][C]
            if a[R][C] == "S":
                pos = (R, C)
                grid[(R, C)] = "a"
            elif a[R][C] == "E":
                target = (R, C)
                grid[(R, C)] = "z"
    return grid, pos, target


def neighbors(pos, visited):
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    R, C = pos
    neighbors = set()
    for i in range(4):
        rr, cc = R + dr[i], C + dc[i]
        if (rr, cc) in grid.keys() and (rr, cc) not in visited:
            if grid[(R, C)] >= chr(ord(grid[(rr, cc)]) - 1):
                neighbors.add((rr, cc))
    return neighbors


def dijkstra(pos):
    path = dict()
    newnodes = dict()
    newnodes[pos] = 0
    while newnodes:
        (R, C) = min(newnodes, key=newnodes.get)
        dist = newnodes.pop((R, C))
        for n in neighbors((R, C), S):
            changed = False
            if not changed:
                newnodes[n] = dist + 1
        path[(R, C)] = dist
        grid.pop((R, C))
        if target in path.keys():

            return path[target]


S = dict()
trails = dict()
grid, _, target = terrain()

for pos in grid.keys():
    if grid[pos] == "a":
        trails[pos] = 1000
for pos in trails.keys():
    grid, _, target = terrain()
    dijkstra_result = dijkstra(pos)
    if dijkstra_result:
        trails[pos] = dijkstra_result
print(min(trails.values()))
