# https://leetcode-cn.com/problems/hamming-distance/
# 461. 汉明距离

class Solution:
    """
        两个数字对应二进制位不同的位置的数目...麻了
    """

    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
