# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
# 剑指 Offer 09. 用两个栈实现队列

from array import array


class Stack:
    def __init__(self):
        self.data = array('i')

    def pop(self) -> int:
        return self.data.pop(-1)

    def push(self, value: int) -> None:
        self.data.append(value)

    def empty(self) -> bool:
        return len(self.data) == 0


class CQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def appendTail(self, value: int) -> None:
        self.stack1.push(value)

    def deleteHead(self) -> int:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.empty():
            return -1
        return self.stack2.pop()

