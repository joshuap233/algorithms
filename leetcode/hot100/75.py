# https://leetcode-cn.com/problems/sort-colors/
# 75. 颜色分类

from typing import List


class Solution:
    """
        你可以不使用代码库中的排序函数来解决这道题吗？
        你能想出一个仅使用常数空间的一趟扫描算法吗？

        我最开始的思路:
        这种问题(一趟扫描,常数空间)一般是交换问题,

        所以有一个 left,一个 right 指针
        left <= right 停止, left指针指向的值为 0 时,
        left +=1, right 指针指向 2 时, right-=1,剩下下面的几种情况

        left     right
        1        0
        1        1
        2        0
        2        1
        除了 1,1 的情况, 其他情况直接交换,移动相应的指针即可,
        当遇到 1,1 时...算法已经无法继续....

        换种思路,设立三个指针, left,right,i, i用于一趟扫描
        left 指向左边非红色, right 指向非黑色
        i 遇到黑色, 与 right 指向的元素交换
        i 遇到红色, 与 left 指向的元素交换
    """

    def sortColors(self, nums: List[int]) -> None:
        i = left = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 2:
                while i < right and nums[right] == 2:
                    right -= 1
                nums[i], nums[right] = nums[right], nums[i]
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            i += 1


s = Solution()
s.sortColors([1, 2, 0])
