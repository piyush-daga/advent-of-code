import unittest
from typing import List


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = ...
        self.assertEqual(main("./input/input_small.txt"), exp_op)



def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")

def unique_digits_in_op(op: str) -> int:
    result = 0

    for token in op.split(" "):
        size = len(token)
        if size in [2, 4, 3, 7]:
            # print(token, sep=" ")
            result += 1

    # print()
    return result

def main(fname: str) -> None:
    data = read_file(fname)
    
    uniq_ops = 0
    for d in data:
        ip, op = d.split(" | ")
        uniq_ops += unique_digits_in_op(op)
    
    print(uniq_ops)


# PArt 2: 1/ Create a mapping for all the digits when correct, using numbers


if __name__ == "__main__":
    # main("./2021/day8/input/input_small.txt")
    main("./2021/day8/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")