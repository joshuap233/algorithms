# https://leetcode-cn.com/problems/permutations-ii/
# 47. 全排列 II


from typing import List


class Solution:
    """
        与 剑指 Offer 38. 字符串的排列去重方法相同
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrace(left: int):
            if left == len(nums) - 1:
                ret.append(nums[:])

            d = set()
            for i in range(left, len(nums)):
                if nums[i] in d:
                    continue
                d.add(nums[i])
                nums[i], nums[left] = nums[left], nums[i]
                backtrace(left + 1)
                nums[i], nums[left] = nums[left], nums[i]

        ret = []
        backtrace(0)
        return ret
