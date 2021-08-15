# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
# 剑指 Offer 56 - I. 数组中数字出现的次数

from typing import List
from functools import reduce


class Solution:
    """
    设两个数为 x,y,将输入的整数异或结果为 z,即 z = x^y,
    异或: 位相同为 0, 位不同为 1, 两个不同的数必定有以为不同,即该位的异或结果为 1
    找到该为 a, 由此可以将输入的数组分为两个子数组,一个子数组内的元素 与 a 为 0,
    另一个与 a 为 1, x,y 分别位于两个子数组, 且其他数必定出现两次

    最开始需要异或所有数字的原因是,必须找到 x 或 y 存在的位,否则无法分组
    """

    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = reduce(lambda a, b: a ^ b, nums)
        i = 0
        while res & 1 != 1:
            i += 1
            res >>= 1
        m = 1 << i

        x, y = 0, 0
        for i in nums:
            if i & m:
                x ^= i
            else:
                y ^= i
        return [x, y]


# 上面查找有效位的算法可以简化:
class Solution1:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = reduce(lambda a, b: a ^ b, nums)
        m = 1
        while m & res == 0:
            m <<= 1

        x, y = 0, 0
        for i in nums:
            if i & m:
                x ^= i
            else:
                y ^= i
        return [x, y]
