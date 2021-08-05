# https://leetcode-cn.com/problems/jump-game/
# 55. 跳跃游戏
from typing import List


class Solution:
    """
        元素代表可以跳跃的最大长度。
        存储最大可达索引即可
    """

    def canJump(self, nums: List[int]) -> bool:
        # 最大可达索引
        maxi = nums[0]

        j = 0
        while j <= maxi and j < len(nums):
            maxi = max(maxi, j + nums[j])
            if j == maxi and j != len(nums) - 1:
                return False
            j += 1
        return True


class Solution1:
    """
        上面的代码优化
    """

    def canJump(self, nums: List[int]) -> bool:
        # 最大可达索引
        maxi, n = 0, len(nums) - 1

        for i, v in enumerate(nums):
            maxi = max(maxi, i + v)
            if i == maxi and i != n:
                return False
        return True


s = Solution1()
print(s.canJump([1, 2, 3]))
print(s.canJump([3, 2, 1, 0, 4]))
print(s.canJump([0]))
print(s.canJump([1]))
