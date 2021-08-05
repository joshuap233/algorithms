# https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
# 剑指 Offer 66. 构建乘积数组

from typing import List
from array import array


class Solution:
    """
    直接用 list 居然比 array 快。。。
    遍历三遍即可，创建两个辅助列表 a,b
    a[i] 存取 i 之前(包括a[i])的元素乘积
    b[j] 存取 j 之后(包括b[j])的元素乘积

    注意 A[0,1,…,n-1] 指的是数组 A 有 n 个元素, 而不是
    数组 A为 [0,1,2,3,4...n-1]

    时间复杂度 O(n), 空间复杂度 O(n)
    """

    def constructArr(self, a: List[int]) -> List[int]:
        f = [1] * (len(a) + 1)
        b = [1] * (len(a) + 1)

        res = 1
        for j in range(len(a)):
            res *= a[j]
            f[j] = res

        res = 1
        for j in reversed(range(len(a))):
            res *= a[j]
            b[j] = res

        return [f[i - 1] * b[i + 1] for i in range(len(a))]


class Solution1:
    """
    优化上面的代码

    还是时间复杂度 O(n), 空间复杂度 O(n)
    """
    def constructArr(self, a: List[int]) -> List[int]:
        ans = [0] * len(a)

        res = 1
        for j in range(len(a)):
            ans[j] = res
            res *= a[j]

        res = 1
        for j in reversed(range(len(a))):
            ans[j] *= res
            res *= a[j]

        return ans


s = Solution1()
s.constructArr([1, 2, 3, 4, 5])
