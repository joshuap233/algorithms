# https://leetcode-cn.com/problems/number-of-provinces/submissions/
# 547. 省份数量


from typing import List


class Solution:
    """
        并查集
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        le = len(isConnected)
        Set = list(range(le))

        def find(idx: int) -> int:
            if Set[idx] == idx:
                return idx
            Set[idx] = find(Set[idx])
            return Set[idx]

        def union(r1: int, r2: int):
            Set[find(r1)] = Set[find(r2)]

        for i in range(le):
            for j in range(i + 1, le):
                if isConnected[i][j] == 1:
                    union(i, j)
        return sum(1 for i, v in enumerate(Set) if i == v)


class Solution1:
    """
        深搜
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int) -> bool:
            r = False
            for j in range(le):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0
                    dfs(j)
                    r = True
            return r

        ret = 0
        le = len(isConnected)
        for i in range(le):
            if dfs(i):
                ret += 1
        return ret


s = Solution1()
s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
