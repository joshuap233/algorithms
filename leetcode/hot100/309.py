# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 309. 最佳买卖股票时机含冷冻期

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = [0] * len(prices)  # 卖出
        buy = [0] * len(prices)   # 买入

        for i in prices:
            pass
