# https://leetcode-cn.com/problems/maximum-swap/submissions/
# 670. 最大交换
from collections import deque


class Solution:
    """
        构建单调栈
        注意 1993 需要换成 9913 而不是 9193
    """

    def maximumSwap(self, num: int) -> int:
        tmp = num
        num = list(str(num))

        stack = deque()
        for i, v in enumerate(num):
            # 移除栈内相同等的元素,防止 1993 与第一个 9 交换
            while stack and num[stack[-1]] <= v:
                stack.pop()
            stack.append(i)

        for i, v in enumerate(num):
            if not stack:
                break

            if v < num[stack[0]]:
                num[i], num[stack[0]] = num[stack[0]], num[i]
                return int(''.join(num))

            if stack[0] == i:
                stack.popleft()
        return tmp


s = Solution()
s.maximumSwap(2736)
