# https://leetcode-cn.com/problems/next-permutation/
# 31. 下一个排列
# 这题目描述是真的迷...
# 注意 [1,3,2] 的下一个字典序不是 [2,3,1] 而是 [2,1,3]

from typing import List

"""
以数字序列 [1,2,3][1,2,3] 为例，其排列按照字典序依次为：
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]

最大的排列 [3,2,1][3,2,1] 的下一个排列为最小的排列 [1,2,3][1,2,3]。

需要从右到左,找到一个数 a, 与它左边的数 b 交换, 
明显,数 a 为数 b 右边序列中最小的那个,而数 b ,为有右到左
逆序遍历中,恰好比 a 大的数

因此,数 b 右边的数为降序排列(即右边序列中没有可以交换的数)
a,b 交换后: a,x,x,x,b,x,x,
a 后的数逆序
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


s = Solution()
l = [1, 5, 1]
s.nextPermutation(l)
print(l)
