# https://leetcode-cn.com/problems/add-strings/
# 415. 字符串相加


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(f'{num1}+{num2}'))


class Solution1:
    """
        注意遍历完成时的溢出问题:
        if overflow:
            res = '1' + res
    """

    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        overflow = 0

        res = ''
        for i in range(len(num2)):
            b = int(num1[-i - 1]) if abs(-i - 1) <= len(num1) else 0
            v = b + int(num2[-i - 1]) + overflow
            overflow = v // 10
            res = str(v % 10) + res
        if overflow:
            res = '1' + res
        return res


s = Solution1()
s.addStrings("456", "77")
