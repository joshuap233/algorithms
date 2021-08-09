# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 309. 最佳买卖股票时机含冷冻期

from typing import List


class Solution:
    """
        有三种状态: 持有股票,不持有股票(不在冷冻期),不持有(在冷冻期)
        dp[i][0] -> 当前持有股票
        dp[i][1] -> 当前不持有股票
        dp[i][2] -> 卖掉了前面的股票,后一天不能买入
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1, n):
            p, v = dp[i - 1], prices[i]
            dp[i][0] = max(p[0], p[1] - v)
            dp[i][1] = max(p[1], p[2])
            dp[i][2] = p[0] + v
        return max(dp[-1])


s = Solution()
s.maxProfit([1, 2, 3, 0, 2])
