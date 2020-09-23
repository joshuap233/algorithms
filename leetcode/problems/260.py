# https://leetcode-cn.com/problems/single-number-iii/

# 260. 只出现一次的数字 III
from typing import List


class Solution:
    def __init__(self):
        self.map = {}

    def singleNumber(self, nums: List[int]) -> List[int]:
        for item in nums:
            if item in self.map:
                self.map[item] += 1
            else:
                self.map[item] = 1
        return [key for key, value in self.map.items() if value == 1]
