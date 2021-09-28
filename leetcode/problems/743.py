# 743. 网络延迟时间
# https://leetcode-cn.com/problems/network-delay-time/
import math
from typing import List


class Solution:
    """
    迪杰斯特拉算法解决单源最短路径问题

    思想
    选择源点 k,顶点个数 n,维护两个数据结构:
    1. 点是否已经访问( visited = [False]*n )
    2. 点到到原点的距离( dist = [[float('inf')]*n for _ in range(n)] )

    具体步骤:
    1. 找到距 k 路径最短且未访问的点 x, 将该点值置为已访问
    2. 更新与该点连通的点到 k 的距离( dist[i] = min(dist[i], dist[x] + time) )
    以上步骤循环 n 次

    具体应用见 leetcode/problems/743.py
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[k - 1] = 0
        visited = [False] * n

        g = [[float('inf')] * n for _ in range(n)]
        for u, v, time in times:
            g[u - 1][v - 1] = time

        for _ in range(n):
            x = min(
                enumerate(dist),
                key=lambda h: h[1] if not visited[h[0]] else float('inf')
            )[0]
            visited[x] = True
            for i, time in enumerate(g[x]):
                dist[i] = min(dist[i], dist[x] + time)
        ret = max(dist)
        return -1 if math.isinf(ret) else ret
