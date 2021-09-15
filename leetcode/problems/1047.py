# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
# 1047. 删除字符串中的所有相邻重复项
from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque([''])
        for i in s:
            if i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)
