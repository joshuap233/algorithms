# https://leetcode-cn.com/problems/minimum-size-subarray-sum/
# 209. 长度最小的子数组
import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        le = float('inf')
        ll = res = 0
        for rr in range(len(nums)):
            res += nums[rr]
            while ll <= rr and res >= target:
                le = min(le, rr - ll + 1)
                res -= nums[ll]
                ll += 1
        return 0 if math.isinf(le) else le
