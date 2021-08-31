# https://leetcode-cn.com/problems/product-of-array-except-self/
# 238. 除自身以外数组的乘积

from typing import List


class Solution:
    """
        说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
        ...什么不能用除法,不能用乘法...

        你可以在常数空间复杂度内完成这个题目吗？
        （ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

        O(n)时间复杂度就是要一遍遍历,弄个辅助数组就完事....
        或许可以叫前缀积
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        b = [1] * (n + 1)
        f = [1] * (n + 1)

        for i in range(n):
            b[i] = nums[i] * b[i - 1]

        for i in reversed(range(n)):
            f[i] = nums[i] * f[i + 1]

        return [b[i - 1] * f[i + 1] for i in range(n)]


class Solution2:
    """
        你可以在常数空间复杂度内完成这个题目吗？

        这是需要滚动数组类似的,或者直接用返回数组?
        ...
        两者结合,首先从左到右,计算元素 i 左边的乘积 left
        将 left 填入数组,然后从右到左,计算元素右边的乘积 right
        res[i] *= right
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 1
        for i, v in enumerate(nums):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in reversed(range(n)):
            res[i] *= right
            right *= nums[i]
        return res
