# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# 94. 二叉树的中序遍历


from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def recur(node: TreeNode):
            if not node:
                return
            recur(node.left)
            res.append(node.val)
            recur(node.right)

        recur(root)
        return res


class Solution1:
    """迭代"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        q = deque()

        while root or q:
            while root:
                q.append(root)
                root = root.left

            root = q.pop()
            ret.append(root.val)
            root = root.right
        return ret
