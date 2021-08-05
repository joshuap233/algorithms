# 剑指 Offer 03. 数组中重复的数字
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/

from typing import List


# Python 访问局部变量和类属性的速度不同...
# 见 https://python3-cookbook.readthedocs.io/zh_CN/latest/c14/p14_make_your_program_run_faster.html


# 这个 44 秒
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)


# 这个 84 秒
class Solution2:
    def __init__(self):
        self.set = set()

    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in nums:
            if i in self.set:
                return i
            self.set.add(i)
