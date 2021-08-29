# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
# 701. 二叉搜索树中的插入操作


from leetcode.helper.tree import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
