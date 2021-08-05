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


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for e in popped:
            if stack and e == stack[-1]:
                stack.pop(-1)
            else:
                for i, v in enumerate(pushed):
                    if v == e:
                        stack.extend(pushed[:i])
                        pushed = pushed[i + 1:]
                        break
                else:
                    return False
        return True
