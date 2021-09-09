from typing import List

"""
    快速选择算法(思想与快排非常相似, 所以放到排序算法里)

    在计算机科学中，快速选择是一种从无序列表找到第 k 小(大)元素的选择算法。

    原理:
     选择枢纽 A, 将 < A 的元素放到枢纽左边, 大于 A 的元素放到枢纽右边,
     如果 右边的元素个数为 K, 那么 A 为所求元素, 否则继续递归,利用三
     数中值分割法可以消除最坏的二次情形
    
    平均时间复杂度
"""


def quickSelect(nums: List[int], k: int) -> int:
    """选择第 K 大的元素"""

    le = len(nums)

    def median(left: int, right: int):
        mid = (left + right) // 2
        if nums[left] > nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        if nums[mid] > nums[right]:
            nums[right], nums[mid] = nums[mid], nums[right]
        if nums[left] < nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]

    def select(left: int, right: int) -> int:
        median(left, right)
        pivot = nums[left]

        ll, rr = left, right
        while ll < rr:
            while ll < rr and nums[rr] >= pivot:
                rr -= 1
            nums[ll] = nums[rr]
            while ll < rr and nums[ll] < pivot:
                ll += 1
            nums[rr] = nums[ll]
        nums[rr] = pivot

        if rr + k == le:
            return nums[rr]

        if rr + k < le:
            return select(rr + 1, right)
        return select(left, rr - 1)

    return select(0, len(nums) - 1)


res = quickSelect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
print(res)
