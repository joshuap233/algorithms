from typing import List
from test import random_lists
import unittest

"""
    1. 挑选基准值：从数列中挑出一个元素，称为“基准”（pivot），

    2. 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，
       所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。
       在这个分割结束之后，对基准值的排序就已经完成，

    3. 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值
       元素的子序列排序。
"""


def get_pivot1(nums: List[int], left: int, right: int):
    """选用第一个元素为枢纽"""
    return left


def get_pivot2(nums: List[int], left: int, right: int):
    """三数中值分割法"""
    mid = (left + right) // 2
    if nums[left] > nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]
    if nums[mid] > nums[right]:
        nums[mid], nums[right] = nums[right], nums[mid]
    if nums[left] > nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]
    return mid


def partition(nums: List[int], left: int, right: int) -> int:
    """原地分割"""
    pivot = get_pivot2(nums, left, right)
    p = nums[pivot]
    nums[left], nums[pivot] = nums[pivot], nums[left]
    while left < right:
        while left < right and nums[right] >= p:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= p:
            left += 1
        nums[right] = nums[left]
    # 最终 left 会 right 重合
    nums[right] = p
    return right


def quickSort(nums: List[int]):
    def sort(left: int, right: int):
        if left >= right:
            return
        pivotIdx = partition(nums, left, right)
        sort(left, pivotIdx - 1)
        sort(pivotIdx + 1, right)

    sort(0, len(nums) - 1)
    return nums


def three_way_partition(nums: List[int], left: int, right: int) -> int:
    """
        三路排序,将等于枢纽的值放到中间,
        可以用来解决荷兰旗问题(leetcode 颜色分类)
        比二路排序多一个指针
    """
    pivot = get_pivot2(nums, left, right)
    p = nums[pivot]

    i = left
    while i <= right:
        if nums[i] > p:
            while i < right and nums[right] > p:
                right -= 1
            nums[i], nums[right] = nums[right], nums[i]
        if nums[i] < p:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        i += 1


class TestQuickSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = quickSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


if __name__ == '__main__':
    unittest.main()
