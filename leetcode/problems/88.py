# https://leetcode-cn.com/problems/merge-sorted-array/
# 88. 合并两个有序数组
from typing import List


# 注意这题,m 是并非 nums1 长度,而是非 0 元素个数
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        for i in range(p2 + 1):
            nums1[i] = nums2[i]


# 上面的方法不如下面的快,离谱,Python 到底优化了上面?
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
