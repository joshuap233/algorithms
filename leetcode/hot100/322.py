# https://leetcode-cn.com/problems/coin-change/
# 322. 零钱兑换
import math
from typing import List


class Solution:
    """
     使用 memo 记录
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def recur(value: int):
            if value == amount:
                return 0

            if value > amount:
                return -1

            if value in memo:
                return memo[value]

            mini = float('inf')
            for i in coins:
                res = recur(i + value) + 1
                if res != 0 and res < mini:
                    mini = res
            memo[value] = -1 if math.isinf(mini) else mini
            return memo[value]

        return recur(0)


class Solution1:
    """
        使用  functools.lru_cache(),
        麻了...比上面的块很多啊...
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import lru_cache

        @lru_cache(amount)
        def recur(value: int):
            if value == amount:
                return 0

            if value > amount:
                return -1

            mini = float('inf')
            for i in coins:
                res = recur(i + value) + 1
                if res != 0 and res < mini:
                    mini = res
            return -1 if math.isinf(mini) else mini

        return recur(0)


class Solution2:
    """
        面值为3元、6元、7元, 凑出 18 元
        贪心: 7+7+3 .... 明显不行

        深搜思路: 尝试 coins[0] ~ coins[-1], 如果小于 amount,
        继续搜索

        深搜优化, 总额相同时,选择使用硬币最少的那个,然后继续搜索(剪枝)

        使用动态规划优化,正向递推
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if math.isinf(dp[-1]) else dp[-1]


s = Solution()
s.coinChange([1, 2], 2)
