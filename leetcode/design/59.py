#   最小栈
class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.values = []

    def push(self, x: int) -> None:
        self.min = min(self.min, x)
        self.values.append(x)

    def pop(self) -> None:
        value = self.values.pop(-1)
        if value == self.min:
            if len(self.values) == 0:
                self.min = float('inf')
                return
        self.min = min(self.values)

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min

