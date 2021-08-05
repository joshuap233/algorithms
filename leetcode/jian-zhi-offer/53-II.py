# https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/
# 剑指 Offer 53 - II. 0～n-1中缺失的数字

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1
