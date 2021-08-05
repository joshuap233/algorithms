# https://leetcode-cn.com/problems/minimum-path-sum/
# 64. 最小路径和

from typing import List


class Solution:
    """
        时间超限,时间复杂度为 2**(max_x + max_y)
    """

    def minPathSum(self, grid: List[List[int]]) -> int:
        max_x, max_y = len(grid[0]) - 1, len(grid) - 1

        mini = float('inf')

        def traceback(x: int, y: int, cnt: int):
            nonlocal mini

            if x > max_x or y > max_y:
                return

            cnt += grid[y][x]

            if x == max_x and y == max_y:
                mini = min(mini, cnt)
                return
            traceback(x + 1, y, cnt)
            traceback(x, y + 1, cnt)

        traceback(0, 0, 0)
        return mini


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


s = Solution()
s.minPathSum([[1, 2, 3], [4, 5, 6]])
