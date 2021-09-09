# https://leetcode-cn.com/problems/diagonal-traverse-ii/
# 1424. 对角线遍历 II

from typing import List


class Solution:
    """时间超限....."""

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ret = []
        maxX, maxY = len(max(nums, key=len)), len(nums)

        x, y = 0, 0
        sX, sY = 0, 0
        n = maxX * maxY
        for _ in range(n):
            if x < len(nums[y]):
                ret.append(nums[y][x])

            if x == maxX - 1 or y == 0:
                if sY != maxY - 1:
                    sY += 1
                else:
                    sX += 1
                x, y = sX, sY
            else:
                x += 1
                y -= 1
        return ret


class Solution1:
    """
        上面的算法的时间复杂度为 n*m , n为高, m 为最大宽
        可以优化的部分: 缺失的元素无需计算
    """

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ret = []
        
