# https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
# 剑指 Offer 28. 对称的二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def recur(node1: TreeNode, node2: TreeNode) -> bool:
            if (not node1) and (not node2):
                return True
            if node1 and node2 and node1.val == node2.val:
                return recur(node1.left, node2.right) and recur(node1.right, node2.left)
            return False

        return recur(root, root)


# 迭代
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        stack1, stack2 = [root], [root]

        while stack1 and stack2:
            node1 = stack1.pop(-1)
            node2 = stack2.pop(-1)
            if node1 and node2 and node1.val == node2.val:
                stack1.append(node1.right)
                stack1.append(node1.left)
                stack2.append(node2.left)
                stack2.append(node2.right)
            elif not (not node1 and not node2):
                return False
        return False if (stack1 or stack2) else True
