# https://leetcode-cn.com/problems/maximal-rectangle/
# 85. 最大矩形

from typing import List


class Solution:
    """
        做法与 221 题一模一样...
        leetcode/hot100/221.py
    """
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_width(k: int) -> int:
            cnt = 0
            while k:
                k &= k << 1
                cnt += 1
            return cnt

        maps = [int(''.join(i), base=2) for i in matrix]
        le = len(maps)

        maxi = 0
        for i, v in enumerate(maps):
            for j in range(i, le):
                v &= maps[j]
                maxi = max(maxi, (j - i + 1) * get_width(v))
        return maxi

