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


array1 = ["MinStack", "push", "push", "push", "getMin", "top", "pop", "getMin"]
array2 = [[], [-2], [0], [-1], [], [], [], []]
obj = MinStack()
for a1, a2 in zip(array1, array2):
    if a1 == 'MinStack':
        print('null')
    elif a1 == 'getMin':
        value = obj.getMin()
        print(value if value != float('inf') else 'null')
    elif a1 == 'push':
        obj.push(a2[0])
        print('null')
    elif a1 == 'pop':
        print(obj.pop())
    else:
        print(obj.top())
