import unittest
from typing import List


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = ...
        self.assertEqual(main("./input/input_small.txt"), exp_op)



def read_file(fname: str) -> List[List[int]]:
    result = []

    with open(fname) as fp:
        data = fp.read().strip()

    for row in data.split("\n"):
        result.append([int(c) for c in row])

    return result


def scenic_score(data: List[List[int]], x: int, y: int) -> int:

    if not x or not y:
        return 0

    # Top
    all_scores = []
    original_x, original_y = x, y

    score = 0
    while y > 0:
        y -= 1
        score += 1
        if data[original_x][original_y] > data[x][y]:
            continue
        else:
            break

    all_scores.append(score)

    x, y = original_x, original_y

    score = 0
    while x > 0:
        x -= 1
        score += 1
        if data[original_x][original_y] > data[x][y]:
            continue
        else:
            break

    all_scores.append(score)

    x, y = original_x, original_y

    score = 0
    while y < len(data) - 1:
        y += 1
        score += 1
        if data[original_x][original_y] > data[x][y]:
            continue
        else:
            break

    all_scores.append(score)

    x, y = original_x, original_y

    score = 0
    while x < len(data) - 1:
        x += 1
        score += 1
        if data[original_x][original_y] > data[x][y]:
            continue
        else:
            break


    all_scores.append(score)

    final_score = 1
    for s in all_scores:
        final_score *= s

    return final_score


def main(fname: str) -> None:
    data = read_file(fname)
    visible = set()

    # First look from left -> right
    # Then right -> left
    # Then top -> down
    # Then down -> top

    j_range = len(data[0])

    for i in range(len(data)):
        max_height = -1
        for j in range(j_range):
            if data[i][j] > max_height:
                val = f"{i:2}{j:2}"
                max_height = data[i][j]

                if val not in visible:
                    visible.add(val)

    for i in range(len(data)):
        max_height = -1
        for j in range(j_range - 1, 0, -1):
            if data[i][j] > max_height:
                val = f"{i:2}{j:2}"
                max_height = data[i][j]

                if val not in visible:
                    visible.add(val)

    for i in range(len(data)):
        max_height = -1
        for j in range(j_range):
            if data[j][i] > max_height:
                val = f"{j:2}{i:2}"
                max_height = data[j][i]

                if val not in visible:
                    visible.add(val)

    for i in range(len(data)):
        max_height = -1
        for j in range(j_range - 1, 0, -1):
            if data[j][i] > max_height:
                val = f"{j:2}{i:2}"
                max_height = data[j][i]

                if val not in visible:
                    visible.add(val)

    # print(sorted(visible))
    # print(len(visible))

    # Part 2
    highest = 0
    for i in range(len(data)):
        for j in range(j_range):
            # print(f"{i=}, {j=}", end=" ")
            score = scenic_score(data, i, j)
            # print(score)

            if score > highest:
                highest = score

    print("Score is: ", highest)


if __name__ == "__main__":
    main("./2022/day8/input/input_small.txt")
    main("./2022/day8/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")