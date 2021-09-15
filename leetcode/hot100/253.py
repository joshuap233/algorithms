# https://leetcode-cn.com/problems/meeting-rooms-ii/
# 253. 会议室 II

from typing import List


class Solution:
    """
        看起来像排序题.....

        将问题转化为上下车问题:
        将问题转化为车上最多有多少人

        比如:
            intervals = [[0,30],[5,10],[15,20]]
            第一个人从0上车，从30下车；
            第二个人从5上车，10下车。。。
        为什么可以这么做?
        车上有 x 个人意味着,这 x 个会议时间并列(不能安排在同一会议室)
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted(intervals, key=lambda x: x[0])
        end = intervals
        end.sort(key=lambda x: x[1])

        maxi = cnt = 0
        p = 0
        for i in start:
            cnt += 1
            while end[p][1] <= i[0]:
                cnt -= 1
                p += 1
            maxi = max(maxi, cnt)
        return maxi


s = Solution()
s.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
