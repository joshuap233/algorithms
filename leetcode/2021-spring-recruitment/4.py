from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums2 + nums1
        # python3 的 sort 使用 timesort
        # Timsort 是一种混合稳定的排序算法，源自归并排序和插入排序
        # 或者手写归并两个排序数组
        new.sort()
        length = len(new)
        if length == 0:
            return 0
        mid = length // 2
        return new[mid] if length % 2 != 0 else (new[mid] + new[mid - 1]) / 2


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums2 + nums1
        # python3 的 sort 使用 timesort
        # Timsort 是一种混合稳定的排序算法，源自归并排序和插入排序
        # 或者手写归并两个排序数组
        new.sort()
        length = len(new)
        if length == 0:
            return 0
        mid = length // 2
        return new[mid] if length % 2 != 0 else (new[mid] + new[mid - 1]) / 2


s = Solution()
print(s.findMedianSortedArrays([2], []))
