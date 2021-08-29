from collections import deque


class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack2.pop()

    def peek(self) -> int:
        self.move()
        return self.stack2[-1]

    def empty(self) -> bool:
        if self.stack or self.stack2:
            return False
        return True

    def move(self) -> None:
        if not self.stack2:
            while self.stack:
                self.stack2.append(self.stack.pop())
