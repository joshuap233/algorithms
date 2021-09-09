# https://leetcode-cn.com/problems/3sum-closest/
# 16. 最接近的三数之和
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i, v in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + v
                if abs(target - res) > abs(target - s):
                    res = s
                if s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target
        return res


class Solution1:
    """
        上面的解法多个了去重
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        le = len(nums)
        nums.sort()

        ret = float('inf')
        i = 0
        while i < le:
            ll, rr = i + 1, le - 1
            while ll < rr:
                s = nums[ll] + nums[rr] + nums[i]
                if target > s:
                    ll += 1
                elif target < s:
                    rr -= 1
                else:
                    return s

                if abs(target - s) < abs(target - ret):
                    ret = s

            p = nums[i]
            while i < le and nums[i] == p:
                i += 1
        return ret


s = Solution()
s.threeSumClosest([0, 2, 1, -3], 1)
