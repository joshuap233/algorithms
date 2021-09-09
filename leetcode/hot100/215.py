# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
# 215. 数组中的第K个最大元素

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


class Solution1:
    """堆"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heapreplace
        heap = nums[:k]
        heapify(heap)
        for i in nums[k:]:
            if heap[0] < i:
                heapreplace(heap, i)
        return heap[0]


class Solution2:
    """
    快速选择算法:
        时间复杂度 O(n)
        空间复杂度 O(logN)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        le = len(nums)

        def median(left: int, right: int):
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                nums[left], nums[mid] = nums[mid], nums[left]
            if nums[mid] > nums[right]:
                nums[right], nums[mid] = nums[mid], nums[right]
            if nums[left] < nums[mid]:
                nums[left], nums[mid] = nums[mid], nums[left]

        def select(left: int, right: int) -> int:
            median(left, right)
            pivot = nums[left]

            ll, rr = left, right
            while ll < rr:
                while ll < rr and nums[rr] >= pivot:
                    rr -= 1
                nums[ll] = nums[rr]
                while ll < rr and nums[ll] < pivot:
                    ll += 1
                nums[rr] = nums[ll]
            nums[rr] = pivot

            if rr + k == le:
                return nums[rr]

            if rr + k < le:
                return select(rr + 1, right)
            return select(left, rr - 1)

        return select(0, len(nums) - 1)


s = Solution1()
s.findKthLargest([2, 1], 2)
