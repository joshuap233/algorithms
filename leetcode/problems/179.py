# https://leetcode-cn.com/problems/largest-number/

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, v in enumerate(nums):
            nums[i] = str(v)

        def cmp(k1: str, k2: str):
            s1 = k1 + k2
            s2 = k2 + k1
            return 1 if s2 > s1 else -1

        nums.sort(key=cmp_to_key(cmp))
        res = ''.join(nums).lstrip('0')
        return res if res != '' else '0'
