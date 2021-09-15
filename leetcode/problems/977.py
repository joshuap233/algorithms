# https://leetcode-cn.com/problems/squares-of-a-sorted-array/
# 977. 有序数组的平方


from typing import List


class Solution:
    """
        请你设计时间复杂度为 O(n) 的算法解决本问题
        双指针法
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:
        le = len(nums)
        ret = [0] * le
        ll, rr = 0, le - 1
        i = le - 1
        while ll <= rr:
            if abs(nums[ll]) >= abs(nums[rr]):
                ret[i] = nums[ll] ** 2
                ll += 1
            else:
                ret[i] = nums[rr] ** 2
                rr -= 1
            i -= 1
        return ret


s = Solution()
s.sortedSquares([-7, -3, 2, 3, 11])
