# https://leetcode-cn.com/problems/subarray-sum-equals-k/
# 560. 和为K的子数组

from typing import List


class Solution:
    """
        和为K连续的子数组
        注意数组中是有负数的....., 所以滑动窗口没用....
        暴力解 O(n*n)
        估计需要优化成 O(n) ....

        设置一个辅助数据结构存取之前的和即可
            比如遍历到 i
            辅助结构 [a1,a2,a3...ai-1]
            如果 当前的和 - am == k
            m - i 为一个连续子数组,
        使用 Counter 作为辅助结构,
        麻烦的地方在于初始化, 初始化时, 哈希表有一个元素 {0:1},
        且 counter 计数在 if Sum - k in counter: 之后

    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        counter = Counter({0: 1})

        Sum = 0
        cnt = 0
        for i in nums:
            Sum += i

            if Sum - k in counter:
                cnt += counter[Sum - k]
            counter[Sum] += 1
        return cnt


s = Solution()
s.subarraySum([1, 1, 1], 2)
