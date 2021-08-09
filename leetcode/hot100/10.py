# https://leetcode-cn.com/problems/regular-expression-matching/
# 10. 正则表达式匹配


class Solution:
    """慢的确慢...好歹过了..."""

    def isMatch(self, s: str, p: str) -> bool:
        np, ns = len(p), len(s)

        def recur(s1: int, p1: int) -> bool:
            if p1 >= np:
                return s1 == ns

            # 匹配当前指针指向的字符
            first_match = s1 < ns and (s[s1] == p[p1] or p[p1] == '.')

            # 查看后方是否有 *
            if p1 + 1 < np and p[p1 + 1] == '*':
                # 1. 跳过当前字符, p+2
                # 2. 匹配当前字符, s+1,且 first_match 必须匹配
                return recur(s1, p1 + 2) or (first_match and recur(s1 + 1, p1))
            else:
                # 否则继续匹配
                return first_match and recur(s1 + 1, p1 + 1)

        return recur(0, 0)


s = Solution()
s.isMatch("aab", "c*a*b")
