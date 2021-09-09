# https://leetcode-cn.com/problems/valid-parentheses/
# 20. 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        pairs = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in pairs.keys():
                li.append(pairs[i])
                continue
            if not li or i != li.pop():
                return False
        return not li
