# https://leetcode-cn.com/problems/trapping-rain-water/
# 42. 接雨水

from typing import List
from collections import deque


class Solution:
    """
        暴力法

        求每一列的水，我们只需要关注当前列，
        以及左边最高的墙，右边最高的墙就够了。

        O(n*n)
        很明显很慢....
    """

    def trap(self, height: List[int]) -> int:
        res = 0
        maxi = 0
        for i, v in enumerate(height):
            max_right = max(height[i + 1:], default=0)
            res += max(min(maxi, max_right) - v, 0)
            maxi = max(maxi, v)
        return res


class Solution1:
    """
        可以优化的地方: 找右边最大值
        可以利用单调栈
    """

    def trap(self, height: List[int]) -> int:
        # 构建单调栈
        stack = deque()
        for i in height:
            while stack and stack[-1] < i:
                stack.pop()
            stack.append(i)

        res = 0
        maxi = 0
        for i, v in enumerate(height):
            max_left = stack[0]
            res += max(min(maxi, max_left) - v, 0)
            maxi = max(maxi, v)
            if v == stack[0]:
                stack.popleft()
        return res


class Solution2:
    """
        构建单调栈的代码可以优化
    """

    def trap(self, height: List[int]) -> int:
        # 构建单调栈
        stack = deque()
        for i in reversed(height):
            if not stack or stack[0] <= i:
                stack.appendleft(i)

        res = 0
        maxi = 0
        for i, v in enumerate(height):
            max_left = stack[0]
            res += max(min(maxi, max_left) - v, 0)
            maxi = max(maxi, v)
            if v == stack[0]:
                stack.popleft()
        return res


s = Solution2()
s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
