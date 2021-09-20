# 代码测试: https://leetcode-cn.com/problems/sort-an-array/
from typing import List
import unittest
from test import random_lists


def mergesort(nums: List[int]) -> List[int]:
    """
        最佳情况时间复杂度: O(n*logN)
        最差情况时间复杂度 O(n*logN)
    """

    def sort(left, right) -> list:
        if left >= right:
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

    return sort(0, len(nums) - 1) if nums else []


def mergesort1(nums: List[int]) -> List[int]:
    """迭代版"""
    le = len(nums)
    new = [0] * le
    step = 1
    while step < le:
        for start in range(0, le, step * 2):
            left, mid, right = start, min(start + step, le), min(start + 2 * step, le)
            p = left
            p1, end1 = left, mid
            p2, end2 = mid, right
            # 数据拷贝到 new 并排序
            while p1 < end1 and p2 < end2:
                if nums[p1] < nums[p2]:
                    new[p] = nums[p1]
                    p1 += 1
                else:
                    new[p] = nums[p2]
                    p2 += 1
                p += 1

            rem = end1 - p2 + end2 - p1
            new[p:p + rem] = nums[p1:end1] if p1 < end1 else nums[p2:end2]
        step += step
        # 交换 new, nums
        nums, new = new, nums
    return nums


class TestMergeSort(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = mergesort(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


class TestMergeSort1(unittest.TestCase):
    def test_equal(self):
        for i in range(1000):
            lists = random_lists()
            cpy = lists[:]
            lists = mergesort1(lists)
            cpy.sort()
            self.assertEqual(lists, cpy)


if __name__ == '__main__':
    unittest.main()
