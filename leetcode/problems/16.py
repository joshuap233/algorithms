# https://leetcode-cn.com/problems/3sum-closest/
# 16. 最接近的三数之和
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i, v in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + v
                if abs(target - res) > abs(target - s):
                    res = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target
        return res


s = Solution()
s.threeSumClosest([0, 2, 1, -3], 1)
