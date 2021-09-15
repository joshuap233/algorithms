from typing import List
from collections import deque


class Solution:
    """
        这题感觉是困难题...

        子矩形计数方法:
        我们对矩阵从左到右、从上到下遍历，对于每个 1，
        统计以它为右下角的子矩形的个数。
        枚举宽度, 当前宽度的子矩形数量为从右到左高度的最小值

        可以用数组存储当前 1 可以向上延伸的高度

        高度最小值可以使用单调栈存储
        下面是暴力解法
    """

    def numSubmat(self, mat: List[List[int]]) -> int:
        maxX, maxY = len(mat[0]), len(mat)
        dp = [[0] * maxX for _ in mat]
        for y in range(1, maxY):
            for x in range(maxX):
                if mat[y][x] != 0:
                    dp[y][x] = dp[y - 1][x] + mat[y][x]

        ret = 0
        for y in range(maxY):
            for x in range(maxX):
                h = dp[y][x]
                for k in range(x, -1, -1):
                    h = min(h, dp[y][k])
                    if h == 0:
                        break
                    ret += h
        return ret
