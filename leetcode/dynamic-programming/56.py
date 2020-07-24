# 最大子序和
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 若前一个元素大于0,则加到当前元素上
        max_ = pre = nums[0]
        for item in nums[1:]:
            pre = (item + pre) if pre > 0 else item
            max_ = max(max_, pre)
        return max_


s = Solution()
print(s.maxSubArray([-2, -3, -1]))
