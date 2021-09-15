# https://leetcode-cn.com/problems/course-schedule/
# 207. 课程表

from typing import List
from collections import deque


class Solution:
    """
        prerequisites 中的元素相当于: [cur,prev]
        拓扑排序


        邻接表: 如果存在一条 (x,y) 的遍,
        则 array[x][y] 置 1

        方法一：入度表（广度优先遍历）
        生成入度表与邻接表,将入度为 0 的节点添加到队列,
        元素 e 出队,然后 (e,x) 入度 -1(相当于删除 e 元素),也就是
        aj[e] 内的元素入度 --, 如果某个元素入度为 0,添加到队列,
        统计出栈的个数是否等于 numCourses 即可

        因为如果 a,b 为环, 那么 a,b 之外的元素删除完了, a,b 入度不会是
        0, 也就不会入栈,
        比如 1->2->3->4->2 删除 1 元素,并不会将环内元素入度清空
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        degrees = [0] * numCourses
        aj = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            degrees[cur] += 1
            aj[pre].append(cur)
        queue = deque([i for i, v in enumerate(degrees) if v == 0])

        while queue:
            h = queue.popleft()
            numCourses -= 1
            for cur in aj[h]:
                degrees[cur] -= 1
                if degrees[cur] == 0:
                    queue.append(cur)
        return numCourses == 0
