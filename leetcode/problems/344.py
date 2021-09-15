# https://leetcode-cn.com/problems/reverse-string/
# 344. 反转字符串
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


class Solution1:
    """
        那些公司也不会出这种题...
    """
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
