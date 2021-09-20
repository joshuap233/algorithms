from typing import List
from test import random_lists
import unittest


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


class TestInsertionSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = insertionSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


if __name__ == '__main__':
    unittest.main()
