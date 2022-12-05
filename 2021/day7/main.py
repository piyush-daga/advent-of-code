import unittest
from collections import Counter
from typing import List


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = ...
        self.assertEqual(main("./input/input_small.txt"), exp_op)



def read_file(fname: str) -> str:
    with open(fname) as fp:
        data = fp.read().strip()

    return data

def frequency_counter(data: List[int]):
    return Counter(data)

def fuel_req_to_move(data: List[int], pos: int):
    result = 0

    for d in data:
        result += abs(d - pos)

    return result

def crab_engineering_fuel(data: List[int], pos: int):
    result = 0

    for d in data:
        steps = abs(d - pos)
        result += (steps * (steps + 1 )) // 2

    return result

def main(fname: str) -> None:
    data = read_file(fname)
    data = [int(d) for d in data.split(",")]

    # freq = frequency_counter(data)

    min = 100_000_00000_000000
    final_pos = 0
    for pos in range(max(data)):
        # fuel_req = fuel_req_to_move(data, pos)
        fuel_req = crab_engineering_fuel(data, pos)
        # print("Fuel required to move to pos: %d is %d" % (pos, fuel_req))
        if fuel_req < min:
            min = fuel_req
            final_pos = pos

    print("Fuel required to move to min pos is: ", final_pos, min)


if __name__ == "__main__":
    # main("./2021/day7/input/input_small.txt")
    main("./2021/day7/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")