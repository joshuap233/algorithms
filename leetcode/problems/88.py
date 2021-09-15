# 88. 合并两个有序数组
# https://leetcode-cn.com/problems/merge-sorted-array/
from typing import List


class Solution:
    """防止覆盖, 从尾部开始合并"""

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        i = len(nums1) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        if p2 >= 0:
            nums1[:i + 1] = nums2[:i + 1]
