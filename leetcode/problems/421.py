# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/
# 421. 数组中两个数的最大异或值
from typing import List


class Solution:
    """
        构建前缀树(两种元素 0/1),
        需要将高位放到树的上层, 否则匹配的时候需要使用字符串表示异或值
    """

    def findMaximumXOR(self, nums: List[int]) -> int:
        tree = {}
        for i in nums:
            root = tree
            for j in range(30, -1, -1):
                v = (i >> j) & 1
                if v not in root:
                    root[v] = {}
                root = root[v]

        maxi = 0
        m = {0: 1, 1: 0}
        for i in nums:
            root = tree
            cur = 0
            for j in range(30, -1, -1):
                v = (i >> j) & 1
                cur = cur * 2
                if m[v] in root:
                    cur += 1
                    root = root[m[v]]
                else:
                    root = root[v]
            maxi = max(maxi, cur)
        return maxi
