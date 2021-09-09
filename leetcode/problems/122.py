# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# 122. 买卖股票的最佳时机 II
from typing import List


class Solution:
    """
        暴力搜索的优化
        暴力搜索: 存在持有与不持有股票两种状态
        持有:
            1. 卖出股票
            2. 继续持有
        不持有:
            1. 买入股票
            2. 继续不持有
        递归搜索到最后一支股票, 计算最大值


        状态: 1. 不持有 -> 不持有
             2.  持有 -> 不持有

             3.  持有 -> 持有
             3.  不持有 -> 持有
           状态 1.2 取最大值, 因为状态都是不持有, 搜索方向相同
           同理 3.4 取最大值

        可以用动态规划来优化搜索Z

    """

    def maxProfit(self, prices: List[int]) -> int:
        # 持有/不持有
        dp = [[0] * 2 for _ in prices]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            v = prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - v)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + v)

        return dp[-1][1]


s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
