# https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
# 剑指 Offer 31. 栈的压入、弹出序列

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while popped:
            e = popped.pop(0)

            if stack and e == stack[-1]:
                stack.pop(-1)
            elif e in pushed:
                i = pushed.index(e)
                stack.extend(pushed[:i])
                pushed = pushed[i + 1:]
            else:
                return False
        return True


class Solution1:
    """上面代码优化"""

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for e in pushed:
            stack.append(e)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
