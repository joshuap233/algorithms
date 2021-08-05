# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
# 剑指 Offer 61. 扑克牌中的顺子

from typing import List


# 提交错两次才对, 离谱
# 出现非 0 重复的牌,则不能构成顺子
class Solution:

    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zero = nums.count(0)
        j = zero + 1
        while j < 5:
            diff = nums[j] - nums[j - 1]
            if diff != 1:
                if diff == 0 or zero < (diff - 1):
                    return False
                zero -= diff - 1
            j += 1
        return True


class Solution1:
    """
        最大值 - 最小值 < 5 即可构成顺子
    """

    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        _min, _max = 14, 0
        for n in nums:
            if n == 0:
                continue
            if n in repeat:
                return False
            repeat.add(n)
            _min = min(_min, n)
            _max = max(_max, n)
        return _max - _min < 5


s = Solution()
s.isStraight([10, 11, 0, 12, 6])
