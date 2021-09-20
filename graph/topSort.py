"""
    拓扑排序是对有向无圈图顶点的一种排序，它使得
    如果存在一条从 vi 到 vj 的路径，那么在排序中
    vi 出现在 vj 的后面。
    显然如果图含有圈，那么拓扑排序是不可能的，因此可以用于判断
    图是否存在圈

    一个简单的拓扑排序算法：
    需要一个入度表与邻接表
    将所有入度为 0 的顶点放入队列， 队列元素 A
    出队， 删除该顶点(查找 A 的邻接表，将所有 A 通向的顶点的入度减一)，
    A 顶点删除后，某个因此而入度为 0， 将该顶点加入队列

    应用: leetcode/hot100/207.py 课程表
"""


def main():
    adjacent_list = [[1, 2], [0, 2], [1]]  # 邻接表
    degrees = [1, 2, 2]  # 入度表

    q = [i for i, v in enumerate(degrees) if v == 0]
    while q:
        h = q.pop(0)
        for c in adjacent_list[h]:
            degrees[c] -= 1
            if degrees[c] == 0:
                q.append(c)


