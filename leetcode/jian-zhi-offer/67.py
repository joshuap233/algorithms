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

