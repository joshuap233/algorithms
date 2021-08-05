# https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
# 剑指 Offer 05. 替换空格


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")
