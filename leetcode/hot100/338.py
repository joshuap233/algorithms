# https://leetcode-cn.com/problems/counting-bits/
# 338. 比特位计数

from typing import List


class Solution:
    """
        num >=0
        要求时间复杂度为 O(n)
    """

    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]


class Solution1:
    """
        要求时间复杂度为 O(n)

        奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的
            就是最低位的 1。

        偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。

        这方法那是真的牛逼....当然不是我自己想出来的....
    """

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = dp[i - 1] + 1
        return dp
