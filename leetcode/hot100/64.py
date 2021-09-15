# https://leetcode-cn.com/problems/minimum-path-sum/
# 64. 最小路径和

from typing import List
from functools import lru_cache


class Solution:
    """深搜"""

    def minPathSum(self, grid: List[List[int]]) -> int:
        mx, my = len(grid[0]), len(grid)

        @lru_cache(None)
        def dfs(x: int, y: int) -> int:
            if not (0 <= x < mx and 0 <= y < my):
                return 40000
            if x == mx - 1 and y == my - 1:
                return grid[-1][-1]
            return min(dfs(x + 1, y), dfs(x, y + 1)) + grid[y][x]

        return dfs(0, 0)


class Solution1:
    """
        动态规划,
        到座标 x,y 最的最小值为 min(dp[y][x-1],dp[y-1][x])
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for y, array in enumerate(grid):
            for x, v in enumerate(array):
                if x > 0 and y > 0:
                    dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + v
                elif x > 0:
                    dp[y][x] = dp[y][x - 1] + v
                elif y > 0:
                    dp[y][x] = dp[y - 1][x] + v
                else:
                    dp[y][x] = v
        return dp[-1][-1]


class Solution2:
    """
        上面的算法优化
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        maxX, maxY = len(grid[0]), len(grid)
        dp = [[40000] * (maxX + 1) for _ in range(maxY + 1)]

        dp[0][1] = 0
        for y in range(1, maxY + 1):
            for x in range(1, maxX + 1):
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + grid[y - 1][x - 1]
        return dp[-1][-1]


class Solution3:
    """滚动数组"""

    def minPathSum(self, grid: List[List[int]]) -> int:
        mx, my = len(grid[0]), len(grid)
        cur = [0] * (mx + 1)
        last = [40000] * (mx + 1)

        for y in range(my):
            for x in range(1, mx + 1):
                cur[x] = min(cur[x - 1], last[x]) + grid[y][x - 1]
            last, cur = cur, last
            cur[0] = 40000
        return last[-1]
