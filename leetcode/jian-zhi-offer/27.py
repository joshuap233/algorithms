# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
# 剑指 Offer 27. 二叉树的镜像


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(node: TreeNode):
            if not node:
                return
            node.left, node.right = node.right, node.left
            recur(node.left)
            recur(node.right)

        recur(root)
        return root


# 迭代:
class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        stack = [root]
        while stack:
            node = stack.pop(-1)
            node.left, node.right = node.right, node.left
            node.left and stack.append(node.left)
            node.right and stack.append(node.right)
        return root
