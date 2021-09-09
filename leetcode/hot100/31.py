# https://leetcode-cn.com/problems/next-permutation/
# 31. 下一个排列

from typing import List


class Solution:
    """
        注意: 如果不存在下一个更大的排列，则将数字重新排列成最小的排列
        （即升序排列）。
    """

    def nextPermutation(self, nums: List[int]) -> None:
        le = len(nums)
        i = 0
        # 从后向前查找第一个降序序列,比如 0 4 3 2 1, 找到 0
        for i in reversed(range(le - 1)):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return

        j = 0
        # 找到第一个比 i 大数字的索引
        for j in reversed(range(i + 1, le)):
            if nums[j] > nums[i]:
                break

        # 交换
        nums[j], nums[i] = nums[i], nums[j]

        # 逆序
        ll, rr = i + 1, le - 1
        while ll < rr:
            nums[ll], nums[rr] = nums[rr], nums[ll]
            ll += 1
            rr -= 1
