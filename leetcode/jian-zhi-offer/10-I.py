# 剑指 Offer 10- I. 斐波那契数列
# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

class Solution:
    memo = {
        0: 0,
        1: 1
    }

    def fib(self, n: int) -> int:
        if self.memo.get(n) is None:
            self.memo[n] = (self.fib(n - 1) + self.fib(n - 2)) % 1000000007
        return self.memo[n]


class Solution2:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


s = Solution()
print(s.fib(1))
