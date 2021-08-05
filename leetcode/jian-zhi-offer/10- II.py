# https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
# 剑指 Offer 10- II. 青蛙跳台阶问题


class Solution:
    def numWays(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b % 1000000007


s = Solution()
print(s.numWays(7))
