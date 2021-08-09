# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
# 581. 最短无序连续子数组


from typing import List


class Solution:
    """
        进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？

        思路: 很明显是双指针
        设置双指针 left,right

        例子:
            [2, 6, 4, 8, 10, 9, 15]
                6, 4, 8, 10, 9
         6 之前的元素与 9 之后的元素必然递增
         因此移动 left 指针时,nums[left] 必定为
         left ~ end 中最小的一个, right 指针同理,
         题目转化为怎么判断 num[left] 是最小的一个

         可以左边遍历,直到序列非递增,记录索引 left
         从右边往左遍历,直到非递增,记录,right,
         在 left ~ end 与 0- right 之间查找比
         num[left] 小的数, 比 num[right] 大的数,
         然后再次遍历,可以找到边界....
         好复杂的逻辑......一写就错,看来需要简化思路

        这题的边界太恶心了.....
    """

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        maxi, mini = float('-inf'), float('inf')
        for i, v in enumerate(nums):
            if v < maxi:
                right = i
            else:
                maxi = v

        for i in reversed(range(len(nums))):
            if nums[i] > mini:
                left = i
            else:
                mini = nums[i]
        return 0 if right == left else right - left + 1


s = Solution()
s.findUnsortedSubarray([1, 2, 3, 4])


class Solution1:
    """
        暴力解简单,先排序,然后 设置 left,right 指针比较即可
    """

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = sorted(nums[:])
        left, right = 0, n - 1

        while left < n and nums[left] == tmp[left]:
            left += 1
        while right >= 0 and nums[right] == tmp[right]:
            right -= 1
        return 0 if right < left else right - left + 1
