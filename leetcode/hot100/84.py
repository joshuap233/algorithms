# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
# 84. 柱状图中最大的矩形

from typing import List
from collections import deque

class Solution:
    """
       错误的想法: 找到左边最低的....
       比如 5,6,2... 很明显上面的想法不行

      看这题目感觉和单调栈有关.....

      暴力解法:
        当前元素为 i,向左延伸,找到最后一个 >= i 的元素,
        向右延伸,找到最后一个 >= i 的元素,计算面积,然后停止延伸!!
        那么问题来了,为什么小于 i 的元素不用管了呢? 比如有个 j 元素,
        应为这是 j 元素的 "职责", j 元素向两边延伸再算面积!!
        如果 i 继续元素,会有重复计算!

     优化:
        构建递增栈, 单调栈存取索引,具体的值从 heights 数组取
        这题用单调栈存取的是还没有求面积的元素
        遍历过程中构建单调栈:
            当前元素为 i, 如果 i 比栈顶元素大,则将 i 入栈,
            否则出栈,直到栈顶元素比 i 大.....
            出栈过程中计算栈顶元素面积,麻烦的是宽度:

            假如出栈元素是 a,栈顶元素是 b,
            宽度为 i - a 吗?
            不, a, b 之间可能有其他已经出栈的元素, 这些元素
            必然比 height[a] 大,因此宽为 i - b -1
        下面在 stack 中添加哨兵节点, 使得无需判断 stack 为空,
        (而且不这么设置, 遍历完成后栈内依然有节点,需要多余的代码清空栈)
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque([0])
        heights = [0] + heights + [0]

        maxi = 0
        for i, v in enumerate(heights):
            while heights[stack[-1]] > v:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                maxi = max(maxi, height * width)
            stack.append(i)
        return maxi


s = Solution()
s.largestRectangleArea([2, 1, 5, 6, 2, 3])
