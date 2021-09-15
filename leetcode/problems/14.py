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


class Solution1:
    """
        字符串排序之后比较头尾部
        (排序之后,公共前缀最大最小的必然在头尾)
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


s = Solution()
s.longestCommonPrefix(["flower", "flow", "flight"])
