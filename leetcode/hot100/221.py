# https://leetcode-cn.com/problems/maximal-square/
# 221. 最大正方形

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        for y, array in enumerate(matrix):
            for x, v in enumerate(array):
                if v == 1:
                    pass
