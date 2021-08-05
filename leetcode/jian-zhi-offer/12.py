# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
# 剑指 Offer 12. 矩阵中的路径

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        y, x = len(board), len(board[0])

        def dfs(i, j, k) -> bool:
            if k >= len(word):
                return True
            if not 0 <= i < x or not 0 <= j < y or board[j][i] != word[k]:
                return False

            board[j][i] = '/'
            res = dfs(i, j - 1, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1)
            board[j][i] = word[k]
            return res

        for i in range(y):
            for j in range(x):
                if board[i][j] == word[0] and dfs(j, i, 0):
                    return True
        return False


s = Solution()
res = s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB")
print(res)
