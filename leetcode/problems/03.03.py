# https://leetcode-cn.com/problems/stack-of-plates-lcci/
# 面试题 03.03. 堆盘子
from collections import deque
from typing import List


class StackOfPlates:
    """
        进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。
        注意: 这题有 0 这种阴间数据, 行!
    """

    def __init__(self, cap: int):
        self.cap = cap
        self.stack: List[List[int]] = []

    def push(self, val: int) -> None:
        if self.cap !=0:
            if not self.stack or len(self.stack[-1]) == self.cap:
                self.stack.append([])
            self.stack[-1].append(val)

    def pop(self) -> int:
        if self.stack:
            e = self.stack[-1].pop()
            if not self.stack[-1]:
                self.stack.pop()
            return e
        return -1

    def popAt(self, index: int) -> int:
        if index < len(self.stack):
            s = self.stack[index]
            e = s.pop()
            if not s:
                self.stack.pop(index)
            return e
        return -1
