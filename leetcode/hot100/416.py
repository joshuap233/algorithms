# https://leetcode-cn.com/problems/partition-equal-subset-sum/
# 416. 分割等和子集
# 01背包问题

from typing import List


class Solution:
    """
        居然过了....
        列举所有子集,然后使用 Set 缓存和,用于剪枝
    """

    def canPartition(self, nums: List[int]) -> bool:
        Set = set()

        def recur(a1: list, s1: int, a2: list, s2: int) -> bool:
            if s1 in Set or not a1:
                return False

            if s1 == s2:
                return True

            Set.add(s1)
            for i in range(len(a1)):
                e = a1.pop(i)
                a2.append(e)

                if recur(a1, s1 - e, a2, s2 + e):
                    return True

                a1.append(a2.pop(-1))
            return False

        return recur(nums, sum(nums), [], 0)


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
