# https://leetcode-cn.com/problems/combination-sum/
# 39. 组合总和
# 又是排列组合题


from typing import List


class Solution:
    """
        回溯,然后想办法去重,
        经典模板题.....回溯然后加个 left 去重
        原来是:
          for i in candidates:

        去重:
         for i in range(left, len(candidates)):
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(value: int, left: int):
            if value == target:
                res.append(nums[:])
                return

            if value > target:
                return

            for i in range(left, len(candidates)):
                v = candidates[i]
                nums.append(v)
                backtrack(value + v, i)
                nums.pop(-1)

        nums = []
        backtrack(0, 0)
        return res
