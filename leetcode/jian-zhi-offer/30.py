# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
# 剑指 Offer 30. 包含min函数的栈


class MinStack:
    """
        使用两个栈,一个栈为正常的栈 a , 另一个栈 b 用来实现 O(1) 找到最小值:
        如果新增的元素 c 小于 b 顶部元素, b.push(c),
        否则 b.push(b[-1])
    """

    def __init__(self):
        self.array = []
        self.array1 = []

    def push(self, x: int) -> None:
        self.array.append(x)

        array1 = self.array1
        array1.append(x if (not array1) or array1[-1] > x else array1[-1])

    def pop(self) -> None:
        if self.array:
            del self.array[-1]
            del self.array1[-1]

    def top(self) -> int:
        return self.array[-1]

    def min(self) -> int:
        return self.array1[-1]


class MinStack1:
    """
        上面的代码优化
        仅当 辅助栈 栈顶元素 大于等于即将入栈元素时,元素入辅助栈
    """

    def __init__(self):
        self.array = []
        self.array1 = []

    def push(self, x: int) -> None:
        array1 = self.array1

        self.array.append(x)
        if not array1 or array1[-1] >= x:
            array1.append(x)

    def pop(self) -> None:
        if self.array.pop() == self.array1[-1]:
            self.array1.pop()

    def top(self) -> int:
        return self.array[-1]

    def min(self) -> int:
        return self.array1[-1]
