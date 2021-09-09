# https://leetcode-cn.com/problems/search-a-2d-matrix/
# 74. 搜索二维矩阵
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix[0]) - 1, 0
        maxY = len(matrix)
        while x >= 0 and y < maxY:
            cur = matrix[y][x]
            if target > cur:
                y += 1
            elif target < cur:
                x -= 1
            else:
                return True
        return False


s = Solution()
s.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    , 3
)
