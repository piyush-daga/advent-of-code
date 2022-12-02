from typing import List


def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")


def main(fname: str):
    hand_score = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    priority = {
        "X": "C",
        "Z": "B",
        "Y": "A"
    }
    new_pr = {
        "A": {
            "win": "Z",
            "lose": "Y"
        },
        "B": {
            "win": "X",
            "lose": "Z"
        },
        "C": {
            "win": "Y",
            "lose": "X"
        },
    }
    win_score = {
        "lost": 0,
        "draw": 3,
        "win": 6
    }
    data = read_file(fname=fname)

    # print(data)

    total_points = 0
    new_points = 0
    outcome = ""

    for d in data:
        op, my = d.split(" ")
        # print(op, my)

        if ord(my) - ord(op) == 23:
            outcome = "draw"
        elif priority[my] == op:
            outcome = "win"
        else:
            outcome = "lost"

        total_points += hand_score[my] + win_score[outcome]

        if my == "X":
            new_points += hand_score[new_pr[op]["win"]] + win_score["lost"]
        elif my == "Y":
            new_points += win_score["draw"] + hand_score[chr(ord(op) + 23)]
        else:
            new_points += win_score["win"] + hand_score[new_pr[op]["lose"]]

        # print(new_points)

    print(new_points)
    print(total_points)


if __name__ == "__main__":
    # main("./input/input_small.txt")
    main("./input/input.txt")