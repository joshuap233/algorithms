# https://leetcode-cn.com/problems/valid-palindrome-ii/
# 680. 验证回文字符串 Ⅱ


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(ll: int, rr: int) -> bool:
            while ll < rr:
                if s[ll] != s[rr]:
                    return False
                ll += 1
                rr -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return valid(left + 1, right) or valid(left, right - 1)
            left += 1
            right -= 1
        return True
