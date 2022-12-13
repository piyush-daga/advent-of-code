import ast
import itertools
import unittest
from functools import cmp_to_key
from pprint import pprint
from typing import List, Optional


def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n\n")

def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare


def is_in_right_order(pair1: List, pair2: List):
    for left, right in itertools.zip_longest(pair1, pair2):
        # print(f"Compare {left} vs {right}")

        # Considering left finishes first
        if left is None and right is not None:
            return True

        elif left is not None and right is None:
            return False

        # If they are not of the same type
        if type(left) != type(right):
            if not isinstance(left, list):
                left = [left]
            else:
                right = [right]

        if isinstance(left, list) and isinstance(right, list):
            result = is_in_right_order(left, right)

            if result == -1:
                continue
            else:
                return result

        elif isinstance(left, int) and isinstance(right, int):
            if left == right:
                continue
            elif left < right:
                return True
            else:
                return False

    return -1


def main(fname: str) -> None:
    pairs_in_right_order = []
    pairs = read_file(fname)
    all_pairs = []

    for index, pair in enumerate(pairs, start=1):
        p1, p2 = pair.split("\n")
        p1, p2 = ast.literal_eval(p1), ast.literal_eval(p2)

        # print(f"== Pair {index} ==")
        # print(f"Compare {p1} vs {p2}")

        right_order = is_in_right_order(p1, p2)
        # print(right_order)

        if right_order:
            pairs_in_right_order.append(index)
        else:
            # print("We did not like this index: ", index)
            pass


        all_pairs.extend([p1, p2])

    all_pairs.extend([[[2]]])
    all_pairs.extend([[[6]]])

    s = sorted(all_pairs, key=cmp_to_key(make_comparator(is_in_right_order)))

    print((s.index([[2]]) + 1) * (s.index([[6]]) + 1))


    print(f"Indexes in right order: {pairs_in_right_order}")
    print(f"Sum of indexes of pairs in right order: {sum(pairs_in_right_order)}")


if __name__ == "__main__":
    # main("./2022/day13/input/input_small.txt")
    main("./2022/day13/input/input.txt")