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


class Solution1:
    """
        O(n) 时间复杂度, O(1) 空间复杂度
    """
    def findRepeatNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            v = nums[i]
            while v != i and nums[v] != v:
                nums[i], nums[v] = nums[v], nums[i]
                v = nums[i]

            if v != i:
                return v
            i += 1


s = Solution1()
s.findRepeatNumber([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 11])
