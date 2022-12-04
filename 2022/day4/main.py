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

        if e1[0] >= e2[0] and e1[1] <= e2[1]:
            fully_inclusive += 1
        elif e2[0] >= e1[0] and e2[1] <= e1[1]:
            fully_inclusive += 1



        # Section2
        if e1[0] <= e2[0] and e1[1] >= e2[0]:
            inclusive += 1
        elif e1[0] >= e2[0] and e1[1] <= e2[1]:
            inclusive += 1
        elif e1[0] >= e2[0] and e1[0] <= e2[1]:
            inclusive += 1


    print("Full inclusive:", fully_inclusive)
    print("Partially inclusive:", inclusive)

    return inclusive


if __name__ == "__main__":
    # main("./input/input_small.txt")

    unittest.main()

    # main("./input/input.txt")