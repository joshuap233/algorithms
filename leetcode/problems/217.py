# https://leetcode-cn.com/problems/contains-duplicate/
# 217. 存在重复元素

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)
