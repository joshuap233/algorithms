# https://leetcode-cn.com/problems/is-unique-lcci/
# 面试题 01.01. 判定字符是否唯一


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))


class Solution1:
    """排序"""

    def isUnique(self, astr: str) -> bool:
        a = sorted(astr)
        for i in range(len(a) - 1):
            if a[i] == a[i + 1]:
                return False
        return True
