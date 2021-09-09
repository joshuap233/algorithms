# https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# 1293. 网格中的最短路径
from collections import deque
from typing import List


class Solution:
    """
        grid[0][0] == grid[m-1][n-1] == 0

        二维网格中的最短路问题，使用广搜
        时间复杂度 O(m*n) m,n 为网格长宽,
        存储 (x,y,curK) 三元组来剪枝(没有 k的话每个网格搜索一遍即可)
    """

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        maxY, maxX = len(grid), len(grid[0])
        if maxX == 1 and maxY == 1:
            return 0

        if maxX + maxY - 2 <= k:
            return maxY + maxX - 1

        s = {(0, 0, k)}
        q = deque([(0, 0, k)])

        i = 0
        while q:
            i += 1  # 广搜推进次数为路径长
            for _ in range(len(q)):
                x, y, r = q.popleft()
                for nx, ny in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    cx, cy = x + nx, y + ny
                    if 0 <= cy < maxY and 0 <= cx < maxX:
                        if cy == maxY - 1 and cx == maxX - 1:
                            return i

                        rem = r if grid[cy][cx] != 1 else r - 1
                        res = (cx, cy, rem)
                        if res not in s and rem >= 0:
                            s.add(res)
                            q.append(res)
        return -1


s = Solution()
ret = s.shortestPath(
    [[0]], 1
)
print(ret)
