# 剑指 Offer 11. 旋转数组的最小数字
# https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 0:
            return 0

        prev = float('inf')
        for i in numbers[::-1]:
            if i > prev:
                return prev
            prev = i
        return numbers[0]


s = Solution()
print(s.minArray([2, 2, 2, 0, 1]))
