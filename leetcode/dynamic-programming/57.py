# https://leetcode-cn.com/explore/featured/card/top-interview-questions-easy/23/dynamic-programming/57/
# 打家劫舍

from typing import List


# 时间超限....,
class Solution:
    """
    小偷只有两种选择,偷下家(+2)或者下下家(+3),
    +4则重复(+2 +2)
    """
    def __init__(self):
        self.nums = []
        self.max = 0

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.rob_index(0, 0)
        self.rob_index(1, 0)
        return self.max

    def rob_index(self, index, total):
        if index >= len(self.nums):
            self.max = max(self.max, total)
            return
        total += self.nums[index]
        self.rob_index(index + 2, total)
        self.rob_index(index + 3, total)


# 加个memo 48ms
class Solution2:
    def __init__(self):
        self.nums = []
        self.max = 0
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.rob_index(0, 0)
        self.rob_index(1, 0)
        return self.max

    def rob_index(self, index, total):
        if index >= len(self.nums):
            self.max = max(self.max, total)
            return
        if index in self.memo and total <= self.memo[index]:
            return
        self.memo[index] = max(self.memo.get(index, 0), total)
        total += self.nums[index]
        self.rob_index(index + 2, total)
        self.rob_index(index + 3, total)
