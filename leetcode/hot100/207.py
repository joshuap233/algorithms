# https://leetcode-cn.com/problems/course-schedule/
# 207. 课程表

from typing import List


class Solution:
    """
        判断是否有环就行...访问某个元素后标记下..

        在选修某些课程之前需要一些先修课程,也就是说,
        有这种阴间数据:
            [[1,0],[1,2],[0,1]]
        也就是,这是个图....

        时间超限......
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        d = defaultdict(list)

        for i in prerequisites:
            d[i[0]].append(i[1])

        def dfs(course: int) -> bool:
            if course not in d:
                return True
            if d[course][-1] is None:
                return False

            for j in d[course]:
                d[course].append(None)
                if not dfs(j):
                    return False
                d[course].pop(-1)
            return True

        for i in prerequisites:
            if not dfs(i[0]):
                return False
        return True


class Solution1:
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
        from collections import deque

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


s = Solution()
s.canFinish(3, [[1, 0], [1, 2], [0, 1]])
