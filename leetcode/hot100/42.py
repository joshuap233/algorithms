# https://leetcode-cn.com/problems/trapping-rain-water/
# 42. 接雨水

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, 0

