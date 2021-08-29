# https://leetcode-cn.com/problems/sqrtx/
# 69. x 的平方根

class Solution:
    """二分...."""

    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        ret = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        return ret
