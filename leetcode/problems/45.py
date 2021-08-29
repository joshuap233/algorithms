# https://leetcode-cn.com/problems/jump-game-ii/
# 45. 跳跃游戏 II

from typing import List


class Solution:
    """
        O(n) 贪心
        不需要知道具体如何跳跃, 只需要只当前可跳跃最大区间,
        然后从当前可跳跃区间中找到下一个最大区间,
        多个最大区间叠加必然是跳跃次数最少的
    """

    def jump(self, nums: List[int]) -> int:
        maxi = end = 0
        cnt = 0
        for i in range(len(nums) - 1):
            maxi = max(maxi, i + nums[i])
            if i == end:
                end = maxi
                cnt += 1
        return cnt


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
