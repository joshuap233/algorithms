# 实现 strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        import re
        res = re.search(needle, haystack)
        if res:
            res = res.regs[0][0]
            return res
        return -1


s = Solution()
print(s.strStr("a", "a"))
