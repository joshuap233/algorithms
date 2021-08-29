# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
# 1047. 删除字符串中的所有相邻重复项


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(i)
        return ''.join(stack)
