# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# 103. 二叉树的锯齿形层序遍历

from typing import List
from leetcode.helper.tree import TreeNode
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            cur = []
            for i in range(len(queue)):
                e = queue.pop(0)
                e.left and queue.append(e.left)
                e.right and queue.append(e.right)
                cur.append(e.val)
            res.append(cur)

        for i, v in enumerate(res):
            if i % 2 == 1:
                v.reverse()
        return res


class Solution1:
    """上面代码优化"""

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ret = []
        q = deque([root])
        j = 0
        while q:
            cur = [0] * len(q)
            for i in range(len(q)):
                e = q.popleft()
                cur[(-i - 1) if j % 2 else i] = e.val
                e.left and q.append(e.left)
                e.right and q.append(e.right)
            ret.append(cur)
            j += 1
        return ret
