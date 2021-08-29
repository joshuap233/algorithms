# https://leetcode-cn.com/problems/find-peak-element/
# 162. 寻找峰值

from typing import List


class Solution:
    """O(n), 找最大值即可"""

    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))


class Solution1:
    """
        O(n*logN)
        玄学编程.....,
        总之如果 nums[mid] < nums[mid + 1]
        那么 >= num[mid+1] 的部分必然有峰值
        (因为找峰值就是找局部最大值)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
