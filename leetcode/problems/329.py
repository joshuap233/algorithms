# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
# 329. 矩阵中的最长递增路径
from typing import List


class Solution:
    """
        用深搜 + 备忘录 ? 深搜回溯时更新备忘录
        1. 备忘录用来优化深搜
        2. 深搜外部一个大循环,保证所有单元格都被搜索过,
        3. 使用返回值来传递搜索路径长度(也可以将路径长度作为参数传递)
        4. 同一个起点的深搜, 不可能搜索到重复单元格, 比如 8 -> 9,
        由于 9 > 8 因此不可能从 9 单元格向 8 搜索

        可以用 lru_cache 代替 memo
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x: int, y: int) -> int:
            if memo[y][x] != -1:
                return memo[y][x]

            cur = matrix[y][x]
            maxi = 0
            for nx, ny in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                cx, cy = x + nx, y + ny
                if 0 <= cx < maxX and 0 <= cy < maxY and cur < matrix[cy][cx]:
                    maxi = max(maxi, dfs(cx, cy) + 1)
            memo[y][x] = maxi
            return maxi

        ret = 0
        maxX, maxY = len(matrix[0]), len(matrix)
        memo = [[-1] * maxX for _ in matrix]
        for y in range(maxY):
            for x in range(maxX):
                ret = max(ret, dfs(x, y) + 1)
        return ret


s = Solution()
res = s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
print(res)
