# https://leetcode-cn.com/problems/string-to-integer-atoi/
# 8. 字符串转换整数 (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if len(s) == 0:
            return 0

        num = "0123456789"
        f = 1
        res = 0
        if s[0] == '-':
            f = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        for i in s:
            if i in num:
                res = res * 10 + int(i)
            else:
                break
        res = res * f
        if res > (2 << 30) - 1:
            return (2 << 30) - 1
        if res < -(2 << 30):
            return -2 << 30
        return res


s = Solution()
print(s.myAtoi("2147483648"))
