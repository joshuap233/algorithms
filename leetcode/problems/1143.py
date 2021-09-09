# https://leetcode-cn.com/problems/longest-common-subsequence/
# 1143. 最长公共子序列


class Solution:
    """
        理论上深搜也能写...?

        画个 n*m 的表格就行
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


class Solution1:
    """优化"""

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        cur = [0] * (l1 + 1)
        last = [0] * (l1 + 1)

        for y in range(1, l2 + 1):
            for x in range(1, l1 + 1):
                if text2[y - 1] == text1[x - 1]:
                    cur[x] = last[x - 1] + 1
                else:
                    cur[x] = max(last[x], cur[x - 1])
            cur, last = last, cur
        return last[-1]
