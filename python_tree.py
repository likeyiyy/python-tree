#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# code is far away from bugs with the god animal protect
# I love animals. They taste delicious.
#         ┌─┐       ┌─┐
#      ┌──┘ ┴───────┘ ┴──┐
#      │                 │
#      │       ───       │
#      │  ─┬┘       └┬─  │
#      │                 │
#      │       ─┴─       │
#      │                 │
#      └───┐         ┌───┘
#          │         │
#          │         │
#          │         │
#          │         └──────────────┐
#          │                        │
#          │      Gods Bless        ├─┐
#          │      Never Bugs        ┌─┘
#          │                        │
#          └─┐  ┐  ┌───────┬──┐  ┌──┘
#            │ ─┤ ─┤       │ ─┤ ─┤
#            └──┴──┘       └──┴──┘
import random

class Node(object):
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.height = 0
        self.key = key
        self.value = value


class Tree(object):
    def __init__(self):
        self.root = None

    def _add(self, node, key, value):
        if node.key == key:
            node.value = value
            return
        elif key < node.key:
            if node.left is None:
                node.left = Node(key, value)
                node.left.height = node.height + 1
                return
            else:
                self._add(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value)
                node.right.height = node.height + 1
                return
            else:
                self._add(node.right, key, value)

    def add(self, key, value):
        if not self.root:
            self.root = Node(key, value)
        else:
            self._add(self.root, key, value)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print node.height * '\t', node.key
            self._print_tree(node.right)

    def print_tree(self):
        self._print_tree(self.root)


if __name__ == '__main__':
    tree = Tree()
    for i in range(1, 10):
        key = random.randint(1, 100)
        value = key * '@'
        tree.add(key, value)
    tree.print_tree()
