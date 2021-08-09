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
        1. num[i] 为 0, 与 num[left] 交换, i+=1
        2. nums[i] 为 2, 与 nums[right] 交换,
        3. num[i] 为 1, i+=1

        第一种情况, 未交换前, num[left] 必然为 1,否则就是第二种情况,
        也就是说, i ~ left 必然全为 1 ,因此 i+1

        第二种情况, 未交换前, num[left] 可能为 0 或 1
        如果为 0 , 那么交换后可能出现这种顺序:
        0,0,0,1,1 [0],xxx
        因此 i 指针能移动

    """

    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        i = 0
        while i < len(nums) and i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


s = Solution()
s.sortColors([1, 2, 0])
