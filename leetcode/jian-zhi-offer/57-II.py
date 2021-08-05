# https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
# 剑指 Offer 57 - II. 和为s的连续正数序列

from typing import List


# 滑动窗口
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        window = []
        value = 0
        for i in range(1, target):
            value += i
            window.append(i)
            while value > target:
                e = window.pop(0)
                value -= e
            if value == target:
                res.append(window[:])
        return res


# 上面的方法优化:
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        value = 0
        left, right = 1, 0
        for i in range(1, target):
            value += i
            right += 1
            while value > target:
                value -= left
                left += 1
            if value == target:
                res.append(list(range(left, right + 1)))
        return res
