# https://leetcode-cn.com/problems/maximal-rectangle/
# 85. 最大矩形

from typing import List


class Solution:
    # 做法与 221 题一模一样...
    # leetcode/hot100/221.py
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nums = [int(''.join(i), base=2) for i in matrix]

        def getWidth(num: int) -> int:
            w = 0
            while num:
                num &= num << 1
                w += 1
            return w

        maxi = 0
        for i, v in enumerate(nums):
            for j in range(i, len(nums)):
                v &= nums[j]
                w = getWidth(v)
                maxi = max(maxi, w * (j - i + 1))

        return maxi
