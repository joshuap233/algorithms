# https://leetcode-cn.com/problems/path-sum/
# 112. 路径总和
from typing import Optional
from leetcode.helper.tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(node: TreeNode, s: int) -> bool:
            if not node:
                return False

            s += node.val
            if not (node.left or node.right):
                return s == targetSum

            return recur(node.left, s) or recur(node.right, s)

        if not root:
            return False

        return recur(root, 0)
