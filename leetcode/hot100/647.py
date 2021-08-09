# https://leetcode-cn.com/problems/palindromic-substrings/
# 647. 回文子串


class Solution:
    """
        O(n*n)

        woc.....
        执行用时：104 ms, 击败了 90.31%
        内存消耗：14.8 MB 击败了 90.95%
        ?????
        中心向外扩展即可, cnt 初始化为 len(s)

        dp 方法也是 O(n*n).....那我用动态规划干嘛??
    """

    def countSubstrings(self, s: str) -> int:
        cnt = len(s)

        def sub(ll: int, rr: int) -> cnt:
            res = 0
            while ll >= 0 and rr < len(s) and s[ll] == s[rr]:
                ll -= 1
                rr += 1
                res += 1
            return res

        for i, v in enumerate(s):
            cnt += sub(i - 1, i + 1)
            cnt += sub(i, i + 1)

        return cnt
