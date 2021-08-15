# https://leetcode-cn.com/problems/longest-common-prefix/
# 14. 最长公共前缀
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = min(strs, key=lambda x: len(x))
        for i, v in enumerate(f):
            for j in strs:
                if j[i] != v:
                    return f[:i]
        return f


s = Solution()
s.longestCommonPrefix(["flower", "flow", "flight"])
