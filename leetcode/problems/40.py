# https://leetcode-cn.com/problems/combination-sum-ii/
# 40. 组合总和 II
from typing import List


class Solution:
    """
        ca 中可能有重复的数字, 因此造成最终结果重复,
        去重: list 没法加入到 set 中...

        去重的方法:
        首先将 ca 排序, 然后:
        if i > left and ca[i - 1] == ca[i]:
            continue
        比如序列 [1,1,2,5,6,7,10]
        如果尝试过 1 ,当前循环不会在尝试 1
        与 三数之和的去重非常像
    """

    def combinationSum2(self, ca: List[int], target: int) -> List[List[int]]:
        ca.sort()

        def backtrace(left: int, s: int):
            if s > target:
                return

            if s == target:
                ret.append(cur[:])

            for i in range(left, len(ca)):
                if i > left and ca[i - 1] == ca[i]:
                    continue
                cur.append(ca[i])
                backtrace(i + 1, ca[i] + s)
                cur.pop()

        ret = []
        cur = []
        backtrace(0, 0)
        return ret
