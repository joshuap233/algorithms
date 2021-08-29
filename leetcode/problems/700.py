# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
# 700. 二叉搜索树中的搜索

from leetcode.helper.tree import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        return self.searchBST(root.left, val) \
            if val < root.val else self.searchBST(root.right, val)
