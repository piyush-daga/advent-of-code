from typing import Any, Dict, List

import anytree
from anytree import Node, NodeMixin, RenderTree

FOLDER = "folder"
FILE = "file"

class WNode(NodeMixin):
    def __init__(self, name, parent=None, weight=None, type=None, full_path=None) -> None:
        super(WNode, self).__init__()
        self.name = name
        self.full_path = full_path
        self.parent = parent
        self.type = type
        self.__weight = weight if (type == "file" and weight) else 0

    @property
    def weight(self) -> int:
        if self.type == "file":
            return self.__weight

        total_weight = 0
        for c in self.children:
            total_weight += c.weight

        return total_weight

    def __str__(self):
        return f"Node: {self.name=}, {self.weight=} {self.type=}"


def read_file(fname: str) -> List[str]:
    with open(fname) as fp:
        data = fp.read()

    return data.split("\n")


def render_tree(tree: WNode):
    for pre, _, node in RenderTree(tree):
        print("%s%s (%s) (%s)" % (pre, node.name, node.weight or 0, node.type))


def parse_data(line: str, tree: WNode, stack: List[str], existing: set):
    if line.startswith("$"):
        # Command incoming
        command = line.lstrip("$ ")
        # We do nothign when command starts with ls
        if command.startswith("cd"):
            dir = command.split(" ")[-1]

            if dir == "..":
                stack.pop()

                return

            stack.append(dir)

            # If we have already traversed the dir
            if dir in existing:
                return

            # If we are seeing the dir for the first time
            existing.add('/'.join(stack))

            node_path = '/'.join(stack[:-1])
            node = anytree.cachedsearch.find(tree, lambda node: node.full_path == node_path and node.type == FOLDER)
            WNode(dir, type=FOLDER, parent=node, full_path='/'.join(stack))

        return

    if line.startswith("dir"):
        return

    size, fname = line.split(" ")
    size = int(size)

    node_path = '/'.join(stack)
    node = anytree.cachedsearch.find(tree, lambda node: node.full_path == node_path and node.type == FOLDER)
    WNode(fname, parent=node, weight=size, type=FILE, full_path=node_path)


def main(fname: str) -> None:
    tree = WNode("/", full_path="/", type=FOLDER)
    stack = []
    existing = set("/")

    data = read_file(fname)

    for line in data:
        parse_data(line, tree, stack, existing)

    # render_tree(tree)

    nodes = anytree.search.findall(tree, lambda node: node.type == FOLDER and node.weight <= 100000)

    total_size = 0
    for node in nodes:
        total_size += node.weight

    total_disk = 70000000
    unused = 30000000
    available = total_disk - tree.weight

    nodes = anytree.search.findall(tree, lambda node: node.type == FOLDER and node.weight >= (unused - available))

    weights = []
    for node in nodes:
        weights.append(node.weight)

    print(sorted(weights)[0])

if __name__ == "__main__":
    main("./2022/day7/input/input_small.txt")
    main("./2022/day7/input/input.txt")

    # unittest.main()

    # main("./input/input.txt")