# https://leetcode-cn.com/problems/longest-consecutive-sequence/
# 128. 最长连续序列

from typing import List


class Solution:
    """
        O(n)
        也就是不能直接排序了....

        遍历两遍,一遍建立字典 {value: False}
        另一遍以当前值为中心扩散,比如当前值为 i,
        判断 i,i+1,i-1 是否在字典中,在则标记为True
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        Dict = {}
        for i in nums:
            Dict[i] = False

        maxi = 0
        for i in nums:
            if not Dict[i]:
                tmp1 = i + 1
                while tmp1 in Dict:
                    Dict[tmp1] = True
                    tmp1 += 1

                tmp2 = i - 1
                while tmp2 in Dict:
                    Dict[tmp2] = True
                    tmp2 -= 1
                maxi = max(maxi, tmp1 - tmp2 - 1)
        return maxi


class Solution:
    """
        O(n),上面的代码优化, 使用 set , 删掉连续的数组即可
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        maxi = 0
        while Set:
            i = Set.pop()
            tmp1 = i + 1
            while tmp1 in Set:
                Set.remove(tmp1)
                tmp1 += 1

            tmp2 = i - 1
            while tmp2 in Set:
                Set.remove(tmp2)
                tmp2 -= 1
            maxi = max(maxi, tmp1 - tmp2 - 1)
        return maxi


s = Solution()
s.longestConsecutive([100, 4, 200, 1, 3, 2])
