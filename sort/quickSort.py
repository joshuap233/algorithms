from typing import List

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


def split(nums: List[int], left: int, right: int) -> int:
    """原地分割"""
    pivot = get_pivot1(nums, left, right)
    p = nums[pivot]

    while left < right:
        while left < right and nums[right] >= p:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= p:
            left += 1
        nums[right] = nums[left]
    return right


def quickSort(nums: List[int]):
    def sort(left: int, right: int):
        if left == right:
            return
        pivotIdx = split(nums, left, right)
        sort(left, pivotIdx)
        sort(right, pivotIdx)

    sort(0, len(nums) - 1)
    return nums
