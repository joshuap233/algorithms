# https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# 1647. 字符频次唯一的最小删除次数
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        s = set()
        ret = 0
        for key, cnt in c.items():
            if cnt in s:
                j = 0
                for j in reversed(range(cnt)):
                    if j not in s:
                        s.add(j)
                        break
                ret += cnt - j
            s.add(cnt)

        return ret


s = Solution()
r = s.minDeletions("ceabaacb")
print(r)
