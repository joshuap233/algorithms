# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# 300. 最长递增子序列
from typing import List
from functools import lru_cache


class Solution:
    """ dfs """

    def lengthOfLIS(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(p: int) -> int:
            maxi = 1
            for j in range(p + 1, len(nums)):
                if nums[p] < nums[j]:
                    maxi = max(maxi, dfs(j) + 1)
            return maxi

        ret = 0
        for i in range(len(nums)):
            ret = max(ret, dfs(i))

        return ret


class Solution1:
    """
        你可以设计时间复杂度为 O(n2) 的解决方案吗？

        深搜的优化, 深搜从后向前计算长度, 使用 lru 缓存,
        下面的算法从前向后计算
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maxi = 0
        for i, v in enumerate(nums):
            for j in range(i):
                if nums[j] < v:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxi = max(maxi, dp[i])
        return maxi


s = Solution()
s.lengthOfLIS([0, 1, 0, 3, 2, 3])
