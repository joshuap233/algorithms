from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        prev = None
        lens = 0
        for i in nums:
            if i == prev:
                if lens == 1:
                    nums[p] = i
                    p += 1
                    lens += 1
            else:
                prev = nums[p] = i
                lens = 1
                p += 1
        return p


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[p - 2]:
                nums[p] = nums[i]
                p += 1
        return p
