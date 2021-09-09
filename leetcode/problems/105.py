# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 105. 从前序与中序遍历序列构造二叉树
from typing import List, Optional
from leetcode.helper.tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre, ino) -> Optional[TreeNode]:
            if not pre:
                return None

            rv = pre[0]
            root = TreeNode(rv)
            if len(pre) == 1:
                return root

            i = ino.index(rv)
            root.left = build(pre[1:1 + i], ino[:i])
            root.right = build(pre[1 + i:], ino[i + 1:])
            return root

        return build(preorder, inorder)
