# https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
# 剑指 Offer 50. 第一个只出现一次的字符

from collections import Counter


# 用哈续表存储频数
class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for i in s:
            d[i] = 2 if i in d else 1

        for i in s:
            if d[i] == 1:
                return i
        return ' '


# 使用 collection 的 counter
class Solution2:
    def firstUniqChar(self, s: str) -> str:
        cnt = Counter(s)
        for v in s:
            if cnt[v] == 1:
                return v
        return ' '
