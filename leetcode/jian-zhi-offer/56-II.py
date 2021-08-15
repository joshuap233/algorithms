# https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
# 剑指 Offer 56 - II. 数组中数字出现的次数 II

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        for i in counter:
            if counter[i] == 1:
                return i


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


class Solution2:
    """
    考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 3 的倍
    数。因此，统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，结果则为
    只出现一次的数字。
    如:
     3 = 0b0011
     3 = 0b0011
     3 = 0b0011
     5 = 0b0101
`    统计结果:
         0124
     对 3 求余
         0b0101
    """

    def singleNumber(self, nums: List[int]) -> int:
        res = [0] * 32
        for i in nums:
            j = 0
            while i:
                if i & 1:
                    res[j] += 1
                j += 1
                i >>= 1
        ret = 0
        for i in reversed(res):
            ret <<= 1
            ret |= i % 3
        return ret


s = Solution2()
s.singleNumber([3, 4, 3, 3])
