# https://leetcode-cn.com/problems/longest-increasing-subsequence/
# 300. 最长递增子序列
from typing import List


class Solution:
    """
        你可以设计时间复杂度为 O(n2) 的解决方案吗？
        你能将算法的时间复杂度降低到 O(n log(n)) 吗?

        我又写了个错误的解法,我的思路是遍历两遍:
        for i, v in enumerate(nums):
            cnt, prev = v,1
            for j in range(i + 1, len(nums)):
                if nums[j] > prev:
                    cnt += 1
                    prev = nums[j]
            maxi = max(maxi, cnt)

        这种写法的问题在于:
        第一遍遍历获得的子序列为
        0,1,3,
        而不是 0,1,2,3

        正确的 O(n*n) 的解法:
            创建一个数组存取 dp, dp[i] 为 i 之后(包括 i)
            的最长递增子序列
            从后向前遍历,修改 dp, 比如当前索引为 i,
            dp[i] = max(dp[k],dp[j],...) k,j 对应的元素比
            num[i] 小

        下面的写法改成正序遍历也是可以的:
            for i in range(len(nums))
                for j in range(i)
        """

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in reversed(range(n)):
            cnt = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    cnt = max(cnt, dp[j] + 1)
            dp[i] = cnt
        return max(dp)


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass


s = Solution()
s.lengthOfLIS([0, 1, 0, 3, 2, 3])
