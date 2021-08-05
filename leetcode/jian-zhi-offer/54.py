# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
# 剑指 Offer 54. 二叉搜索树的第k大节点

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        v = 0

        def recur(node):
            nonlocal k, v
            if k == 0:
                return

            node.right and recur(node.right)

            k -= 1
            if k == 0:
                v = node.val
                return

            node.left and recur(node.left)

        recur(root)
        return v
