# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 持有/不持有
        dp = [[0] * 2 for _ in prices]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            v = prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - v)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + v)

        return max(dp[-1][0], dp[-1][1])


s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
