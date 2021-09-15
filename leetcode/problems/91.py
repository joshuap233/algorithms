# https://leetcode-cn.com/problems/decode-ways/
# 91. 解码方法
from functools import lru_cache


class Solution:
    """
        吐了.....一堆边界情况
    """

    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(left: int) -> int:
            if left < len(s) and s[left] == '0':
                return 0
            if left >= len(s) - 1:
                return 1

            ret = dfs(left + 1)
            if '0' < s[left:left + 2] <= '26':
                ret += dfs(left + 2)
            return ret

        return dfs(0)


class Solution1:
    """
        青蛙跳台阶问题(一次可以跳一阶或两阶),进阶版..
        面向用例编程......
    """

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        a, b = 1, 1
        for i in range(1, len(s)):
            tmp = 0
            if s[i] != '0':
                tmp += b
            if s[i - 1] != '0' and '0' < s[i - 1:i + 1] <= '26':
                tmp += a
            a, b = b, tmp
        return b


s = Solution1()
print(s.numDecodings("2101"))
