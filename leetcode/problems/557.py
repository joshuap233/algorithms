# 557. 反转字符串中的单词 III
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())
