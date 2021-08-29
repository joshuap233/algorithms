from random import randint
import unittest
from heapSort import heapSort
from quickSort import quickSort
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from mergeSort import mergesort


def random_lists(mini: int = 0, maxi: int = 1000, nums: int = 1000):
    return [randint(mini, maxi + 1) for _ in range(randint(0, nums + 1))]


class TestQuickSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = quickSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


class TestHeapSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = heapSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


class TestMergeSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = mergesort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


class TestBubbleSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = bubbleSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


class TestInsertionSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = insertionSort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


if __name__ == "__main__":
    unittest.main()
