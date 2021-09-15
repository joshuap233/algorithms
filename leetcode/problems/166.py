# 166. 分数到小数
# https://leetcode-cn.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = numerator, denominator
        ret = []
        d = {}
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            ret.append('-')

        a, b = abs(a), abs(b)
        ret.append(str(a // b))
        if a % b == 0:
            return ''.join(ret)

        ret.append('.')
        a = (a % b) * 10
        while a and a not in d:
            ret.append(str(a // b))
            d[a] = len(ret) - 1
            a = (a % b) * 10

        if a not in d:
            return ''.join(ret)
        return ''.join(ret[:d[a]] + ['('] + ret[d[a]:] + [')'])


s = Solution()
print(s.fractionToDecimal(-50, 8))
