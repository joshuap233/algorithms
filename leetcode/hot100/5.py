# https://leetcode-cn.com/problems/longest-palindromic-substring/
# 5. 最长回文子串


class Solution:
    """
        O(n*n)
        遍历字符串, 当前字符为 a,以 a 为中心向两边扩张即可
        但有两种情况
        1
          aba 这可以直接以 b 为中心向两边扩张
          expand(i - 1, i + 1) 处理
        2
          bbbb 以 b 为中心向两边扩张会出现问题,

          expand(i, i + 1) 处理
    """

    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0

        def expand(ll, r):
            nonlocal right, left
            while ll >= 0 and r < len(s) and s[ll] == s[r]:
                ll -= 1
                r += 1
            if right - left < r - ll:
                right, left = r, ll

        for i, v in enumerate(s):
            expand(i - 1, i + 1)
            expand(i, i + 1)

        return s[left + 1:right]


sol = Solution()
sol.longestPalindrome("cbbd")
