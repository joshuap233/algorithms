from typing import List
from heapq import heapify, heappop


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
