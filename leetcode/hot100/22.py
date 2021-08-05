# https://leetcode-cn.com/problems/generate-parentheses/
# 22. 括号生成
# 这题和全排列类似

from typing import List


class Solution:
    """
        注意这种: (()())

        这题相当于填括号题,有 n 个 '(' 与 n 个 ')'
        设剩余 x 个 '(' 括号, y 个 ')' 括号
        x,y 必须满足 x >= y

        也就是 right - ll + 1
    """

    def generateParenthesis(self, n: int) -> List[str]:
        res = set()

        def recur(head: str, left: int, right: int) -> None:
            if left == 0:
                res.add(head + ')' * right)
                return

            for i in range(1, left + 1):
                ll = left - i
                for j in range(1, right - ll + 1):
                    recur(head + '(' * i + ')' * j, ll, right - j)

        # left right 为剩余的左右括号数
        recur('', n, n)
        return list(res)


class Solution1:
    """
      这种方法不需要剪枝..
    """

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s: list, left: int, right: int):
            if len(s) == 2 * n:
                res.append(''.join(s))

            if left > 0:
                s.append('(')
                backtrack(s, left - 1, right)
                s.pop(-1)
            if left < right:
                s.append(')')
                backtrack(s, left, right - 1)
                s.pop(-1)

        backtrack([], n, n)
        return res


s = Solution()
print(s.generateParenthesis(4))
