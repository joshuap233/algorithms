# https://leetcode-cn.com/problems/maximum-product-subarray/
# 152. 乘积最大子数组

from typing import List


class Solution:
    """
        整数数组 nums, 类似 最大子序和, 不过要分正负两种情况
        所以动态规划需要两个数组,一个数组(a)存最大值,
        一个数组(b)存最小值,需要同时更新 a,b 数组
        注意初始化:
            maxi[0] = nums[0]
            mini[0] = nums[0]
        除非遇到负数,否则乘积必定越变越大(因为都是整数)
        所以只需要比较:
            nums[i], maxi[i - 1] * v, mini[i - 1] * v

    """

    def maxProduct(self, nums: List[int]) -> int:
        maxi = [0] * len(nums)  # 存正数
        mini = [0] * len(nums)  # 存负数

        maxi[0] = nums[0]
        mini[0] = nums[0]
        for i in range(1, len(nums)):
            v = nums[i]
            maxi[i] = max(nums[i], maxi[i - 1] * v, mini[i - 1] * v)
            mini[i] = min(nums[i], maxi[i - 1] * v, mini[i - 1] * v)
        return max(maxi)


class Solution1:
    """
        优化上面的代码,只需要之前的最大值与最小值即可
    """

    def maxProduct(self, nums: List[int]) -> int:
        res = mini = maxi = nums[0]

        for i in nums[1:]:
            maxi, mini = max(maxi * i, i, mini * i), min(maxi * i, i, mini * i)
            res = max(maxi, res)
        return res


s = Solution1()
s.maxProduct([-4, -3, -2])
