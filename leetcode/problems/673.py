# 673. 最长递增子序列的个数
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

from typing import List


class Solution:
    """
        看清题: 找的是个数
        给定一个未排序的整数数组，找到最长递增子序列的个数。

        时间复杂度: O(n*n)
        需要一个 lens 数组(dp 数组),存储长度,
        一个 count 数组, 存储长度对应的次数

        注意 count[i] = count[j],
        而不是 count[i] = 1
    """

    def findNumberOfLIS(self, nums: List[int]) -> int:
        lens = [1] * len(nums)  # 长度
        count = [1] * len(nums)
        maxi = 1
        count[0] = 1
        for i, v in enumerate(nums):
            for j in range(0, i):
                if v > nums[j]:
                    if lens[j] + 1 > lens[i]:
                        lens[i] = lens[j] + 1
                        count[i] = count[j]
                    elif lens[j] + 1 == lens[i]:
                        count[i] += count[j]
            maxi = max(maxi, lens[i])
        return sum(c for i, c in enumerate(count) if lens[i] == maxi)


s = Solution()
r = s.findNumberOfLIS(
    [1, 2, 4, 3, 5, 4, 7, 2]
)
print(r)
