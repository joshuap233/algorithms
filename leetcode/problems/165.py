# https://leetcode-cn.com/problems/compare-version-numbers/
# 165. 比较版本号


class Solution:
    """忽略任何前导零后的整数值"""

    def compareVersion(self, version1: str, version2: str) -> int:
        n, m = len(version1), len(version2)
        i = j = 0
        while i < n or j < m:
            v1 = v2 = 0
            while i < n and version1[i].isdigit():
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < m and version2[j].isdigit():
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
            j += 1
        return 0


class Solution1:
    """思路二"""

    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        m = min(len(v1), len(v2))
        for p in range(m):
            a, b = int(v1[p]), int(v2[p])
            if a > b:
                return 1
            elif a < b:
                return -1

        if sum(v1[m:]) != sum(v2[m:]):
            return 1 if len(v1) > len(v2) else -1
        return 0
