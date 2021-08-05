from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        z, t = 0, -1
        index = 0
        while index - t <= len(nums):
            while -t <= len(nums) and nums[index] == 2 and index - t <= len(nums):
                nums[index], nums[t] = nums[t], nums[index]
                t -= 1
            if nums[index] == 0:
                nums[index], nums[z] = nums[z], nums[index]
                z += 1
            index += 1


s = Solution()
nums = [0, 1, 2]

s.sortColors(nums)
print(nums)
