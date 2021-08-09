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
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        maxi = num = 0
        i = j = 0
        # start[i] == end[j] 的情况没有为什么也能对?
        while i < len(start):
            if start[i] < end[j]:  # 上车
                num += 1
                i += 1
            else:
                num -= 1  # 下车
                j += 1
            maxi = max(maxi, num)
        return maxi



s = Solution()
s.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
