# 191. 位1的个数
# https://leetcode-cn.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        num = bin(n)
        return num.count('1')
