# https://leetcode-cn.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
       没看清题目,....第一遍就写错了
       后续遍历,取左右子树深度之和的最大值即可
    """

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxi = 0

        def recur(node: TreeNode):
            nonlocal maxi
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            # 计算路径长
            maxi = max(maxi, left + right)

            # 返回深度
            return max(left, right) + 1

        recur(root)
        return maxi
