# https://leetcode-cn.com/problems/unique-paths/
# 62. 不同路径


class Solution:
    """"
        这题怎么这么眼熟啊......
        找到了: https://leetcode-cn.com/problems/minimum-path-sum/
        最小路径和
        回溯绝对超时
        ....简单的 dp 题....
        当前的路径数量 = 上面的路径数量 + 左边的路径数量...
    """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for y in range(m):
            for x in range(n):
                if y >= 1 and x >= 1:
                    dp[y][x] = dp[y][x - 1] + dp[y - 1][x]
                elif y >= 1:
                    dp[y][x] = dp[y - 1][x]
                elif x >= 1:
                    dp[y][x] = dp[y][x - 1]
        return dp[-1][-1]


s = Solution()
s.uniquePaths(3, 7)
