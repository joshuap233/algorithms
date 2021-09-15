# https://leetcode-cn.com/problems/house-robber-ii/
# 213. 打家劫舍 II
from typing import List


class Solution:
    """
        这题多了个限制条件, 最后一间房与第一间房不能同时偷窃

        这题偷最后一个房屋的时候无法判断第一个房屋是否被偷,
        所以需要遍历两次(一次偷第一个房屋,一次不偷)
    """

    def rob(self, nums: List[int]) -> int:
        def Rob(left: int, right: int) -> int:
            for i in range(left + 1, right + 1):
                dp[i][0] = dp[i - 1][1] + nums[i]
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            return max(dp[right])

        if len(nums) <= 2:
            return max(nums)

        # 0 偷窃
        dp = [[0] * 2 for _ in nums]

        dp[0][0] = nums[0]
        a = Rob(0, len(nums) - 2)

        dp[1][:] = [nums[1], 0]
        b = Rob(1, len(nums) - 1)
        return max(a, b)


s = Solution()
print(s.rob([1, 2, 3, 1]))
