# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
# 1190. 反转每对括号间的子串


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i, v in enumerate(s):
            if v == ')':
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop(-1))
                stack.pop(-1)
                stack.extend(tmp)
            else:
                stack.append(v)
        return ''.join(stack)


s = Solution()
s.reverseParentheses("(abcd)")
