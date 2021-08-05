# https://leetcode-cn.com/problems/word-break/
# 139. 单词拆分

from typing import List


class Solution:
    """
        构建字典树,
        使用 'end' 标记单词结束

        ....时间超限......
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        Dict = {}

        # 构建字典树
        for i in wordDict:
            subDict = Dict
            for j in i:
                subDict.setdefault(j, {})
                subDict = subDict[j]
            subDict['end'] = True

        def recur(left: int, sub: dict) -> bool:
            if left >= len(s):
                return 'end' in sub

            # 搜索到底部再回退
            res = s[left] in sub and recur(left + 1, sub[s[left]])

            res = res or ('end' in sub and recur(left, Dict))
            return res

        return recur(0, Dict)


class Solution:
    """
        不构建字典树, 直接用 in 判断...
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache

        @lru_cache()
        def recur(string: str) -> bool:
            if not string:
                return True

            res = False
            for i in range(1, len(string) + 1):
                if string[:i] in wordDict:
                    res = res or recur(string[i:])
            return res

        return recur(s)


s = Solution()
s.wordBreak('leetcode', ['leet', 'code'])
