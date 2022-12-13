import operator
import random
from pprint import pprint
from typing import List


def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read().strip()

    return data.split("\n\n")


def parse_ip(monkey_str: str):
    # {
    #     0: {
    #         "worry": [],
    #         "op": operator.mul,
    #         "val": "self | int",
    #         "test": {
    #             "condition": "",
    #             True: "",
    #             False: ""
    #         }
    #     }
    # }

    monkey_business = {}
    monkey = ""
    for index, line in enumerate(monkey_str.split("\n")):
        if index == 0:
            monkey = line.split(" ")[-1][0]
            monkey_business[monkey] = {"test": {}, "inspected": 0}
        elif index == 1:
            # TODO: What if starting items are empty
            items = [int(i) for i in line.split(": ")[-1].split(", ")]

            monkey_business[monkey]["worry"] = items
        elif index == 2:
            op = line.split(": ")[-1]
            ops = op.split(" ")[-2:]

            monkey_business[monkey]["op"] = operator.mul if ops[0] == "*" else operator.add
            monkey_business[monkey]["val"] = "self" if ops[1] == "old" else int(ops[1])
        elif index == 3:
            monkey_business[monkey]["test"]["divisible"] = int(line.split(" ")[-1])
        elif index == 4:
            monkey_business[monkey]["test"][True] = line.split(" ")[-1]
        elif index == 5:
            monkey_business[monkey]["test"][False] = line.split(" ")[-1]

    return monkey_business


def main(fname: str) -> None:
    data = read_file(fname)

    monkeys = {}
    for d in data:
        monkeys.update(parse_ip(d))
    # pprint(monkeys)

    rounds = 1000
    total_monkeys = len(monkeys)
    boredom_factor = 1

    for _ in range(rounds):
        for m in range(total_monkeys):
            m = str(m)
            for i in range(len(monkeys[m]["worry"])):
                monkeys[m]["inspected"] += 1
                old = monkeys[m]["worry"][i]
                val = monkeys[m]["val"]
                op = monkeys[m]["op"]
                div = monkeys[m]["test"]["divisible"]

                ################################################################

                # if val == "self":
                #     monkeys[m]["worry"][i] = op(old, old) # // boredom_factor
                # else:
                #     monkeys[m]["worry"][i] = op(old, val) # // boredom_factor

                # which_monkey = (monkeys[m]["worry"][i] % monkeys[m]["test"]["divisible"]) == 0

                # hint: if you need to check
                # (49 +  21) is divisible by 7

                # Then "49 % 7" + 21 is always divisible by 7
                # I was stuck and was not able to get correct answer. Then second hint worked :smile:
                # Second hint:
                # (160 + 8) is divisible by 7 and 4

                # Then 160 % (7*4)  + 8 is always divisible by 7 and 4

                ################################################################

                if op == operator.mul:
                    which_monkey = old % div == 0
                else:
                    # (old % div)
                    ...


                monkeys[monkeys[m]["test"][which_monkey]]["worry"].append(monkeys[m]["worry"][i])

            monkeys[m]["worry"] = []

        print(f"== After Round {_} ==")
        inspects = []
        for m in monkeys:
            inspect = monkeys[m]['inspected']
            inspects.append(inspect)
            print(f"Monkey {m} inspected items {inspect} times")
        # pprint(monkeys)

    # pprint(monkeys)
    inspects = []
    for m in monkeys:
        inspect = monkeys[m]['inspected']
        inspects.append(inspect)
        print(f"Monkey {m} inspected items {inspect} times")

    final = sorted(inspects, reverse=True)[:2]
    print(final[0] * final[1])

if __name__ == "__main__":
    main("./2022/day11/input/input_small.txt")
    # main("./2022/day11/input/input.txt")
