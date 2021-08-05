# https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/
# 剑指 Offer 47. 礼物的最大价值

from typing import List


# 很慢
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        v = [[0] * len(grid[0]) for _ in grid]

        def recur(x, y):
            if x >= len(grid[0]) or y >= len(grid):
                return 0
            if v[y][x] != 0:
                return v[y][x]

            v[y][x] = max(grid[y][x] + recur(x + 1, y), grid[y][x] + recur(x, y + 1))
            return v[y][x]

        return recur(0, 0)


# 优化上面的递归,结果时间一样??????
# 原理是 (x,y) 的最大值为它左边的最大值 + 右边的最大值
# 广度优先搜索即可
class Solution1:
    def maxValue(self, grid: List[List[int]]) -> int:
        queue = [(0, 0)]
        dp = [[-1] * len(grid[0]) for _ in grid]

        while queue:
            x, y = queue.pop(0)
            _max = dp[y][x - 1] if x >= 1 else 0
            if y >= 1:
                _max = max(_max, dp[y - 1][x])
            dp[y][x] = _max + grid[y][x]
            if x + 1 < len(grid[0]) and dp[y][x + 1] == -1:
                queue.append((x + 1, y))
                dp[y][x + 1] = 0
            if y + 1 < len(grid) and dp[y + 1][x] == -1:
                queue.append((x, y + 1))
                dp[y + 1][x] = 0
        return dp[-1][-1]


# 优化上面的代码
class Solution2:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i, v in enumerate(grid[0]):
            for j, v1 in enumerate(grid):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[j][i] += grid[j - 1][i]
                elif j == 0:
                    grid[j][i] += grid[j][i - 1]
                else:
                    grid[j][i] += max(grid[j][i - 1], grid[j - 1][i])
        return grid[-1][-1]


s = Solution1()
print(s.maxValue([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
