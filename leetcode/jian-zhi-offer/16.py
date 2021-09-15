# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
# 剑指 Offer 16. 数值的整数次方

# 最后处理符号
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        re = 1
        pos = True if n > 0 else False
        n = abs(n)
        while n > 1:
            if n % 2 == 1:
                re *= x
            x *= x
            n //= 2
        return x * re if pos else 1 / (x * re)
