# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/
# 440. 字典序的第K小数字
from typing import Optional


class Solution:
    """字典树"""

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1

        while k > 0:
            cnt = 0
            left, right = cur, cur + 1
            # cnt 为以 cur 为父节点的树的儿子数
            while left <= n:
                cnt += min(right, n + 1) - left
                left *= 10
                right *= 10

            # cnt 包括了当前节点, 而 k 不包括当前节点
            if cnt <= k:
                k -= cnt
                cur = cur + 1
            else:
                k -= 1
                cur = cur * 10
        return cur


s = Solution()
print(s.findKthNumber(2, 2))
