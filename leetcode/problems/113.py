# https://leetcode-cn.com/problems/path-sum-ii/
# 113. 路径总和 II
from leetcode.helper.tree import TreeNode
from typing import Optional, List


class Solution:
    """
        叶子节点 是指没有子节点的节点。
    """

    def pathSum(self, root: Optional[TreeNode], s: int) -> List[List[int]]:
        def backtrace(node: TreeNode, s: int):
            if not node:
                return

            s -= node.val
            cur.append(node.val)
            if not (node.left or node.right):
                if s == 0:
                    ret.append(cur[:])
                cur.pop(-1)
                return

            backtrace(node.left, s)
            backtrace(node.right, s)
            cur.pop(-1)

        ret = []
        cur = []
        backtrace(root, s)
        return ret
