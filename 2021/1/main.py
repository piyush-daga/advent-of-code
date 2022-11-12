from typing import List


def read_inputs(fname: str) -> List[int]:
    with open(fname) as fp:
        data = fp.read()

    return [int(d) for d in data.split("\n")]


def simple_larger() -> int:
    inputs = read_inputs("./1/input/input")
    init = inputs[0]
    increased = 0

    for val in inputs:
        if val > init:
            increased += 1
        init = val

    return increased


def sliding_window_measurments() -> int:
    inputs = read_inputs("./1/input/input")
    increased = 0
    window_size = 3

    total_windows = len(inputs) - window_size

    window = 0
    previous_total = 0
    while window <= total_windows:
        current_total = sum(inputs[window: window + window_size])
        if window and current_total > previous_total:
            increased += 1

        previous_total = current_total
        window += 1

    return increased


if __name__ == "__main__":
    print(sliding_window_measurments())