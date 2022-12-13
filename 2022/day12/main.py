import unittest
from typing import List

import numpy as np


def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n")


def main(fname: str) -> None:
    arr = []

    data = read_file(fname)

    for d in data:
        line = []
        for c in d:
            line.append(c)
        arr.append(line)

    array = np.array(arr)
    print(array)



if __name__ == "__main__":
    main("./2022/day12/input/input_small.txt")
    # main("./2022/day12/input/input.txt")