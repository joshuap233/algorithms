# https://leetcode-cn.com/problems/house-robber/
# 198. 打家劫舍

from typing import List


class Solution:
    """
        动态规划, 当前房屋编号为 i,金额为 v[i]

        当前房屋最大可偷取金额为 max(v[i-2],v[i-3]) + v
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]

        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        return max(dp[-1], dp[-2])


class Solution1:
    """
        上面方法的优化,当前房屋编号为 i, 金额为 v[i]
        当前房屋最大可偷取金额为 max(v[i-1],v[i]+v[i-2])
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


class Solution1:
    """
        上面方法的优化,由于只需要直到上一个房屋的金额与上上个的金额
        只需要存两个数即可,用切片遍历似乎更浪费空间
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        last2, last1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            last1, last2 = max(last1, last2 + nums[i]), last1
        return last1
