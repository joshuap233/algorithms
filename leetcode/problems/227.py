# https://leetcode-cn.com/problems/basic-calculator-ii/
# 227. 基本计算器 II


class Solution:
    def calculate(self, s: str) -> int:
        s.replace('/', '//')
        return eval(s)


class Solution1:
    def calculate(self, s: str) -> int:
        stack = []
        res, sign = 0, 1
        i, n = 0, len(s)
        while i < n:
            v = s[i]
            if v == '+':
                pass
            elif v == '-':
                pass
            elif v == '/':
                pass
            elif v == '*':
                pass
            elif v.isdigit():
                digit = 0
                while i < n and s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                    i += 1
                i -= 1
            i += 1
        return res
