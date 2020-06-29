# 买卖股票的最佳时机 II


class Solution:

    def maxProfit(self, prices) -> int:
        return self.calculate(prices)

    # 找出上升序列
    def calculate(self, prices) -> int:
        start = 0
        profit = 0
        for index, item in enumerate(prices):
            if self.array_has_next(prices, index) and item < prices[index + 1]:
                continue
            else:
                profit += (item - prices[start])
                start = index + 1
        return profit

    @staticmethod
    def array_has_next(array, index):
        return index != len(array) - 1


s = Solution()
# print(s.maxProfit([3, 2, 6, 5, 0, 3]))
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
