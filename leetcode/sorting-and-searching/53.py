#  第一个错误的版本
# The isBadVersion API is already defined for you.


def isBadVersion(version) -> bool:
    """
        @param version, an integer
        @return a bool
    """
    pass


class Solution:
    def firstBadVersion(self, n):
        start = 0
        end = n
        while start <= end:
            mid = (end + start) // 2
            if isBadVersion(mid):
                if mid == 1 or (mid > 1 and not isBadVersion(mid-1)):
                    return mid
                end = mid - 1
            else:
                start = mid + 1
