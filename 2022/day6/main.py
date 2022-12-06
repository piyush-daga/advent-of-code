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

def first_occurrence_of_non_repeats(data: str):
    result = 0
    for i, d in enumerate(data):
        # For first part
        # c = Counter(data[i: i+4])
        # For second part
        c = Counter(data[i: i+14])
        val = c.most_common(1)[0][1]
        if  val == 1:
            result = i
            break

    return result


def main(fname: str) -> None:
    data = read_file(fname)

    # For first part
    # print(first_occurrence_of_non_repeats(data) + 4)
    # For second part
    print(first_occurrence_of_non_repeats(data) + 14)


if __name__ == "__main__":
    main("./day6/input/input_small.txt")
    main("./day6/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")