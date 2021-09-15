# https://leetcode-cn.com/problems/move-zeroes/
# 283. 移动零

from typing import List


class Solution:
    """
        计数,遇到 0 计数 + 1, 非 0 则
         nums[i - cnt] = 当前值
    """
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i, v in enumerate(nums):
            if v == 0:
                zero += 1
            else:
                nums[i-zero] = v

        for i in range(zero):
            nums[-i - 1] = 0
