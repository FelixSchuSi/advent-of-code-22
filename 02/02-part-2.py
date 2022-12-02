# rounds = [line.replace("\n", "").split(" ") for line in open("02/02-example-input", "r").readlines()]
rounds = [line.replace("\n", "").split(" ") for line in open("02/02-input", "r").readlines()]

def calc_round_score(opponent_pick: str, lose_draw_win: str) -> int:
    win_score = 0
    pick_score = None
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    if lose_draw_win == "Y":
        win_score = 3
        pick_score = 1 if opponent_pick == "A" else 2 if opponent_pick == "B" else 3
    elif lose_draw_win == "X":
        win_score = 0
        pick_score = 3 if opponent_pick == "A" else 1 if opponent_pick == "B" else 2
    elif lose_draw_win == "Z":
        win_score = 6
        pick_score = 2 if opponent_pick == "A" else 3 if opponent_pick == "B" else 1
    return win_score + pick_score

print(sum([calc_round_score(round[0], round[1]) for round in rounds]))