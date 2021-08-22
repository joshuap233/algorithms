# 代码测试: https://leetcode-cn.com/problems/sort-an-array/
from typing import List


def mergesort(nums: List[int]) -> List[int]:
    """
        最佳情况时间复杂度: O(n*logN)
        最差情况时间复杂度 O(n*logN)
    """

    def sort(left, right) -> list:
        if left == right:
            return [nums[left]]
        mid = (left + right) // 2
        ll = sort(left, mid)
        rr = sort(mid + 1, right)

        new = []
        p2 = p1 = 0
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
