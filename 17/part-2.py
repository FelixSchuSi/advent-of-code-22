rocks, rock_index = (
    (0, 1, 2, 3),
    (1, 0 + 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 0 + 1j, 0 + 2j, 0 + 3j),
    (0, 1, 0 + 1j, 1 + 1j),
), 0

jets, jet_index = [ord(x) - 61 for x in open("17/input").read()], 0
tower, cache, top = set(), dict(), 0

empty = lambda pos: pos.real in range(7) and pos.imag > 0 and pos not in tower
check = lambda pos, dir, rock: all(empty(pos + dir + r) for r in rock)

for step in range(int(1e12)):
    pos = complex(2, top + 4)
    key = rock_index, jet_index
    if key in cache:
        S, T = cache[key]
        d, m = divmod(1e12 - step, step - S)
        if m == 0:
            print(int(top + (top - T) * d))
            break
    else:
        cache[key] = step, top

    rock = rocks[rock_index]
    rock_index = (rock_index + 1) % len(rocks)

    while True:
        jet = jets[jet_index]
        jet_index = (jet_index + 1) % len(jets)

        if check(pos, jet, rock):
            pos += jet
        if check(pos, -1j, rock):
            pos += -1j
        else:
            break

    tower |= {pos + r for r in rock}
    top = max(top, pos.imag + [1, 0, 2, 2, 3][rock_index])
