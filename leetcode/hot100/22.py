# https://leetcode-cn.com/problems/generate-parentheses/
# 22. 括号生成
# 这题和全排列类似

from typing import List
from collections import deque

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

        def backtrack(left: int, right: int):
            if len(cur) == 2 * n:
                res.append(''.join(cur))

            if left > 0:
                cur.append('(')
                backtrack(left - 1, right)
                cur.pop()

            if left < right:
                cur.append(')')
                backtrack(left, right - 1)
                cur.pop()

        cur = deque()
        backtrack(n, n)
        return res


s = Solution()
print(s.generateParenthesis(4))
