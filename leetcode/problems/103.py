# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# 103. 二叉树的锯齿形层序遍历

from typing import List
from leetcode.helper.tree import TreeNode


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
