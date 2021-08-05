# 对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。
#
# 以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。
# https://leetcode-cn.com/problems/smallest-good-base/

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)


