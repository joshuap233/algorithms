# https://leetcode-cn.com/problems/palindrome-partitioning/
# 131. 分割回文串


from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isM(array: list) -> bool:
            for i in range(len(array) // 2):
                if array[i] != array[-i - 1]:
                    return False
            return True

        def backtrace(left: int, cur: list):
            if cur and isM(cur):
                res.append(''.join(cur))
            for i in range(left, len(s)):
                cur.append(s[left])
                backtrace(i + 1, cur)
                cur.pop(-1)

        backtrace(0, [])
        return res


s = Solution()
s.partition("aab")
