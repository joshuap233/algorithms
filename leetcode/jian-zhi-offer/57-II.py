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
        Sum = 0
        left = 1
        for right in range(left, target):
            Sum += right
            while Sum > target:
                Sum -= left
                left += 1
            if Sum == target:
                res.append(list(range(left, right + 1)))
        return res
