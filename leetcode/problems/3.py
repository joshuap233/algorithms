# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 3. 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxvalue = 0
        length = 0
        start = 0
        d = {}
        for i, v in enumerate(s):
            if v not in d or d[v] < start:
                length += 1
                d[v] = i
            else:
                maxvalue = max(maxvalue, length)
                length = i - d[v]
                start = d[v]
                d[v] = i
        return max(maxvalue, length)


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
