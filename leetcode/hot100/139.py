# https://leetcode-cn.com/problems/word-break/
# 139. 单词拆分

from typing import List
from functools import lru_cache


class Solution:
    """
        递归剪枝
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(word: str) -> bool:
            if not word:
                return True
            for i in range(1, len(word) + 1):
                if word[:i] in wordDict:
                    if dfs(word[i:]):
                        return True
            return False

        return dfs(s)


class Solution1:
    """
        动态规划
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i - 1] and s[i:j + 1] in wordDict:
                    dp[j] = True
        return dp[-2]

