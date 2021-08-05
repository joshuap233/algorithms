# https://leetcode-cn.com/problems/reverse-integer/
# 7. 整数反转


class Solution:
    def reverse(self, x: int) -> int:
        p = 1 if x > 0 else -1
        x = str(abs(x))
        res = int(x[::-1]) * p
        if (2 ** 31) > res >= -(2 ** 31):
            return res
        return 0


s = Solution()
print(s.reverse(1563847412))
