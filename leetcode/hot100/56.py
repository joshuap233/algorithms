# https://leetcode-cn.com/problems/merge-intervals/
# 56. 合并区间

from typing import List


class Solution:
    """
      排序题, 然后 记录 left ,right ,right 需要取所有区间中大的那个,
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0]
        for s, e in intervals:
            if s <= right:
                right = max(right, e)
            else:
                res.append([left, right])
                left, right = s, e

        if not res or res[-1] != [left, right]:
            res.append([left, right])
        return res


class Solution1:
    """
        上面的优化, 不记录 left,right,直接与上个区间比较并更新上个区间
        上面的快一点.....
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for s, e in intervals:
            if not res or s > res[-1][1]:
                res.append([s, e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res
