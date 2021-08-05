# https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
# 剑指 Offer 16. 数值的整数次方


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


# 最后处理符号
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        tmp_n = n
        res = x
        remain = 1
        n = abs(n)
        while n > 1:
            if n % 2 != 0:
                remain *= res
            res *= res
            n = n // 2
        return res * remain if tmp_n > 0 else 1 / (res * remain)


s = Solution2()
print(s.myPow(2.000, 10))
