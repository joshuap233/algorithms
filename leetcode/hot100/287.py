# https://leetcode-cn.com/problems/find-the-duplicate-number/
# 287. 寻找重复数

from typing import List


class Solution:
    """
        你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

        特点是其数字都在 1 到 n 之间
        也就是值 = 索引+1,然而不能修改 nums....

        不要求常量空间可以直接排序...或使用 Counter 也行

        可以将数组看成链表,
        比如 [1,3,4,2,2]
        index(0) 跳转到 index(1) 处
        index(1) 跳转到 index(3) 处....
        值 != 索引 +1 的位置连接成链表,由于链表中有两个或多个节点
        跳转向同一个节点,则必然形成环...

        至于 [2,1,3] 这种情况, 1->1 也能形成环,但,如果没有其他
        索引为 1 的数,不可能跳转到索引 1
    """

    def findDuplicate(self, nums: List[int]) -> int:
        # 索引
        fast, slow = 0, 0
        # ......Python 没有do while

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                p = 0
                while slow != p:
                    slow = nums[slow]
                    p = nums[p]
                return p
