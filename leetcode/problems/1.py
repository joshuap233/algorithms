# https://leetcode-cn.com/problems/two-sum/
# 1. 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if value + nums[j] == target:
                    return [i, j]
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [i, d[target - v]]
            d[v] = i
        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
