# https://leetcode-cn.com/problems/jump-game/
# 55. 跳跃游戏
from typing import List


class Solution:
    """遍历过程中更新最大可达索引即可"""

    def canJump(self, nums: List[int]) -> bool:
        i = maxi = 0
        while i <= maxi and i < len(nums):
            maxi = max(maxi, i + nums[i])
            i += 1
        return i == len(nums)


class Solution1:
    """
        上面的代码优化
    """

    def canJump(self, nums: List[int]) -> bool:
        i = maxi = 0
        while i <= maxi and i < len(nums):
            maxi = max(maxi, i + nums[i])
            if maxi >= len(nums) - 1:
                return True
            i += 1
        return i == len(nums)
