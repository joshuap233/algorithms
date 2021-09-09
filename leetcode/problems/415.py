# https://leetcode-cn.com/problems/add-strings/
# 415. 字符串相加


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(f'{num1}+{num2}'))


class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        p1, p2 = len(num1) - 1, len(num2) - 1
        cur = 0
        while p1 >= 0 or p2 >= 0 or cur:
            if p1 >= 0:
                cur += int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                cur += int(num2[p2])
                p2 -= 1
            res = str(cur % 10) + res
            cur //= 10
        return res


s = Solution1()
s.addStrings("456", "77")
