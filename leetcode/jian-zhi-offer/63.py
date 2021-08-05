# https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
# 剑指 Offer 63. 股票的最大利润

from typing import List


class Solution:
    """
     记录 max 和 min
     遍历过程中更新 min, 然后用当前值 - min 计算 max 即可
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        _max = 0
        _min = prices[0]
        for i in prices:
            _max = max(_max, i - _min)
            _min = min(_min, i)
        return _max


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
