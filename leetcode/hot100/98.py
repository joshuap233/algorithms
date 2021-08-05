# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 98. 验证二叉搜索树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        解法1, 将值存入数组在判断
    """

    def isValidBST(self, root: TreeNode) -> bool:
        value = []

        def recur(node: TreeNode) -> None:
            if not node:
                return

            recur(node.left)
            value.append(node.val)
            recur(node.right)

        recur(root)
        for i in range(1, len(value)):
            if value[i] <= value[i - 1]:
                return False
        return True


class Solution:
    """
        解法2, 递归过程中判断
        使用 prev 存储中序遍历上一个节点
        (在 recur(node.left) 与 recur(node.right) 直接为prev 赋值即可)

        节点的左子树只包含小于当前节点的数。
        节点的右子树只包含大于当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。

    """

    def isValidBST(self, root: TreeNode) -> bool:
        isValid = True
        prev = float('-inf')

        def recur(node: TreeNode) -> None:
            nonlocal prev, isValid
            if not node or not isValid:
                return

            recur(node.left)
            if node.val <= prev:
                isValid = False

            prev = node.val
            recur(node.right)

        recur(root)
        return isValid
