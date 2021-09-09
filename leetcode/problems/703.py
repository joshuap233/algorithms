# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/
# 703. 数据流中的第 K 大元素
from typing import List
from heapq import heapify, heappop, heapreplace, heappush


class KthLargest:
    """
        这题描述是个什么玩意???
        一个简单题错三次????
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        le = len(nums)

        while le > k:
            heappop(self.heap)
            le -= 1

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heapreplace(self.heap, val)
        return self.heap[0]


s = KthLargest(3, [0])
s.add(-1)
s.add(1)
s.add(-2)
s.add(-4)
s.add(3)
