# https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
# 剑指 Offer 15. 二进制中1的个数


class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        return s.count('1')


class Solution1:
    def hammingWeight(self, n: int) -> int:
        # 注意负数的处理
        b = abs(n)
        i = 0
        while b:
            if b & 1:
                i += 1
            b >>= 1
        return i


