# https://leetcode-cn.com/problems/burst-balloons/
# 312. 戳气球

from typing import List
from functools import lru_cache


class Solution:
    """
        回溯 + lru_cache,

        错误的思路:
        每次去除一个气球
        回溯会改变气球顺序.....写了半天结果思路是错的....

        我们从底向上推,添加气球而不是戳爆气球,
        设置 left, right 指针, 指向需要添加的气球两端,
        因此需要在 num 数组两端添加 1 ,left, right
        初始时指向 0,len(num-1),然后递归即可....

        挺慢的...不管还算好理解
    """

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def recur(left: int, right: int) -> int:
            if left + 1 >= right:
                return 0

            maxi = 0
            for i in range(left + 1, right):
                val = nums[left] * nums[i] * nums[right]
                # i 在新添加的气球边缘
                maxi = max(maxi, recur(left, i) + recur(i, right) + val)
            return maxi

        return recur(0, len(nums) - 1)


s = Solution()
s.maxCoins([9, 76, 64, 21])
