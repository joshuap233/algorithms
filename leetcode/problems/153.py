# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
# 153. 寻找旋转排序数组中的最小值
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


s = Solution()
print(s.findMin([11, 13, 15, 17]))
