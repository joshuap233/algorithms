# https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/
# 1658. 将 x 减到 0 的最小操作数
from typing import List


class Solution:
    """
        注意数值是大于 0 的,没有负数,
        使用双指针, 找两端值的和可以转化为找中间值的和
        (也可以从左到右遍历, 找到是和大于 x 的值的位置,置为左指针,
        然后有指针从数组末尾开始向左移动,这种方式编码麻烦)
    """

    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        target = s - x
        if target < 0:
            return -1
        left = right = 0
        maxi = -1
        while right < len(nums):
            target -= nums[right]
            right += 1
            while target < 0:
                target += nums[left]
                left += 1
            if target == 0:
                maxi = max(maxi, right - left)
        return maxi if maxi == -1 else len(nums) - maxi


so = Solution()
so.minOperations([
    1, 1, 4, 2, 3
], 5)
