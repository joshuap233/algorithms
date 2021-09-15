from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrace(left: int):
            ret.append(cur[:])

            if left == len(nums):
                return

            for i in range(left, len(nums)):
                if i != left and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                backtrace(i + 1)
                cur.pop(-1)

        nums.sort()
        ret = []
        cur = []
        backtrace(0)
        return ret
