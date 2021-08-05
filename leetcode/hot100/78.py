# https://leetcode-cn.com/problems/subsets/
# 78. 子集

from typing import List


class Solution:
    """
        解法错误.....有重复元素.....没找到去重剪枝的办法...
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def traceback(array: list):
            res.append(array[:])

            for i in range(len(array)):
                e = nums.pop(i)
                traceback(array)
                array.append(e)

        traceback(nums)
        return res


class Solution1:
    """
        分析回溯题的时候画出一棵树,用于分析与剪枝
        递归传递一个 left,继续上次添加到数组的值在 nums 中的索引+1
        用于递归与剪枝
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(left: int, array: list) -> None:
            res.append(array)

            for i in range(left, len(nums)):
                recur(i + 1, array + [nums[i]])

        recur(0, [])
        return res


s = Solution1()
print(s.subsets([1, 2, 3]))
