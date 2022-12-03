import unittest
from collections import defaultdict
from typing import List


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = 70
        self.assertEqual(main("./input/input_small.txt"), exp_op)



def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")


def main(fname: str) -> int:
    result = 0

    data = read_file(fname)

    priority = {
        chr(c):i  for i, c in enumerate(range(97, 123), start=1)
    }
    priority.update({chr(c): i for i, c in enumerate(range(65, 91), start=27)})

    for d in data:
        first, second = d[: len(d)//2], d[(len(d)//2): ]
        result += priority[set(first).intersection(set(second)).pop()]

    print(f"Result of part 1: {result}")

    # Part 2
    result = 0
    i = 0

    while i < len(data) - 2:
        result += priority[set(data[i]).intersection(set(data[i + 1])).intersection(set(data[i + 2])).pop()]
        i += 3

    print("Result of part 2: ", result)

    return result


if __name__ == "__main__":
    main("./input/input_small.txt")
    # unittest.main()

    # main("./input/input.txt")