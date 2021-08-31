from typing import Optional

"""Python 可以直接使用 heapq(最小堆)"""

"""
    堆是一颗完全二叉树, 底层上的元素从左到右填入,
    有可能例外的是底层,因此它可以用数组实现
    
    一颗高为 h 的完全二叉树右 2**h ~ 2**(h+1)-1 个节点
    
    1. 数组索引 0 不存储元素
    2. 对于任意位置 i 上的元素, 其左儿子在位置 2i 上,
        右儿子在 2i+1, 父亲在 floor(i/2)
    3. 最小堆: 最小元在根上,并且子树也是最小堆
    
插入元素 X:
    上滤: 
      在空闲位置创建一个空穴(即索引为 len(heap) 处), 如果 X 放到
    空穴而不破坏堆序,那么插入完成, 否则将空穴父节点移入空穴中,
    直到 x 能放入空穴为止
    
删除最小元素 Y:
    下滤: 
      删除一个元素后, 堆中出现空穴, 因此堆的最后一个元素 X 必须移动
    到某个地方(即索引为 len-1 的元素)。将空穴两个儿子较小的移入
    空穴，这样就把空穴下推了一层。重复该步骤直到 X 可以放入空穴
"""


class MinHeap:
    def __init__(self):
        self.e = [float('-inf')]

    def insert(self, val: int) -> None:
        self.e.append(val)

        i = len(self.e) - 1
        while self.e[i // 2] > val:
            self.e[i] = self.e[i // 2]
            i //= 2
        self.e[i] = val

    def deleteMin(self) -> Optional[int]:
        if not self:
            return None

        first, last = self.e[1], self.e[-1]
        i, child = 1, 2
        le = len(self.e)
        while child < le:
            if child + 1 < le and self.e[child + 1] < self.e[child]:
                child += 1
            if last > self.e[child]:
                self.e[i] = self.e[child]
            else:
                break
            i, child = child, child * 2
        self.e[i] = last
        self.e.pop(-1)
        return first

    def min(self) -> Optional[int]:
        return self.e[1] if len(self.e) > 1 else None

    def valid(self) -> bool:
        le = len(self.e)
        for i in range(1, le):
            v = self.e[i]
            child = i * 2
            if child < le and self.e[child] < v:
                return False
            child += 1
            if child < le and self.e[child] < v:
                return False
        return True

    def __bool__(self) -> bool:
        return len(self.e) > 1

    def __len__(self):
        return len(self.e) - 1


if __name__ == '__main__':
    from random import randint
    from plot import print_heap

    heap = MinHeap()
    for i in [2, 1, 4, 5, 10, 6, 7]:
        heap.insert(i)
        print_heap(heap.e)


    def test():
        for i in range(1000):
            print(f"==== test {i} ===")
            s = set()
            debug = []
            for _ in range(40):
                v = randint(0, 1000)

                while v in s:
                    v = randint(0, 1000)

                s.add(v)
                debug.append(v)
                heap.insert(v)
                if not heap.valid():
                    print("debug1: ", debug)
                    assert False

            debug2 = []
            for _ in range(40):
                e = heap.deleteMin()
                assert e is not None

                debug2.append(e)
                if not heap.valid():
                    print("debug1: ", debug)
                    print("debug2: ", debug2)
                    assert False
                prev = e

            print(f"==== pass {i} ===")
            print()
