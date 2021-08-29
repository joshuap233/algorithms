# https://leetcode-cn.com/problems/spiral-matrix-ii/
# 59. 螺旋矩阵 II
from typing import List


class Solution:
    """设置 left, right, up, down 四个边界"""
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        end = n * n
        k = 1
        left, right, up, down = 0, n - 1, 0, n - 1
        while k <= end:
            for x in range(left, right + 1):
                res[up][x] = k
                k += 1
            up += 1

            for y in range(up, down + 1):
                res[y][right] = k
                k += 1
            right -= 1

            for x in reversed(range(left, right + 1)):
                res[down][x] = k
                k += 1
            down -= 1

            for y in reversed(range(up, down + 1)):
                res[y][left] = k
                k += 1
            left += 1
        return res


s = Solution()
print(s.generateMatrix(4))
