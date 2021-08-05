# https://leetcode-cn.com/problems/single-number/
# 136. 只出现一次的数字

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums, 0)
