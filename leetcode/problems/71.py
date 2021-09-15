# https://leetcode-cn.com/problems/simplify-path/
# 71. 简化路径
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = deque()
        for i in paths:
            if i == '.' or not i:
                continue
            if i == '..':
                stack and stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))
