# https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
# 剑指 Offer 55 - II. 平衡二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        bal = True

        def recur(node):
            nonlocal bal
            if not node:
                return 0
            left = recur(node.right) + 1
            right = recur(node.left) + 1

            if abs(left - right) > 1:
                bal = False

            return max(left, right)

        recur(root)
        return bal
