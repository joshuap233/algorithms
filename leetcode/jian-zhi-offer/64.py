# https://leetcode-cn.com/problems/qiu-12n-lcof/
# 剑指 Offer 64. 求1+2+…+n


class Solution:
    def sumNums(self, n: int) -> int:
        return (n ** 2 + n) >> 1


class Solution1:
    # 不能用循环,使用递归代替循环
    def sumNums(self, n: int) -> int:
        if n == 0:
            return 0
        return n + self.sumNums(n - 1)
