# https://leetcode-cn.com/problems/power-of-two/
# 231. 2 的幂
import math


class Solution:
    """2的幂只有最高位为 1(二进制)"""

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1


class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1) == 0)
