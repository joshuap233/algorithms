# https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
# 剑指 Offer 44. 数字序列中某一位的数字


class Solution:
    """
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

    1*9 + 2*90 + 3*900 + 4*9000 + 5 *90000 + 6*900000 +
    7 *9000000 + 8*90000000 + 9*900000000 ..
    """

    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n

        cnt = 10    # 当前层的数字总数
        length = 1  # 当前层的数字长度
        start = 1
        while n > cnt:
            n -= cnt
            length += 1
            start *= 10
            cnt = start * length * 9

        index = n // length
        value = start + index
        return int(str(value)[n % length])


s = Solution()
print(s.findNthDigit(11))
