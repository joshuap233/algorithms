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
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


s = Solution()
s.uniquePaths(3, 7)
