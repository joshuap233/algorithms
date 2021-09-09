# https://leetcode-cn.com/problems/wiggle-sort-ii/
# 324. 摆动排序 II
from typing import List


class Solution:
    """
        进阶：你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

        桶排序, 桶需要从右向左遍历插入数组中,防止相同的元素挤在中间
        从左向右遍历会出错

        比如序列: [4,5,5,6]
        第一次: 4 _ 5 _
        第二次: 4 5 5 6,

        桶需要从右向左遍历插入数组中:
        1:  _ 6 _ 5
        2. 5 6 4 5
    """

    def wiggleSort(self, nums: List[int]) -> None:
        b = [0] * 5001
        for i in nums:
            b[i] += 1
        le = len(nums)
        left = 5000

        for i in reversed(range(2)):
            for j in range(i, le, 2):
                while b[left] == 0:
                    left -= 1
                nums[j] = left
                b[left] -= 1


class Solution1:
    """
        利用快速选择找到中位数
    """

    def wiggleSort(self, nums: List[int]) -> None:
        target = (len(nums) - 1) // 2

        def quickSelect(left: int, right: int):
            ll, rr = left, right

            pivot = nums[ll]
            while ll < rr:
                while ll < rr and nums[rr] >= pivot:
                    rr -= 1
                nums[ll] = nums[rr]
                while ll < right and nums[rr] <= pivot:
                    ll += 1
                nums[rr] = nums[ll]
            nums[rr] = pivot

            if rr == target:
                return rr
            if rr > target:
                return quickSelect(left, rr - 1)
            return quickSelect(rr + 1, right)

        def three_way_partition(value: int):
            pass

        i = quickSelect(0, len(nums) - 1)


s = Solution1()
r = [1, 5, 1, 1, 6, 4]
s.wiggleSort(r)
print(r)
