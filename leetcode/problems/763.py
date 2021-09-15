# https://leetcode-cn.com/problems/partition-labels/
# 763. 划分字母区间
from typing import List


class Solution:
    """
        同一字母最多出现在一个片段中,
        也就是一个片段要包括所有相同的字母
    """

    def partitionLabels(self, s: str) -> List[int]:
        a = {}
        ret = []
        for i, v in enumerate(s):
            a[v] = i

        i = 0
        while i < len(s):
            cnt = 1
            end = a[s[i]]
            while i < end:
                end = max(end, a[s[i]])
                i += 1
                cnt += 1
            i += 1
            ret.append(cnt)
        return ret
