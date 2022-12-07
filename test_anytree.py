from anytree import Node, NodeMixin, RenderTree


class WNode(NodeMixin):
    def __init__(self, foo, parent=None, weight=None, type=None):
        super(WNode, self).__init__()
        self.foo = foo
        self.parent = parent
        self.type = type
        self.__weight = weight if (type == "file" and weight) else 0

    @property
    def weight(self):
        if self.type == "file":
            return self.__weight

        total_weight = 0
        for c in self.children:
            total_weight += c.weight

        return total_weight


a = WNode("a", type="folder")
a0 = WNode("a0", parent=a, weight=2, type="file")
a1 = WNode("a1", parent=a, weight=3)
a1a = WNode("a1a", parent=a1, weight=5, type="file")
a2 = WNode("a2", parent=a)

# for c in a.children:
#     print(c.weight)

for pre, _, node in RenderTree(a):
    print("%s%s (%s) (%s)" % (pre, node.foo, node.weight or 0, node.type))