# https://leetcode-cn.com/problems/number-of-islands/
# 200. 岛屿数量


from typing import List


class Solution:
    """
        深搜
        注意需要向 4 个方向搜索, 不可省略上方
        1 0 1 1 1
        1 0 1 0 1
        1 1 1 0 1
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        mx, my = len(grid[0]), len(grid)

        def dfs(x: int, y: int):
            if 0 <= x < mx and 0 <= y < my and grid[y][x] == '1':
                grid[y][x] = '0'
                dfs(x, y + 1)
                dfs(x, y - 1)
                dfs(x + 1, y)
                dfs(x - 1, y)

        for y, array in enumerate(grid):
            for x, v in enumerate(array):
                if v == '1':
                    dfs(x, y)
                    cnt += 1
        return cnt


s = Solution()
s.numIslands([["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"], ["1", "1", "1", "0", "1"]])
