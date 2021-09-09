# https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
# 剑指 Offer 51. 数组中的逆序对

from typing import List
from bisect import bisect_left

"""
python 数组赋值
In [1]: a = [1,2,3,4]                                                                                           

In [2]: b = [0]*4                                                                                               

In [3]: b[1:3] = a[1:3]                                                                                         

In [4]: b                                                                                                       
Out[4]: [0, 2, 3, 0]
"""


class Solution:
    """
        nLogN
        利用归并排序, 将数组拆分
        比如
    先拆:
           7, 3, 2, 6, 0, 1, 5, 4
                     |
           7,3,2,6      0,1,5,4
              |            |
           7,3  2,6     0,1  5,4     统计每组中的逆序对
    再合并
           2,3,6,7      0,1,4,5     统计前面的数组与后面的数组中逆序对的个数


    """

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cnt = 0

        def merge_sort(left: int, right: int) -> list:
            nonlocal cnt
            if right == left:
                return [nums[left]]

            mid = (left + right) // 2
            array1 = merge_sort(left, mid)
            array2 = merge_sort(mid + 1, right)
            new = []

            p1, p2 = 0, 0

            while p1 < len(array1) and p2 < len(array2):
                if array1[p1] > array2[p2]:
                    new.append(array2[p2])
                    p2 += 1
                else:
                    new.append(array1[p1])
                    cnt += p2
                    p1 += 1

            if p1 < len(array1):
                cnt += (len(array1) - p1) * len(array2)
                new.extend(array1[p1:])
            elif p2 < len(array2):
                new.extend(array2[p2:])
            return new

        merge_sort(0, len(nums) - 1)
        return cnt


class Solution2:
    """
        比上面的要快
        O(n*n)
    """

    def reversePairs(self, nums: List[int]) -> int:
        temp = []
        res = 0
        for t in reversed(nums):
            i = bisect_left(temp, t)
            res += i
            # python 的切片赋值比 insert 快了一大截
            # 好像是因为切片赋值底层用的汇编的内存拷贝?
            temp[i:i] = [t]
        return res
