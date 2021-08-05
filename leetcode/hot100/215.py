# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
# 215. 数组中的第K个最大元素

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


class Solution1:
    """'
        出这题的人就离谱,怕是不希望人直接用排序把,用堆也是 nlog2n
        内置 sort 用 c 实现,不必 Python 实现快吗???
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heapreplace
        heap = nums[:k]
        heapify(heap)
        for i in nums[k:]:
            if heap[0] < i:
                heapreplace(heap, i)
        return heap[0]


s = Solution1()
s.findKthLargest([2, 1], 2)
