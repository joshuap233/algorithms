# https://leetcode-cn.com/problems/number-of-islands/
# 200. 岛屿数量


from typing import List
from collections import deque


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


class Solution1:
    """广搜"""

    def numIslands(self, grid: List[List[str]]) -> int:
        maxX, maxY = len(grid[0]), len(grid)
        cnt = 0
        q = deque()

        def bfs(x: int, y: int):
            grid[y][x] = '0'
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for nx, ny in [(0, 1), (1, 0), (0, -1), (- 1, 0)]:
                    cx, cy = x + nx, y + ny
                    if 0 <= cx < maxX and 0 <= cy < maxY and grid[cy][cx] == '1':
                        q.append((cx, cy))
                        grid[cy][cx] = '0'

        for y in range(maxY):
            for x in range(maxX):
                if grid[y][x] == '1':
                    cnt += 1
                    bfs(x, y)
        return cnt
