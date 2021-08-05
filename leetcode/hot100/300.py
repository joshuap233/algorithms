# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# 300. 最长递增子序列
from typing import List


class Solution:
    """
        你可以设计时间复杂度为 O(n2) 的解决方案吗？
        你能将算法的时间复杂度降低到 O(n log(n)) 吗?

        下面的解法为 O(n*n)
        我又写了个错误的解法,我的思路是遍历两遍:
        maxi = 0
        for i, v in enumerate(nums):
            prev = v
            cnt = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > prev:
                    cnt += 1
                    prev = nums[j]
            maxi = max(maxi, cnt)
        return maxi

        这种写法的问题在于:
        [0,1,0,3,2,3]
        第一遍遍历获得的子序列为
        0,1,3,
        而不是 0,1,2,3
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


s = Solution()
s.lengthOfLIS([0, 1, 0, 3, 2, 3])
