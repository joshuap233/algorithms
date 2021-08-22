# B + tree

class Node:
    def __init__(self, order: int):
        self.order = order
        self.keys = []


class Leaf:
    def __init__(self):
        self.vales = []
        self.keys = []


class BPlusTree:
    def __init__(self, order):
        pass
