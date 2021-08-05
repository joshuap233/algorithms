# https://leetcode-cn.com/problems/lru-cache/
# 146. LRU 缓存机制
# Python 有个 collections.OrderedDict

from typing import Dict
from collections import OrderedDict


class Node:
    def __init__(self, value: int, key: int):
        self.value: int = value
        self.key: int = key
        self.next: 'Node' = self
        self.prev: 'Node' = self


class LRUCache:
    """
        双向链表 + 哈希表
    """

    def __init__(self, capacity: int):
        self.length = capacity
        self.cache: Dict[int, Node] = {}
        # 双向循环链表
        self.lru: Node = Node(0, 0)

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self.delete(node)
            self.update(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self.delete(node)
        else:
            if self.length == len(self.cache):
                d = self.lru.next
                self.delete(d)
                del self.cache[d.key]
            node = Node(value, key)
            self.cache[key] = node
        self.update(node)

    def delete(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def update(self, node: Node):
        node.next = self.lru
        node.prev = self.lru.prev

        self.lru.prev.next = node
        self.lru.prev = node


class LRUCache1(OrderedDict):
    """上面的快一点..."""
    def __init__(self, capacity: int):
        super().__init__()
        self.length = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self[key] = value
            self.move_to_end(key)
        else:
            if len(self) == self.length:
                self.popitem(False)
            self[key] = value
