# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# 4. 寻找两个正序数组的中位数
from typing import List


class Solution:
    """
        O(m+n)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums2 + nums1

        # 归并
        new.sort()
        mid = len(new) // 2
        if len(new) % 2 == 0:
            return (new[mid] + new[mid - 1]) / 2
        return new[mid]


class Solution1:
    """
    O(log (m+n))
    log 的时间复杂度,且对数组结构,明显要用二分
    log 的时间复杂度,且对数组结构,明显要用二分

    这道题可以转化成寻找两个有序数组中的第 k 小的数,
    k=(m+n)/2 或 (m+n)/2+1
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


s = Solution1()
s.findMedianSortedArrays([1, 3], [2, 4])
