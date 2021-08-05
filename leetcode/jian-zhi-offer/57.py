# https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
# 剑指 Offer 57. 和为s的两个数字


from typing import List


# 使用 set 存储已遍历数字方便查找
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = set()
        for i in nums:
            if target - i in d:
                return [i, target - i]
            else:
                d.add(i)
        return []


# 双指针 i , j 分别指向数组 numsnums 的左右两端 （俗称对撞双指针）
# 如果 nums[i] + nums[j] > target, 则 j 左移
# 如果 ....              < target, 则 i 右移
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [nums[left], nums[right]]
        return []
