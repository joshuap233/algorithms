# https://leetcode-cn.com/problems/house-robber/
# 198. 打家劫舍

from typing import List


class Solution:
    """
        暴力搜索的优化
        暴力搜索: 有两种选择, 且需要传递一个之前的状态(偷/不偷)
        剪枝方法: 到同一个房屋时, 搜索偷取金额大的那个

        动态规划优化:
        偷:  不偷 + 当前房屋金额
        不偷: max(不偷, 偷)
    """
    def rob(self, nums: List[int]) -> int:
        # 0 偷
        dp = [[0] * 2 for _ in nums]
        dp[0][0] = nums[0]

        for i in range(1, len(nums)):
            dp[i][0] = dp[i - 1][1] + nums[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
        return max(dp[-1][0], dp[-1][1])


class Solution1:
    """
        上面方法的优化,由于只需要直到上一个房屋的金额与上上个的金额
        只需要存两个数即可(滚动数组)
    """

    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in nums:
            a, b = b, max(b, a + i)
        return b
