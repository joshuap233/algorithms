# 买卖股票的最佳时机
from typing import List


# 暴力解法,踩线通过
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_item = float('inf')
        max_item = {
            'index': -1,
            'value': 0
        }
        for index, item in enumerate(prices):
            # 如果是递减序列,则跳过
            if (index + 1) < len(prices) and prices[index + 1] < prices[index]:
                continue
            # 比前面已经遍历的序列中最小值还要大的,直接跳过
            if min_item < item:
                continue
            # 如果当前值的索引在已知最大值的索引之前,则直接使用已知的最大值,否则找到后面序列的最大值
            if index > max_item['index']:
                min_item = item
                max_item['value'] = 0
                for index1, item1 in enumerate(prices[index + 1:]):
                    if item1 > max_item['value'] and item1 > item:
                        max_item['index'] = index1
                        max_item['value'] = item1
            profit = max_item['value'] - item
            if profit > max_profit:
                max_profit = profit
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        pass


s = Solution()
print(s.maxProfit([2]))
