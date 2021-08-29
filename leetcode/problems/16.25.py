# 面试题 16.25. LRU 缓存
# https://leetcode-cn.com/problems/lru-cache-lcci/
from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key, last=True)
            return self[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self:
            self[key] = value
            self.move_to_end(key)
        else:
            if len(self) == self.capacity:
                self.popitem(last=False)
            self[key] = value
