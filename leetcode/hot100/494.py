# https://leetcode-cn.com/problems/target-sum/
# 494. 目标和
# 这个好像叫 背包问题
# 背包问题:
# https://leetcode-cn.com/problems/target-sum/solution/dai-ma-sui-xiang-lu-494-mu-biao-he-01bei-rte9/

from functools import lru_cache
from typing import List


class Solution:
    """
        串联起[所有]整数，可以构造一个 表达式
        就是向整数中间填数'+' 或'-' 呗....
        数组顺序是不可以变的....

        这玩意的时间复杂度是 O(2**n)
        n 是 nums 数组的长度

        lru_cache 参数为 None 时不设置最大值,默认值为 128
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def recur(left: int, _sum: int) -> int:
            if left == len(nums):
                return 1 if _sum == target else 0
            return recur(left + 1, _sum + nums[left]) + recur(left + 1, _sum - nums[left])

        return recur(0, 0)


class Solution1:
    """
        动态规划版...
        能够以「递归」的形式实现动态规划（记忆化搜索），自然也能使用「递推」的方式进行实现。
        所以动态规划的键是 left 与 _sum(也就是上面递归记忆的键)
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        dp[i][j] 表示第 i 个数,计算结果为 j 的方案数
        递推方程:
            dp[i][j] = dp[i-1][j - num[i]] + dp[i-1][j + num[i]]
        计算结果范围为 [-sum(nums), sum(nums)]
        -sum(nums) 对应索引 0, 因此访问结果的索引需要 偏移 sum(nums)

        慢得离谱...但好歹写出来了
        """
        Sum = sum(nums)
        if target > Sum:
            return 0

        n = Sum * 2 + 1
        dp = [[0] * n for _ in nums]
        dp[0][nums[0] + Sum] = 1
        dp[0][-nums[0] + Sum] += 1
        for i in range(1, len(nums)):
            for j in range(n):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]
                if j + nums[i] < n:
                    dp[i][j] += dp[i - 1][j + nums[i]]
        return dp[-1][target + Sum]


class Solution2:
    """
        这是别人题解的递推方程:
            dp[i][j] = dp[i-1][j - num[i-1]] + dp[i-1][j + num[i-1]]
            表示前 i 个数, 计算结果为 j 的方案数(不包括 i)
        初始条件:
                (0, 0) = 1
                也就是 dp[0][Sum] = 1

        我的:
            dp[i][j] = dp[i-1][j - num[i]] + dp[i-1][j + num[i]]
            dp[i][j] 表示第 i 个数,计算结果为 j 的方案数
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Sum = sum(nums)
        if target > Sum:
            return 0

        n = Sum * 2 + 1
        dp = [[0] * n for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            p = nums[i - 1]
            for j in range(n):
                if j - p >= 0:
                    dp[i][j] += dp[i - 1][j - p]
                if j + p < n:
                    dp[i][j] += dp[i - 1][j + p]
        return dp[-1][target + Sum]


class Solution3:
    """
        可以用 i-1 推 i 列, 跳过次数为 0 的项,这种方法更好理解
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Sum = sum(nums)
        if target > Sum:
            return 0

        n = Sum * 2 + 1
        dp = [[0] * n for _ in range(len(nums) + 1)]
        dp[0][Sum] = 1
        for i in range(len(nums)):
            sums = dp[i]
            for j, cnt in enumerate(sums):
                if cnt == 0:
                    continue
                dp[i + 1][j + nums[i]] += cnt
                dp[i + 1][j - nums[i]] += cnt
        return dp[-1][target + Sum]


class Solution4:
    """
        在上述「动态规划」分析中，我们总是尝试将所有的状态值都计算出来，
        当中包含很多对「目标状态」不可达的“额外”状态值。
        即达成某些状态后，不可能再回到我们的「目标状态」。

        比如 target != s/-s 时, s 与 -s 就是不可达额外状态
        (s = Sum(nums))

        我怎么知道哪些状态不可达?????
        麻了....
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        pass


s = Solution3()
s.findTargetSumWays([1, 1, 1, 1, 1], 3)
