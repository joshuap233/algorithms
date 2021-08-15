# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# 剑指 Offer 04. 二维数组中的查找

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        x, y = len(matrix[0]) - 1, 0
        yEnd = len(matrix) - 1

        while x >= 0 and y <= yEnd:
            value = matrix[y][x]
            if target == value:
                return True
            elif target > value:
                y += 1
            else:
                x -= 1
        return False


class Solution1:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        x, y = len(matrix[0]) - 1, 0

        while x >= 0 and y < len(matrix):
            if target > matrix[y][x]:
                y += 1
            elif target < matrix[y][x]:
                x -= 1
            else:
                return True
        return False


s = Solution1()
s.findNumberIn2DArray(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
