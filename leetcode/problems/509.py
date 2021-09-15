# https://leetcode-cn.com/problems/fibonacci-number/
# 509. 斐波那契数


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
