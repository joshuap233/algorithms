# https://leetcode-cn.com/problems/target-sum/
# 494. 目标和
# 这个好像叫 背包问题
# 背包问题:
# https://leetcode-cn.com/problems/target-sum/solution/dai-ma-sui-xiang-lu-494-mu-biao-he-01bei-rte9/

from typing import List


class Solution:
    """
        串联起[所有]整数，可以构造一个 表达式
        就是向整数中间填数'+' 或'-' 呗....
        数组顺序是不可以变的....

        超时了...,即使使用了 lru_cache....

        这玩意的时间复杂度是 O(2**n)
        n 是 nums 数组的长度

        给爷看傻了....官方就是这种方法...没 Python 版
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recur(left: int, _sum: int) -> int:
            if left == len(nums):
                return 1 if _sum == target else 0
            return recur(left + 1, _sum + nums[left]) + recur(left + 1, _sum - nums[left])

        return recur(0, 0)


s = Solution()
s.findTargetSumWays([1, 1, 1, 1, 1], 1)
