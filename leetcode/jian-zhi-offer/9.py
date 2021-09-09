# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
# 剑指 Offer 09. 用两个栈实现队列

from array import array


class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)

    def deleteHead(self) -> int:
        if not (self.s1 or self.s2):
            return -1

        if not self.s2:
            self.s2 = self.s1[::-1]
            self.s1 = []
        return self.s2.pop(-1)
