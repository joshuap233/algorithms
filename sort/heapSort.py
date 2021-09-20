from typing import List
from heapq import heapify, heappop
import unittest
from test import random_lists


def heapSort(nums: List[int]) -> List[int]:
    """
        最佳情况时间复杂度: O(n*logN)
        最差情况时间复杂度 O(n*logN)
    """
    new = [0] * len(nums)
    heapify(nums)
    for i in range(len(nums)):
        new[i] = heappop(nums)
    return new


class TestHeapSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = heapSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


if __name__ == '__main__':
    unittest.main()
