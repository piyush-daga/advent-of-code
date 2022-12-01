from typing import List


def read_file(fname: str) -> List[List[int]]:
    result: List[List[int]] = []
    with open(fname) as fp:
        data = fp.read()

    elves = data.split("\n\n")
    for elf in elves:
        result.append([int(e) for e in elf.split("\n")])

    return result


def main(fname: str):
    all_elves = []
    data = read_file(fname)

    for d in data:
        all_elves.append(sum(d))

    top_three = sorted(all_elves, reverse=True)[:3]

    print("Top three elves total:", sum(top_three))
    print("Highest Elf value:", top_three[0])

    # print(highest)


if __name__ == "__main__":
    main("./input/input.txt")
