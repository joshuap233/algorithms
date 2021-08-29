from typing import List


def insertionSort(nums: List[int]) -> List[int]:
    """
        最佳情况时间复杂度: O(n)
        最差情况时间复杂度 O(n*n)

        插入排序由 N-1 趟排序组成,对于 P=1 趟到
        P=N-1 趟,插入排序保证从位置 0 - P 的元素为
        已排序状态
        向前插入(交换)
    """
    n = len(nums)
    for i in range(1, n):
        for j in reversed(range(i)):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                break
    return nums


