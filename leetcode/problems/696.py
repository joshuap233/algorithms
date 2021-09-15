# https://leetcode-cn.com/problems/count-binary-substrings/
# 696. 计数二进制子串

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        a = []
        i = 0
        while i < len(s):
            cnt = 1
            while i + 1 < len(s) and s[i + 1] == s[i]:
                i += 1
                cnt += 1
            a.append(cnt)
            i += 1

        ret = 0
        for i in range(1, len(a)):
            ret += min(a[i], a[i - 1])
        return ret


class Solution1:
    """
        空间优化
    """
    def countBinarySubstrings(self, s: str) -> int:
        a, b = 0, 0
        i = 0
        ret = 0
        while i < len(s):
            a = 1
            while i + 1 < len(s) and s[i + 1] == s[i]:
                i += 1
                a += 1
            i += 1
            ret += min(a, b)
            a, b = b, a
        return ret


s = Solution1()
s.countBinarySubstrings(
    "00110011"
)
