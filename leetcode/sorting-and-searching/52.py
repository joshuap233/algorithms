# 合并两个有序数组
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        self.remove_end_zero(nums1, m)
        self.remove_end_zero(nums2, n)
        nums1.extend(nums2)
        nums1.sort()

    @staticmethod
    def remove_end_zero(array: list, length: int):
        while len(array) > length:
            array.pop(length)
