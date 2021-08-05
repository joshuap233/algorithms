# https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
# 剑指 Offer 39. 数组中出现次数超过一半的数字

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, None
        for i in nums:
            if i == res:
                count += 1
            else:
                count -= 1
                if count < 1:
                    count = 1
                    res = i
        return res
