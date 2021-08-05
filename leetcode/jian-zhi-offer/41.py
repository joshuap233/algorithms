# https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
# 剑指 Offer 41. 数据流中的中位数
from bisect import insort
from heapq import heappop, heappush


class MedianFinder:
    """
        直接过了就离谱
        需要注意的是,中位数为 len(array)//2 -1 与 len(array)//2
    """

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        insort(self.array, num)

    def findMedian(self) -> float:
        ll = len(self.array)
        if ll % 2 == 0:
            return (self.array[ll // 2] + self.array[ll // 2 - 1]) / 2
        return self.array[ll // 2]


class MedianFinder1:
    """
        使用两个堆
            每次插入后,必须保证
            最大堆存储小的一半数值
            最小堆存储大的一半数值
        方法:
           需要插入到最小堆时,先将元素插入最大堆,然后将最大堆堆顶元素插入
           最小堆
    """

    def __init__(self):
        self.max = []  # 最小堆
        self.min = []  # 最大堆

    def addNum(self, num: int) -> None:
        if len(self.max) >= len(self.min):
            # self.min 元素+1,当两个堆元素总个数为奇数时,中位数在 min 中
            heappush(self.max, -num)
            # 将最小值存入 self.max, 保证 self.max 存的是较小的一半
            heappush(self.min, -heappop(self.max))
        else:
            heappush(self.min, num)
            heappush(self.max, -heappop(self.min))

    def findMedian(self) -> float:
        ll = len(self.max) + len(self.min)
        if ll % 2 == 0:
            return (self.min[0] - self.max[0]) / 2
        return self.min[0]


s = MedianFinder1()
s.addNum(1)
s.addNum(2)
s.addNum(3)
s.findMedian()
