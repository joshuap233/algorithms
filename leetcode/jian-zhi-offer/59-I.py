# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/
# 剑指 Offer 59 - I. 滑动窗口的最大值

from collections import deque
from typing import List


class Solution:
    """
    将值依次存入堆中,一次获取最大值,
    堆中存入 (值,值的索引)
    解决的问题:
        1. 最大值 a 从堆中 pop, 已经不再堆中, 但依然在窗口中,
        下一个最大值依然为 a,因此,需要比较窗口左边界的索引与上次 pop
        的最大值

        2.从堆中 pop 的值不在窗口中,因此需要一直 pop 直到最大值在窗口中
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappop, heappush
        res = []
        left, right = 0, 0
        heap = []
        while right < k - 1:
            heappush(heap, (-nums[right], right))
            right += 1

        e, i = float('inf'), 0
        while right < len(nums):
            heappush(heap, (-nums[right], right))

            if i < left or e > -nums[right]:
                e, i = heappop(heap)
                while i < left:
                    e, i = heappop(heap)

            res.append(-e)
            right += 1
            left += 1
        return res


class Solution1:
    """
    上面代码优化
    不直接 pop 最大值而是直接访问堆的最大值(第一个元素)
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappop, heappush, heapify
        if k == 0:
            return []

        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapify(q)

        # 堆的根为第一个元素
        res = [-q[0][0]]
        for i in range(k, n):
            heappush(q, (-nums[i], i))
            # i-k 为左边界索引 - 1
            while q[0][1] <= i - k:
                heappop(q)
            res.append(-q[0][0])

        return res


class Solution2:
    """另一种解题方法: 参考:
         59-II
        可以设置一个辅助队列
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        res = []
        queue = deque()
        left, right = 0, 0

        def pop():
            nonlocal left
            if queue[0] == nums[left]:
                queue.popleft()
            left += 1

        def put():
            nonlocal right
            value = nums[right]
            while queue and queue[-1] < value:
                queue.pop()
            queue.append(value)
            right += 1

        for i in range(k):
            put()

        res.append(queue[0])
        for i in range(k, len(nums)):
            put()
            pop()
            res.append(queue[0])
        return res


class Solution3:
    """
    优化上面的代码
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        res = []
        queue = deque()

        for right in range(k):
            while queue and queue[-1] < nums[right]:
                queue.pop()
            queue.append(nums[right])

        res.append(queue[0])
        for right in range(k, len(nums)):
            while queue and queue[-1] < nums[right]:
                queue.pop()
            queue.append(nums[right])

            if queue[0] == nums[right - k]:
                queue.popleft()
            res.append(queue[0])
        return res
