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
     修改上面的 sort, 依然是 O(m+n)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new.append(nums1[i])
                i += 1
            else:
                new.append(nums2[j])
                j += 1
        new.extend(nums1[i:] if i < len(nums1) else nums2[j:])
        mid = len(new) // 2
        if len(new) % 2 == 0:
            return (new[mid] + new[mid - 1]) / 2
        return new[mid]


class Solution2:
    """
      需要 O(log(m+n)), 很明显就是二分了...
      题目转换为求第 (m+n)/2 小的数,

      找中位数的技巧:
        分割线左边的元素个数为 (m+n+1)//2 (无论总个数奇偶)
        比如:
        1,2,| 3,4 '|' 为 分割线, 左边为 2
        1,2,| 3 左边为 2

    这题思路感觉不难
    比如两个数组,需要找第 n 个元素:

    a,b,c,d,e,f
    a1,b1,c1,d1

    找两个数组的分割线即可,
    比如当前第一个数组的分割线左边有 x 个元素,
    那么第二个数组左边就有 n-x 个元素,
    还需要满足, 两条分割线左边的元素最大值 < 右边元素最小值
    (可以看看一个条分割线,一个数组的情况)
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        x = (n1 + n2 + 1) // 2

        def binary_search(num: int) -> int:
            mid1 = 0
            left, right = 0, n1 - 1
            while left < right:
                mid1 = (left + right) // 2
                mid2 = num - mid1 - 2

                if mid2 + 1 >= n2 or nums1[mid1] > nums2[mid2 + 1]:
                    right = mid1 - 1
                elif mid2 < 0 or nums2[mid2] > nums1[mid1 + 1]:
                    left = mid1 + 1
                else:
                    break
            return max(nums1[mid1], nums2[mid1])

        a = binary_search(x)
        if (n1 + n2) % 2 != 0:
            return a

        return (a + binary_search(x - 1)) / 2


s = Solution1()
s.findMedianSortedArrays([1, 3], [2, 3])
