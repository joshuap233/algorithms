# https://leetcode-cn.com/problems/multiply-strings/
# 43. 字符串相乘
from functools import reduce

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(f'{num1}*{num2}'))


class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        a = [0] * (l1 + l2)
        for i, vi in enumerate(reversed(num1)):
            cur = 0
            for j, vj in enumerate(reversed(num2)):
                cur = int(vi) * int(vj) + a[i + j] + cur
                a[i + j] = cur % 10
                cur //= 10
            a[i + l2] += cur
        return reduce(lambda x, y: str(y) + x, a, '').lstrip('0') or '0'



s = Solution1()
s.multiply("123", "456")
