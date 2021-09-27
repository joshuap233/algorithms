# 503. 下一个更大元素 II
from typing import List
from collections import deque


class Solution:
    """
        题目给的循环数组,要求循环搜索...
        解决: 直接将 nums 复制两倍
    """

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = deque()
        le = len(nums)
        ret = [-1] * le
        nums.extend(nums[:])
        for i, v in enumerate(nums):
            while stack and nums[stack[-1]] < v:
                ret[stack.pop()] = v
            if i < le:
                stack.append(i)
        return ret


s = Solution()
s.nextGreaterElements([5, 4, 3, 2, 1])
