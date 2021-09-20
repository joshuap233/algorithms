from typing import List
from test import random_lists
import unittest


def bubbleSort(nums: List[int]) -> List[int]:
    """
        比较相邻的元素。如果第一个比第二个大，就交换他们两个。
        对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。
        这步做完后，最后的元素会是最大的数。
        针对所有的元素重复以上的步骤，除了最后一个。
    """
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


class TestBubbleSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = bubbleSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


if __name__ == '__main__':
    unittest.main()
