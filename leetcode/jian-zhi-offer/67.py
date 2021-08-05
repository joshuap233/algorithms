# https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/
# 剑指 Offer 67. 把字符串转换成整数

# 字符串有一个 isdigit 方法与 isspace 方法
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，
# 这些字符可以被忽略，它们对于函数不应该造成影响。
# 注意,没有小数点
class Solution:
    def strToInt(self, s: str) -> int:
        res = 0
        s = s.lstrip()
        sign = 1
        if s and s[0] in '-+':
            if s[0] == '-':
                sign = -1
            s = s[1:]

        for i in s:
            if not ('0' <= i <= '9'):
                break
            res = res * 10 + ord(i) - ord('0')

        res *= sign
        if res > (2 << 30) - 1:
            return (2 << 30) - 1

        if res < -(2 << 30):
            return -(2 << 30)
        return res


# 自动机做法:
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Solution1:
    class Automaton:
        def __init__(self):
            self.state = 'start'
            self.sign = 1
            self.ans = 0
            self.table = {
                'start': ['start', 'signed', 'in_number', 'end'],
                'signed': ['end', 'end', 'in_number', 'end'],
                'in_number': ['end', 'end', 'in_number', 'end'],
                'end': ['end', 'end', 'end', 'end'],
            }

        def get_col(self, c):
            if c.isspace():
                return 0
            if c == '+' or c == '-':
                return 1
            if c.isdigit():
                return 2
            return 3

        def get(self, c):
            self.state = self.table[self.state][self.get_col(c)]
            if self.state == 'in_number':
                self.ans = self.ans * 10 + int(c)
                self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
            elif self.state == 'signed':
                self.sign = 1 if c == '+' else -1

    def myAtoi(self, str: str) -> int:
        automaton = self.Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans
