import unittest
from typing import List


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = 4
        # self.assertEqual(main("./input/input_small.txt"), exp_op)
        self.assertEqual(main("./input/input.txt"), exp_op)



def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")


def main(fname: str) -> int:
    fully_inclusive = 0
    inclusive = 0

    data = read_file(fname)
    for row in data:
        sec1, sec2 = row.split(",")
        e1 = [int(s) for s in sec1.split("-")]
        e2 = [int(s) for s in sec2.split("-")]

        # A better way
        s1 = set(list(range(e1[0], e1[1] + 1)))
        s2 = set(list(range(e2[0], e2[1] + 1)))

        if s1.issuperset(s2) or s1.issubset(s2):
            fully_inclusive += 1

        # Section2
        if s1.intersection(s2):
            inclusive += 1

    print("Full inclusive:", fully_inclusive)
    print("Partially inclusive:", inclusive)

    return inclusive


if __name__ == "__main__":
    # main("./input/input_small.txt")

    unittest.main()

    # main("./input/input.txt")