# https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
# 剑指 Offer 68 - II. 二叉树的最近公共祖先


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        注意这里是二叉树, 不是二叉搜索树

        若 root 是 p, q 的 最近公共祖先 ，则只可能为以下情况之一：
            p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
            p=root ，且 q 在 root 的左或右子树中；
            q=root ，且 p 在 root 的左或右子树中；

        这种题目就是要选择二叉树遍历方式...,
        为了回溯查找根节点,只能用后续遍历,也就是将判断
        是否为父节点的代码放到最后

        还有一个难点是,怎么判断一个节点是最近的公共祖先
    """

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        # 如果左子树不存在 q, 那么 left 为 None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 当前节点为公共节点
        if left and right:
            return root

        # 1. right 不为 None 则 right 树有 p 或 q
        # 2. left 不为 None 则 left 树有 p 或 1
        # 3. right 或 left 都为空,则 root 树不包括 p 或 q
        return right or left
