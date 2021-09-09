# https://leetcode-cn.com/problems/coin-change-2/
# 518. 零钱兑换 II
from functools import lru_cache
from typing import List


class Solution:
    """
        注意将 for i in range(c, amount + 1): 放到外层会导致重复计算

        比如 coins = [1,2,5], amount = 5
        凑 1 有 1 种方法
        凑 2 有 2 种方法
        凑 3 有 1+2 中方法(只有两种, 1+2 与 2+1 重复)

        而 for c in coins 在外层则可以避免这个问题
    """

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[-1]

