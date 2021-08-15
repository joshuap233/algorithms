# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
# 438. 找到字符串中所有字母异位词

# 这题和无重复字符的最长字串很像
# leetcode/hot100/3.py

from typing import List
from collections import Counter


class Solution:
    """
        很明显是要用滑动窗口匹配字符...而且窗口长度固定,
        将 Counter 计数器当成窗口即可, 时间复杂度为
        O(n*len(s))
    """

    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        m, n = len(s), len(p)
        target = Counter(p)
        window = Counter(s[:n - 1])

        res = []

        for i in range(n - 1, m):
            window[s[i]] += 1
            left = i - n + 1
            if target == window:
                res.append(left)

            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
        return res


s = Solution1()
s.findAnagrams("cbaebabacd", "abc")
