# 743. 网络延迟时间
# https://leetcode-cn.com/problems/network-delay-time/
import math
from typing import List


class Solution:

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
