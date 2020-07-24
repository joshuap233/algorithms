# 最长回文子串
# https://leetcode-cn.com/problems/longest-palindromic-substring/


# 1644ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        subString = []
        max_subString = {'length': 0, 'left': 0, 'right': 0}
        for index, item in enumerate(s):
            if index + 1 < len(s) and s[index] == s[index + 1]:
                subString.append([index, index + 1])
            if index + 2 < len(s) and s[index] == s[index + 2]:
                subString.append([index, index + 2])
        for string in subString:
            left = string[0]
            right = string[1]
            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            length = right - left
            if length > max_subString['length']:
                max_subString['length'] = length
                max_subString['left'] = left
                max_subString['right'] = right
        return s[max_subString['left']:max_subString['right'] + 1]


s = Solution()
print(s.longestPalindrome('babad'))
