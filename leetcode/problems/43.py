# https://leetcode-cn.com/problems/multiply-strings/
# 43. 字符串相乘


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(f'{num1}*{num2}'))


class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        lists = [0] * (len(num1) + len(num2))
        base = 0
        for i, vi in enumerate(reversed(num1)):
            overflow = 0
            j = 0
            for j, v in enumerate(reversed(num2)):
                lists[j + base] += int(v) * int(vi) + overflow
                overflow = lists[j + base] // 10
                lists[j + base] %= 10
            lists[j + base + 1] += overflow
            base += 1
        return ''.join([str(i) for i in reversed(lists)]).lstrip('0')


s = Solution1()
s.multiply("123", "456")
