# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
# 121. 买卖股票的最佳时机
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ret = 0
        for i in prices:
            ret = max(ret, i - mini)
            mini = min(mini, i)
        return ret
