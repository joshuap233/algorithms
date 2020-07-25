# 非递减数列
# https://leetcode-cn.com/problems/non-decreasing-array/

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for index in range(1, len(nums)):
            pre = nums[index - 1]
            curr = nums[index]
            if curr < pre:
                if changed:
                    return False
                if index - 2 >= 0:
                    if index - 2 >= 0 and nums[index - 2] < curr:
                        nums[index - 1] = curr
                    else:
                        nums[index] = pre
                changed = True
        return True


s = Solution()
print(s.checkPossibility([3, 4, 2, 3]))
