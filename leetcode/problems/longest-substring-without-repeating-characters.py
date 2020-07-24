# 3. 无重复字符的最长子串
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


# 128ms
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        length = 0
        index = 0
        string_length = len(s)
        while index < string_length:
            while index < string_length and s[index] not in window:
                window.append(s[index])
                index += 1
            length = max(length, len(window))
            window.pop(0)
        return length


s = Solution()
print(s.lengthOfLongestSubstring('abcdefh'))
