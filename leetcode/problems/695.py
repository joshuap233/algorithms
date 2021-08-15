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
        maxi = 0
        mx, my = len(grid[0]), len(grid)

        def dfs(x: int, y: int):
            nonlocal cnt, maxi
            if 0 <= x < mx and 0 <= y < my and grid[y][x] == 1:
                cnt += 1
                grid[y][x] = 0
                dfs(x, y + 1)
                dfs(x, y - 1)
                dfs(x + 1, y)
                dfs(x - 1, y)

        cnt = 0
        for y, array in enumerate(grid):
            for x, v in enumerate(array):
                if v == 1:
                    dfs(x, y)
                    maxi = max(maxi, cnt)
                    cnt = 0
        return maxi


s = Solution()
s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
