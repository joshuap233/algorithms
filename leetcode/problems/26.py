from typing import List


class Solution:
    """有序数组"""

    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1
        return left
