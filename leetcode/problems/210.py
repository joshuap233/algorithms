# https://leetcode-cn.com/problems/course-schedule-ii/
# 210. 课程表 II


from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = []
        adj = []

