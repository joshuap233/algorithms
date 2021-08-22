# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
# 剑指 Offer 40. 最小的k个数

import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) <= k:
            return arr
        arr.sort()
        return arr[:k]


# 堆
class Solution1:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        hp = [-i for i in arr[:k]]
        heapq.heapify(hp)
        for i in arr[k:]:
            if hp[0] < -i:
                heapq.heapreplace(hp, -i)
        return [-i for i in hp]
