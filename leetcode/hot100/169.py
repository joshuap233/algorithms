# https://leetcode-cn.com/problems/majority-element/
# 169. 多数元素


from typing import List


class Solution:
    """
        尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

        摩尔投票法思路
        如果我们把众数记为 +1，把其他数记为 -1，将它们全部加起来，
    """

    def majorityElement(self, nums: List[int]) -> int:
        v = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == v:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    v = nums[i]
                    cnt = 1
        return v
