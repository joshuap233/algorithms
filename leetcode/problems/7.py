# https://leetcode-cn.com/problems/reverse-integer/
# 7. 整数反转


class Solution:
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        r = sign * int(''.join(reversed(str(abs(x)))))
        if r > self.MAX or r < self.MIN:
            return 0
        return int(r)


class Solution1:
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        r = 0
        p = 1 if x > 0 else -1
        x = abs(x)
        while x:
            r = r * 10 + x % 10
            x //= 10

        r *= p
        if r > self.MAX or r < self.MIN:
            return 0
        return r
