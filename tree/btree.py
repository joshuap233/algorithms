"""
阶为 M 的 B 树是一颗具有下列结构特性的树:
1. 树的根或者一片树叶，或者其儿子树在 2 和 M 之间
2. 除根外，所有非树叶节点的儿子树在 ceil(m/2) 和 m 之间
3. 所有树叶都在相同的深度上

B 树所有数据存储在树叶上
(这是《数据结构与算法 C 语言描述》对 B 树的定义)
另一种定义是 B 树内部节点允许存储数据,下面实现的是这种。
"""

from typing import List


class Node:
    def __init__(self, leaf=False):
        self.leaf: bool = leaf
        self.key: List[int] = []
        self.child: List[Node] = []


class BTree:
    def __init__(self, order):
        self.root = Node(True)
        self.order = order

    def search(self, key: int) -> bool:
        node = self.root
        while True:
            for i, k in enumerate(node.key):
                if key < k:
                    if node.leaf:
                        return False
                    node = node.child[i]
                    break
                elif key == k:
                    return True
            else:
                if node.leaf:
                    return False
                node = node.child[-1]

    def delete(self, key: int):
        pass

    def insert(self, key: int, value):
        pass
