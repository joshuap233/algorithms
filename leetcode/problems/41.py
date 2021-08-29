# https://leetcode-cn.com/problems/first-missing-positive/
# 41. 缺失的第一个正数

from typing import List


class Solution:
    """
        将值为 x 的数放到索引为 x-1 处,
        如果 x>n, 忽略
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)

        while i < n:
            v = nums[i]
            while v - 1 != i and 0 < v <= n and nums[v - 1] != v:
                nums[i], nums[v - 1] = nums[v - 1], nums[i]
                v = nums[i]
            i += 1

        for i, v in enumerate(nums):
            if i != v - 1:
                return i + 1
        return n + 1


s = Solution()
print(s.firstMissingPositive([3, 4, -1, 1]))
