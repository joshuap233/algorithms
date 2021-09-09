# https://leetcode-cn.com/problems/contiguous-array/
# 525. 连续数组

from typing import List


class Solution:
    """
    `   将 nums 中的 0 换成 1,
        问题变成前缀和问题
    """

    def findMaxLength(self, nums: List[int]) -> int:
        for i, v in enumerate(nums):
            if v == 0:
                nums[i] = -1

        s = {}
        Sum = 0
        maxi = 0
        for i, v in enumerate(nums):
            Sum += v
            if Sum == 0:
                maxi = i + 1
            else:
                if Sum in s:
                    maxi = max(maxi, i - s[Sum])
                else:
                    s[Sum] = i
        return maxi


class Solution1:
    """
    `   上面代码的优化
    """

    def findMaxLength(self, nums: List[int]) -> int:
        s = {}
        maxi = Sum = 0
        for i, v in enumerate(nums):
            v = v or -1
            Sum += v
            if Sum == 0:
                maxi = i + 1
            else:
                if Sum in s:
                    maxi = max(maxi, i - s[Sum])
                else:
                    s[Sum] = i
        return maxi


s = Solution()
s.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1])
