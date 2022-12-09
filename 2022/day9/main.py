import unittest
from copy import deepcopy
from typing import List

import numpy as np

ROW_INDEX = 0
COL_INDEX = 1

class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = ...
        self.assertEqual(main("./input/input_small.txt"), exp_op)


def make_grid(size: int) -> np.ndarray:
    return np.zeros((size, size), int)


def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")


def move_tail(current_head: List[int], current_tail: List[int]):
    # Are they on the same row
    if current_head[ROW_INDEX] == current_tail[ROW_INDEX]:
        diff = current_head[COL_INDEX] - current_tail[COL_INDEX]
        if abs(diff) > 1:
            while abs(current_head[COL_INDEX] - current_tail[COL_INDEX]) != 1:
                current_tail[COL_INDEX] = current_tail[COL_INDEX] + 1 if diff > 0 else current_tail[COL_INDEX] - 1

        return
    # Are they on the same col
    if current_head[COL_INDEX] == current_tail[COL_INDEX]:
        diff = current_head[ROW_INDEX] - current_tail[ROW_INDEX]
        if abs(diff) > 1:
            while abs(current_head[ROW_INDEX] - current_tail[ROW_INDEX]) != 1:
                current_tail[ROW_INDEX] = current_tail[ROW_INDEX] + 1 if diff > 0 else current_tail[ROW_INDEX] - 1

        return

    # Diagonal movement
    x_diff = current_head[ROW_INDEX] - current_tail[ROW_INDEX]
    y_diff = current_head[COL_INDEX] - current_tail[COL_INDEX]

    if abs(x_diff) == 1 and abs(y_diff) == 1:
        return

    if abs(x_diff) > 1 or abs(y_diff) > 1:
        # Now we need to move diagonally
        current_tail[ROW_INDEX] = current_tail[ROW_INDEX] + 1 if x_diff > 0 else current_tail[ROW_INDEX] - 1
        current_tail[COL_INDEX] = current_tail[COL_INDEX] + 1 if y_diff > 0 else current_tail[COL_INDEX] - 1

        move_tail(current_head=current_head, current_tail=current_tail)


def move_head_tail(grid: np.ndarray, current_head_pos: List[int], current_tail_pos: List[int], move: str):
    direction, steps = move.split(" ")
    steps = int(steps)

    if direction == "R":
        for _ in range(steps):
            current_head_pos[COL_INDEX] += 1
            move_tail(current_head=current_head_pos, current_tail=current_tail_pos)
            grid[current_tail_pos[ROW_INDEX]][current_tail_pos[COL_INDEX]] += 1
    elif direction == "L":
        for _ in range(steps):
            current_head_pos[COL_INDEX] -= 1
            move_tail(current_head=current_head_pos, current_tail=current_tail_pos)
            grid[current_tail_pos[ROW_INDEX]][current_tail_pos[COL_INDEX]] += 1
    elif direction == "D":
        for _ in range(steps):
            current_head_pos[ROW_INDEX] += 1
            move_tail(current_head=current_head_pos, current_tail=current_tail_pos)
            grid[current_tail_pos[ROW_INDEX]][current_tail_pos[COL_INDEX]] += 1
    elif direction == "U":
        for _ in range(steps):
            current_head_pos[ROW_INDEX] -= 1
            move_tail(current_head=current_head_pos, current_tail=current_tail_pos)
            grid[current_tail_pos[ROW_INDEX]][current_tail_pos[COL_INDEX]] += 1


def move_head_tail_longer(grid: np.ndarray, move: str, pos: List[List[int]]):
    direction, steps = move.split(" ")
    steps = int(steps)


    if direction == "R":
        for i in range(steps):
            for i, val in enumerate(pos):
                # which means this is the actual head
                if i == 0:
                    val[COL_INDEX] += 1
                if i == 9:
                    break
                move_tail(current_head=val, current_tail=pos[i + 1])
                if i == 8:
                    # Increment for the tail
                    grid[pos[i + 1][ROW_INDEX]][pos[i + 1][COL_INDEX]] += 1

    elif direction == "L":
        for _ in range(steps):
            for i, val in enumerate(pos):
                # which means this is the actual head
                if i == 0:
                    val[COL_INDEX] -= 1
                if i == 9:
                    break
                move_tail(current_head=val, current_tail=pos[i + 1])
                if i == 8:
                    # Increment for the tail
                    grid[pos[i + 1][ROW_INDEX]][pos[i + 1][COL_INDEX]] += 1
    elif direction == "D":
        for _ in range(steps):
            for i, val in enumerate(pos):
                # which means this is the actual head
                if i == 0:
                    val[ROW_INDEX] += 1
                if i == 9:
                    break
                move_tail(current_head=val, current_tail=pos[i + 1])
                if i == 8:
                    # Increment for the tail
                    grid[pos[i + 1][ROW_INDEX]][pos[i + 1][COL_INDEX]] += 1
    elif direction == "U":
        for _ in range(steps):
            for i, val in enumerate(pos):
                # which means this is the actual head
                if i == 0:
                    val[ROW_INDEX] -= 1
                if i == 9:
                    break
                move_tail(current_head=val, current_tail=pos[i + 1])
                if i == 8:
                    # Increment for the tail
                    grid[pos[i + 1][ROW_INDEX]][pos[i + 1][COL_INDEX]] += 1


def main(fname: str) -> None:
    data = read_file(fname)
    grid_size = 1000
    start = 500

    grid = make_grid(grid_size)
    # start at the middle?
    head_pos, tail_pos = [start, start], [start, start]
    # Mark the starting pos as visited
    grid[start][start] = 1

    # Part 1
    for d in data:
        move_head_tail(grid, head_pos, tail_pos, d)

    print("Tail visited: ", np.count_nonzero(grid), " times")


    # Part 2
    grid = make_grid(grid_size)
    pos = [[start, start] for _ in range(10)]
    grid[start][start] = 1

    for d in data:
        move_head_tail_longer(grid, move=d, pos=pos)

    print("Tail visited: ", np.count_nonzero(grid), " times")


if __name__ == "__main__":
    # main("./2022/day9/input/input_small.txt")
    main("./2022/day9/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")