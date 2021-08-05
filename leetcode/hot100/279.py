# https://leetcode-cn.com/problems/perfect-squares/
# 279. 完全平方数
# from math import isqrt


class Solution:
    """
       注意有个 isqrt(x) 函数, 对 x 开方然后向下取整
       isqrt(10) = 3,

        开始没有 left 直接时间超限,
        然后画树分析,使用 left 去重

        经典的使用 left 去重
    """

    def numSquares(self, n: int) -> int:
        from math import isqrt

        mini = n
        j = isqrt(n)
        square = [i * i for i in range(1, j + 1)]

        def recur(rem: int, cnt: int, left):
            nonlocal mini

            if rem == 0:
                mini = min(cnt, mini)
                return
            if rem < 0 or cnt >= mini:
                return

            while left >= 0:
                recur(rem - square[left], cnt + 1, left)
                left -= 1

        recur(n, 0, len(square) - 1)
        return mini


class Solution2:
    """
       动态规划, 类似于凑硬币那题...
    """

    def numSquares(self, n: int) -> int:
        from math import isqrt
        nums = [i * i for i in range(1, isqrt(n) + 1)]
        dp = [n] * (n + 1)

        # i = j 时会用到 dp[0],也就是需要凑的数恰好等于完全平方数时
        dp[0] = 0

        for i in nums:
            for j in range(i, n + 1):
                dp[j] = min(dp[j - i] + 1, dp[j])
        return dp[-1]


s = Solution()
s.numSquares(14)
