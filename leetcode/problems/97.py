# https://leetcode-cn.com/problems/interleaving-string/
# 97. 交错字符串
from functools import lru_cache


class Solution:
    """
        len(s1) + len(s2) == len(s3)

        dfs + memo(lru_cache)
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        le1, le2, le3 = len(s1), len(s2), len(s3)

        @lru_cache(None)
        def dfs(p1, p2, p3) -> bool:
            if p1 >= le1 and p2 >= le2:
                return True

            if p3 >= le3 and (p1 < le1 or p2 < le2):
                return False

            if p1 < le1 and s1[p1] == s3[p3]:
                if dfs(p1 + 1, p2, p3 + 1):
                    return True

            if p2 < le2 and s2[p2] == s3[p3]:
                if dfs(p1, p2 + 1, p3 + 1):
                    return True
            return False

        if le1 + le2 != le3:
            return False
        return dfs(0, 0, 0)
