# https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
# 剑指 Offer 59 - II. 队列的最大值
from collections import deque


class MaxQueue:
    """
    考虑构建一个递减列表来保存队列 所有递减的元素 ，
    递减列表随着入队和出队操作实时更新，这样队列最大元素就始终对应递减列
    表的首元素，实现了获取最大值 O(1) 时间复杂度。

    当执行入队 push_back() 时： 若入队一个比队列某些元素更大的数字 x ，
    则为了保持此列表递减，需要将双向队列 尾部所有小于 x 的元素 弹出
    """

    def __init__(self):
        self.queue = deque()
        self.queue1 = deque()  # 辅助队列

    def max_value(self) -> int:
        return self.queue1[0] if self.queue1 else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)

        queue = self.queue1
        while queue and queue[-1] < value:
            queue.pop()
        queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        ret = self.queue.popleft()
        if ret == self.queue1[0]:
            self.queue1.popleft()
        return ret
