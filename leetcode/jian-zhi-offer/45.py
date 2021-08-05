# https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
# 剑指 Offer 45. 把数组排成最小的数
from typing import List
from functools import cmp_to_key


class Solution:
    """
    本质是排序题, 难点是比较 a:str, b:str 的大小
    比较方法:
        比较 a+b 与 b + a 即可
    麻烦的是 Python3 的 sort 没有 cmp 参数, key=lambda .. 这种只有一个参数,
    所以 cmp_to_key 是怎么实现的?
    """
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]

        def cmp(x: str, y: str):
            s1 = x + y
            s2 = y + x
            return 1 if s1 > s2 else -1

        nums.sort(key=cmp_to_key(cmp))
        return ''.join(nums)
