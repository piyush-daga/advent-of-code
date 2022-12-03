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


def main(fname: str) -> int:
    ...


if __name__ == "__main__":
    # main("./input/input_small.txt")

    unittest.main()

    # main("./input/input.txt")