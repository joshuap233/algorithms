# https://leetcode-cn.com/problems/sort-an-array/
# 912. 排序数组

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(left, right) -> list:
            if left == right:
                return [nums[left]]
            mid = (left + right) // 2
            ll = sort(left, mid)
            rr = sort(mid + 1, right)
            new = []
            p1 = 0
            p2 = 0
            while p1 < len(ll) and p2 < len(rr):
                if ll[p1] < rr[p2]:
                    new.append(ll[p1])
                    p1 += 1
                else:
                    new.append(rr[p2])
                    p2 += 1
            new.extend(ll[p1:] if p1 < len(ll) else rr[p2:])
            return new

        return sort(0, len(nums) - 1)
