import unittest
from typing import List

import numpy as np


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = ...
        self.assertEqual(main("./input/input_small.txt"), exp_op)



def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")


def cycle_check(cycles, x) -> int:
    if cycles in [20, 60, 100, 140, 180, 220]:
        print(f"{cycles=}, {x=}, {cycles * x=}")

        return cycles * x
    return 0


def draw_crt_pixel(board, pixel, x):
    k = x + (pixel // 40) * 40

    if pixel in [k -1, k, k +1]:
        board[pixel] = '#'

        return
    board[pixel] = "."


def draw_board(board):
    print('\n'.join(['  '.join(board[i: i + 40]) for i in range(0, 240, 40)]))


def main(fname: str) -> None:
    data = read_file(fname)

    x = 1
    cycles = 0
    total = 0

    for d in data:

        if d == "noop":
            cycles += 1
            total += cycle_check(cycles=cycles, x=x)
            continue

        _, value = d.split(" ")
        value = int(value)

        cycles += 1
        total += cycle_check(cycles=cycles, x=x)

        cycles += 1
        total += cycle_check(cycles=cycles, x=x)

        x += value


    crt_board = ["" for _ in range(241)]
    x = 1
    cycles = 0

    for d in data:
        if d == "noop":
            draw_crt_pixel(crt_board, cycles, x)
            cycles += 1
            continue

        _, value = d.split(" ")
        value = int(value)

        draw_crt_pixel(crt_board, cycles, x)
        cycles += 1

        draw_crt_pixel(crt_board, cycles, x)
        cycles += 1

        x += value

    draw_board(crt_board)


if __name__ == "__main__":
    # main("./2022/day10/input/input_small.txt")
    main("./2022/day10/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")