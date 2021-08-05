# https://leetcode-cn.com/problems/top-k-frequent-elements/
# 347. 前 K 个高频元素
# 还有一个快排的解题方法
from typing import List


class Solution:
    """
        进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

        也就是不能用排序呗....
        直接用 Counter

    这玩意(heapq.nlargest)的时间复杂度是 O(nlogn)
    def most_common(self, n=None):
        if n is None:
            return sorted(self.items(), key=_itemgetter(1), reverse=True)
        return _heapq.nlargest(n, self.items(), key=_itemgetter(1))
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        return [i[0] for i in counter.most_common(k)]


class Solution1:
    """
        时间复杂度 必须 优于 O(n log n),
        麻了, O(nlogK) 也算优于 O(nlog(n)) ....
        那就用堆吧
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        from heapq import heapreplace, heappush
        counter = Counter(nums)
        heap = []
        for v, i in counter.items():
            if len(heap) < k:
                heappush(heap, (i, v))
            elif heap[0][0] < i:
                heapreplace(heap, (i, v))
        return [i[1] for i in heap]
