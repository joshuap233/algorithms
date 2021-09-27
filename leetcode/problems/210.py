# https://leetcode-cn.com/problems/course-schedule-ii/
# 210. 课程表 II


from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        ret = []

        for ai, bi in prerequisites:
            adj[bi].append(ai)
            indegree[ai] += 1
        q = deque([i for i, v in enumerate(indegree) if v == 0])

        while q:
            numCourses -= 1
            e = q.pop()
            ret.append(e)
            for i in adj[e]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return ret if numCourses == 0 else []
