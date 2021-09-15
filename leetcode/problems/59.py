# https://leetcode-cn.com/problems/spiral-matrix-ii/
# 59. 螺旋矩阵 II
from typing import List


class Solution:
    """
        设置 left, right, top, bottom 四个边界
        和螺旋矩阵 I 一个方法, 不过需要首先初始化一个数组然后填数
    """

    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        x = y = 0
        i = 1
        while i <= n * n:
            for x in range(left, right + 1):
                ret[y][x] = i
                i += 1
            top += 1

            for y in range(top, bottom + 1):
                ret[y][x] = i
                i += 1
            right -= 1

            for x in reversed(range(left, right + 1)):
                ret[y][x] = i
                i += 1
            bottom -= 1

            for y in reversed(range(top, bottom + 1)):
                ret[y][x] = i
                i += 1
            left += 1
        return ret


s = Solution()
print(s.generateMatrix(4))
