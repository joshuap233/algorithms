# https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
# 剑指 Offer 44. 数字序列中某一位的数字


class Solution:
    """
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

    1*9 + 2*90 + 3*900 + 4*9000 + 5 *90000 + 6*900000 +
    7 *9000000 + 8*90000000 + 9*900000000 ..

    没有难度,但是恶心... 记录三个数据:
    开始数, 结束的数, 当前层的数的位数(第一层特殊处理)
    """

    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n

        s, e = 1, 9
        cnt = 10
        le = 1
        while cnt < n:
            n -= cnt
            s, e = s * 10, e * 10 + 9
            le += 1
            cnt = (e - s + 1) * le

        num = s + n // le
        return int(str(num)[n % le])


s = Solution()
print(s.findNthDigit(11))
