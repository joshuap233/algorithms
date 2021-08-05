# Definition for a binary tree node.
# https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
# 剑指 Offer 26. 树的子结构

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False

        def recursive2(node1: TreeNode, target: TreeNode):
            if target is None:
                return True
            if ((not node1) and target) or node1.val != target.val:
                return False
            return recursive2(node1.left, target.left) and recursive2(node1.right, target.right)

        def recursive(node: TreeNode):
            if not node:
                return False
            if node.val == B.val and recursive2(node, B):
                return True
            return recursive(node.left) or recursive(node.right)

        return recursive(A)
