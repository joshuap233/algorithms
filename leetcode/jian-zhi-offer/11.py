# 剑指 Offer 11. 旋转数组的最小数字
# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

from typing import List


class Solution:
    """
        二分
        好恶心的题
    """

    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                return min(numbers[left:right])
        return numbers[left]


s = Solution()
print(s.minArray([2, 2, 2, 0, 1]))
