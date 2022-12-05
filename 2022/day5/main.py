import unittest
from collections import defaultdict
from typing import List


class TestSuccess(unittest.TestCase):
    def test_success(self):
        exp_op = "CMZ"
        self.assertEqual(main("./2022/day5/input/input_small.txt"), exp_op)



def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read()

    return data.split("\n\n")

def create_crates(cr_ip: str):
    crates = defaultdict(list)
    lines = cr_ip.split("\n")
    length_line = len(lines[0])
    for line in lines[:-1]:
        for index, i in enumerate(range(0, length_line, 4), start=1):
            if line[i: i+3] != "   ":
                val = line[i: i+3].strip().replace("[", "").replace("]", "")
                crates[str(index)].insert(0, val)

    return crates


def action(instructions: str):
    for line in instructions.split("\n"):
        tokens = line.split(" ")
        yield {"from": tokens[3], "num": int(tokens[1]), "to": tokens[-1]}

def main(fname: str) -> str:
    cr_ip, instructions = read_file(fname)

    crates = create_crates(cr_ip=cr_ip)
    for act in action(instructions):
        # for _ in range(act["num"]):
        #     crates[act["to"]].append(crates[act["from"]].pop())

        # For part 2
        crates[act["to"]].extend(crates[act["from"]][-act["num"]:])
        del crates[act["from"]][-act["num"]:]

    result = ""
    for i in range(1, len(crates) + 1):
        result += crates[str(i)].pop()

    return result

if __name__ == "__main__":
    # print(main("./2022/day5/input/input_small.txt"))
    print(main("./2022/day5/input/input.txt"))

    # unittest.main()

    # main("./input/input.txt")