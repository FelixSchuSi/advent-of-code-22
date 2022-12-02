# rounds = [line.replace("\n", "").split(" ") for line in open("02/02-example-input", "r").readlines()]
rounds = [line.replace("\n", "").split(" ") for line in open("02/02-input", "r").readlines()]

def calc_round_score(opponent_pick: str, our_pick: str) -> int:
    win_score = 0
    pick_score = 1 if our_pick == "X" else 2 if our_pick == "Y" else 3
    if our_pick == "X" and opponent_pick == "C":
        win_score = 6
    if our_pick == "Y" and opponent_pick == "A":
        win_score = 6
    if our_pick == "Z" and opponent_pick == "B":
        win_score = 6
    if our_pick == "X" and opponent_pick == "A" or our_pick == "Y" and opponent_pick == "B" or our_pick == "Z" and opponent_pick == "C":
        win_score = 3
    return win_score + pick_score

print(sum([calc_round_score(round[0], round[1]) for round in rounds]))