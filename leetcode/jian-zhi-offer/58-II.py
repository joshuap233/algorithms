# https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
# 剑指 Offer 58 - II. 左旋转字符串


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


class Solution1:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        while n:
            s.append(s.pop(0))
            n -= 1
        return ''.join(s)


class Solution2:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = [''] * len(s)

        for i in range(n, n + len(s)):
            res[i - n] = s[i % len(s)]
        return ''.join(res)

s = Solution2()
print(s.reverseLeftWords('abcdefg', 2))
