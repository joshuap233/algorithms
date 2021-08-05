# https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
# 剑指 Offer 42. 连续子数组的最大和

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = float('-inf')
        count = 0
        for i in nums:
            count += i
            _max = max(_max, count)
            if count < 0:
                count = 0
        return _max
