# https://leetcode-cn.com/problems/valid-parentheses/
# 20. 有效的括号
class Solution:
    """
        解题方法:
          辅助栈, 遇到 left 符号则压入,
          遇到 right 符号则 从栈中弹出且判断是否与left 对应
        坑, 弹出的时候栈判空,以及返回时,如果栈不为空,返回 False

    """
    def isValid(self, s: str) -> bool:
        stack = []
        left = {'(', '{', '['}
        valid = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in left:
                stack.append(i)
            elif not stack or stack.pop() != valid[i]:
                return False
        return not stack
