from collections import deque


class MyStack:
    """
        进阶：你能否实现每种操作的均摊时间复杂度为 O(1) 的栈？
        换句话说，执行 n 个操作的总时间复杂度 O(n) ，
        尽管其中某个操作可能需要比其他操作更长的时间。
        你可以使用两个以上的队列。
    """

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
