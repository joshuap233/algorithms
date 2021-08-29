# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
# 718. 最长重复子数组

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxi = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                    maxi = max(maxi, dp[j][i])
        return maxi


class Solution1:
    """滚动数组"""

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        last = [0] * (m + 1)
        cur = [0] * (m + 1)
        maxi = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    cur[j] = last[j - 1] + 1
                    maxi = max(maxi, cur[j])
                else:
                    cur[j] = 0
            last, cur = cur, last
        return maxi


s = Solution1()
s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
