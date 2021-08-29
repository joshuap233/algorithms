# https://leetcode-cn.com/problems/delete-node-in-a-bst/
# 450. 删除二叉搜索树中的节点

from leetcode.helper.tree import TreeNode


class Solution:
    @staticmethod
    def findMin(node: TreeNode) -> int:
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left and root.right):
                return root.left or root.right
            root.val = self.findMin(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root
