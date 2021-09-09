# https://leetcode-cn.com/problems/max-area-of-island/
# 695. 岛屿的最大面积


from typing import List


class Solution:
    """
        深搜
        注意需要向 4 个方向搜索, 不可省略上方
        1 0 1 1 1
        1 0 1 0 1
        1 1 1 0 1
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx, my = len(grid[0]), len(grid)

        def dfs(x: int, y: int) -> int:
            if not (0 <= x < mx and 0 <= y < my) or grid[y][x] == 0:
                return 0
            grid[y][x] = 0
            return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + 1

        maxi = 0
        for j in range(my):
            for i in range(mx):
                if grid[j][i] == 1:
                    maxi = max(maxi, dfs(i, j))
        return maxi
