# https://leetcode-cn.com/problems/maximal-square/
# 221. 最大正方形

from typing import List


class Solution:
    """
        看别人题解写出来的,这方法真牛逼....
        O(n*n)

        首先，把矩阵的每一行看作一个二进制数，对于矩阵：
        比如:
            1 0 1 0 0
            1 0 1 1 1
            1 1 1 1 1
            1 0 0 1 0

        看成:
            0b10100
            0b10111
            0b11111
            0b10010

        然后第一行与之后的行与操作,结果为:
            0b10000
        然后数连续个 1 的个数,这就是最大高 h,
        宽度为相与的行数 w,正方行边长为 min(w,h)
        比如第一行与第二行相与,结果为:
           0b10100, 此时高为 1,宽为 1

        怎么求连续个 1 的个数?
            cnt = 0
            while num:
                num &= num << 1
                cnt += 1
            return cnt
    """

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nums = [int(''.join(i), base=2) for i in matrix]

        def getWidth(num: int) -> int:
            """求连续 1 的个数"""
            cnt = 0
            while num:
                num &= num << 1
                cnt += 1
            return cnt

        maxi = 0
        for i, v in enumerate(nums):
            for j in range(i, len(nums)):
                v &= nums[j]

                w = getWidth(v)
                maxi = max(maxi, min(w, j - i + 1))
        return maxi * maxi


s = Solution()
s.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
