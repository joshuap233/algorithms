# https://leetcode-cn.com/problems/valid-palindrome/
# 125. 验证回文串


class Solution:
    """
        保留数字与字母再判断
    """
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
