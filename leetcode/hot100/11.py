# https://leetcode-cn.com/problems/container-with-most-water/
# 11. 盛最多水的容器

from typing import List


class Solution:
    """
        使用双指针
            left, right = 0, len(height) - 1

            首先计算容积,如果大于 max 则将 max 置为当前容积
            接着比较 height[left] 与 height[right]
            高较小的那个指针移动,
    """
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        _max = 0

        while left < right:
            _max = max(_max, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return _max


s = Solution()
print(s.maxArea([1, 3, 2, 5, 25, 24, 5]))
