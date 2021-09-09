# 与 316 题相同
# 1081. 不同字符的最小子序列
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/

from collections import Counter, deque


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        c = Counter(s)
        q = deque()
        for i in s:
            if i not in q:
                while q and q[-1] >= i and c[q[-1]]:
                    q.pop()
                q.append(i)
            c[i] -= 1
        return ''.join(q)
