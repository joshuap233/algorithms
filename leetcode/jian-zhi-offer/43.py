# https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
# 剑指 Offer 43. 1～n 整数中 1 出现的次数


class Solution:
    """
        1               1-9
        20              1-99
        300             1-999
        4000            1-9999
        50000           1-99999
    """

    def countDigitOne(self, n: int) -> int:
        cnt = 0
        for i in range(n + 1):
            cnt += str(i).count('1')
        print(cnt)


s = Solution()
s.countDigitOne(99)
