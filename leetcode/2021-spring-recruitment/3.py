class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        left = 0
        _ascii = dict()
        for i, v in enumerate(s):
            if v in _ascii and _ascii[v] >= left:
                _max = max(_max, i - left)
                left = _ascii[v] + 1
            _ascii[v] = i
        return max(_max, len(s) - left)


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
