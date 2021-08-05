# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# 33. 搜索旋转排序数组

from typing import List


class Solution:
    """
        O(log n),二分,映射一下索引就行
        我又写了个错误的解法:
            映射索引,但找到边界的时间复杂度是 O(n)
        ???

        将数组一分为二，其中一定有一个是有序的，另一个可能是有序，
        也能是部分有序。此时有序部分用二分法查找。
        无序部分再一分为二，其中一个一定有序，另一个可能有序，
        可能无序。就这样循环.
    """

    def search(self, nums: List[int], target: int) -> int:

        def binary_search(ll: int, rr: int) -> int:
            while ll <= rr:
                m = (ll + rr) // 2
                if target > nums[m]:
                    ll = m + 1
                elif target < nums[m]:
                    rr = m - 1
                else:
                    return m
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                # mid 左边有序,搜索左边
                res = binary_search(left, mid)
                if res != -1:
                    return res
                left = mid + 1
            else:
                # mid 右边有序,搜索右边
                res = binary_search(mid, right)
                if res != -1:
                    return res
                right = mid - 1
        return -1


s = Solution()
s.search([1, 3, 5], 1)
