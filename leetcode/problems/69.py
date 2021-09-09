# https://leetcode-cn.com/problems/sqrtx/
# 69. x 的平方根

class Solution:
    """二分"""

    def mySqrt(self, x: int) -> int:
        ll, rr = 0, x
        ret = 0
        while ll <= rr:
            mid = (ll + rr) // 2
            p = mid * mid
            if p > x:
                rr = mid - 1
            elif p < x:
                ll = mid + 1
                ret = mid
            else:
                return mid
        return ret
