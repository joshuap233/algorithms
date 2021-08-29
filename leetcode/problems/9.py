# https://leetcode-cn.com/problems/palindrome-number/
# 9. 回文数


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True
