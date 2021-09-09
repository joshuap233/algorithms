# https://leetcode-cn.com/problems/3sum/
# 15. 三数之和
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        le = len(nums)
        a = 0
        while a < le:
            b, c = a + 1, le - 1

            while b < c:
                v = nums[a] + nums[b] + nums[c]
                if v == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    p1, p2 = nums[b], nums[c]
                    # 去重
                    while b < c and nums[b] == p1:
                        b += 1
                    while b < c and nums[c] == p2:
                        c -= 1
                elif v < 0:
                    b += 1
                else:
                    c -= 1
            # 去重
            p = nums[a]
            while a < le and nums[a] == p:
                a += 1
        return res
