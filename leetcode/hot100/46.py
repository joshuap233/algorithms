# https://leetcode-cn.com/problems/permutations/
# 46. 全排列

"""
    本题类似 leetcode/jian-zhi-offer/38.py
"""

from typing import List


class Solution:
    """
        使用递归,每层递归去掉个数字,将去掉的数字添加到
        head
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(head: list, ll: list):
            if len(ll) == 1:
                head.extend(ll)
                res.append(head)

            for i, v in enumerate(ll):
                recur(head[:] + [v], ll[:i] + ll[i + 1:])

        recur([], nums)
        return res


class Solution1:
    """
        回溯:
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(first):
            if first == len(nums)-1:
                res.append(nums[:])
                return
            # first 之前的数已经填过
            for i in range(first, len(nums)):
                # 将已经使用的值放到 first 位
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                # 回溯
                nums[i], nums[first] = nums[first], nums[i]

        # first 为等待填入的索引
        backtrack(0)
        return res


class Solution2:
    def permute(self, nums: List[int]):
        import itertools
        return list(itertools.permutations(nums))


class Solution3:
    """
        采用下一个字典序的方法
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [nums[:]]

        while True:
            i = len(nums) - 2

            while i >= 0 and nums[i] > nums[i + 1]:
                i -= 1

            if i >= 0:
                j = len(nums) - 1
                while j > i and nums[j] < nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]

                # 逆序
                left, right = i + 1, len(nums) - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                res.append(nums[:])
            else:
                return res
