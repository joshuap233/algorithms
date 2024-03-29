# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 似乎剑指 offer 有这题....
# 34. 在排序数组中查找元素的第一个和最后一个位置

from typing import List


class Solution:
    """
        实现时间复杂度为 O(log n)
        那就二分....二分模版我都能默写出来了....这题需要改一下
        看样子是要两次二分?
        两次二分, 二分接收一个参数 low:
        下面时和普通二分不同的部分
            if nums[mid] == target:
                if low:
                    right = mid - 1
                else:
                    left = mid + 1
        return left if low else right


        最后判断:
        if ll >= len(nums) or nums[ll] != target:
            return [-1, -1]

    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(low: bool):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    if low:
                        right = mid - 1
                    else:
                        left = mid + 1
            return left if low else right

        ll = binary_search(True)
        if ll >= len(nums) or nums[ll] != target:
            return [-1, -1]

        rr = binary_search(False)
        return [ll, rr]


class Solution1:
    """
        比上面的好理解一点
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(ll: int, rr: int, low: bool):
            while ll <= rr:
                mid = (ll + rr) // 2
                if nums[mid] > target:
                    rr = mid - 1
                elif nums[mid] < target:
                    ll = mid + 1
                else:
                    if low:
                        if mid == 0 or nums[mid - 1] != target:
                            return mid
                        rr = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid + 1] != target:
                            return mid
                        ll = mid + 1
            return -1

        res = [-1, -1]
        res[0] = binary_search(0, len(nums) - 1, True)
        res[1] = binary_search(0, len(nums) - 1, False)
        return res
