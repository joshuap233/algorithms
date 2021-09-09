# https://leetcode-cn.com/problems/daily-temperatures/
# 739. 每日温度

from typing import List
from collections import deque


class Solution:
    """
        从左向右遍历
        维护一个单调栈,如果当前元素 <= 栈顶元素, 当前元素入栈
        否则栈顶元素出栈,直到当前元素为最小元素
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                e = stack.pop()
                res[e] = i - e
            stack.append(i)
        return res
