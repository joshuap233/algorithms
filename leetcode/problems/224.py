# https://leetcode-cn.com/problems/basic-calculator/
# 224. 基本计算器


class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        cur, sign = 0, 1
        n = len(s)
        i = 0
        while i < n:
            v = s[i]
            if v.isdigit():
                digit = 0
                while i < n and s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                    i += 1
                i -= 1
                cur += sign * digit
            elif v == '(':
                stack.append((cur, sign))
                cur, sign = 0, 1
            elif v == ')':
                last_res, last_sign = stack.pop()
                cur = last_res + last_sign * cur
            elif v == '+':
                sign = 1
            elif v == '-':
                sign = -1
            i += 1
        return cur


s = Solution()
print(s.calculate("- (3 + (4 + 5))"))
