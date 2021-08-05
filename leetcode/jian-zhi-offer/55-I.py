# https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
# 剑指 Offer 55 - I. 二叉树的深度


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        _max = 0

        def recur(node, deep):
            nonlocal _max
            if not node:
                _max = max(_max, deep)
                return
            deep += 1
            recur(node.left, deep)
            recur(node.right, deep)

        recur(root, 0)
        return _max


# 简单的写法：
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
